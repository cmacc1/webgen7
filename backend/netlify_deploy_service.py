"""
Netlify Deployment Service
Handles automatic site creation, deployment, and monitoring via Netlify API
"""
import os
import logging
import aiohttp
import json
import zipfile
import io
import base64
from typing import Dict, Any, Optional, List

logger = logging.getLogger(__name__)

class NetlifyDeployService:
    def __init__(self, api_token: str):
        self.api_token = api_token
        self.base_url = "https://api.netlify.com/api/v1"
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }
    
    async def create_site(self, site_name: str, project_files: Dict[str, str]) -> Dict[str, Any]:
        """
        Create a new Netlify site and deploy files
        Returns site info including Deploy Preview URL
        """
        logger.info(f"🚀 Creating Netlify site: {site_name}")
        
        try:
            async with aiohttp.ClientSession() as session:
                # Step 1: Create site
                site_data = await self._create_site_api(session, site_name)
                site_id = site_data.get("id")
                site_url = site_data.get("url")
                
                logger.info(f"✅ Site created: {site_id}")
                logger.info(f"   URL: {site_url}")
                
                # Step 2: Deploy files
                deploy_data = await self._deploy_files(session, site_id, project_files)
                deploy_id = deploy_data.get("id")
                deploy_url = deploy_data.get("deploy_ssl_url") or deploy_data.get("url")
                
                logger.info(f"✅ Deployment created: {deploy_id}")
                logger.info(f"   Deploy URL: {deploy_url}")
                
                # Step 3: Wait for build to complete
                build_status = await self._wait_for_build(session, deploy_id)
                
                # Get the clean site URL (without deploy ID prefix)
                clean_site_url = site_data.get("ssl_url") or f"https://{site_data.get('name')}.netlify.app"
                
                logger.info(f"✅ Clean Site URL: {clean_site_url}")
                
                return {
                    "site_id": site_id,
                    "site_name": site_data.get("name"),
                    "site_url": clean_site_url,  # Use clean URL
                    "deploy_id": deploy_id,
                    "deploy_url": clean_site_url,  # Use clean URL
                    "deploy_preview_url": clean_site_url,  # Use clean URL for consistency
                    "deploy_preview_url_with_id": deploy_url,  # Keep original for reference
                    "build_status": build_status,
                    "admin_url": site_data.get("admin_url"),
                    "ssl_url": clean_site_url
                }
                
        except Exception as e:
            logger.error(f"❌ Netlify deployment failed: {str(e)}")
            raise
    
    async def _create_site_api(self, session: aiohttp.ClientSession, site_name: str) -> Dict[str, Any]:
        """Create a new site via Netlify API"""
        
        # Generate unique site name
        import time
        unique_name = f"{site_name}-{int(time.time())}"
        
        payload = {
            "name": unique_name,
            "custom_domain": None,
            "processing_settings": {
                "skip_processing": False
            }
        }
        
        async with session.post(
            f"{self.base_url}/sites",
            headers=self.headers,
            json=payload
        ) as response:
            if response.status not in [200, 201]:
                error_text = await response.text()
                logger.error(f"Site creation failed: {error_text}")
                raise Exception(f"Failed to create site: {response.status} - {error_text}")
            
            return await response.json()
    
    async def _deploy_files(self, session: aiohttp.ClientSession, site_id: str, files: Dict[str, str]) -> Dict[str, Any]:
        """Deploy files to Netlify site using zip upload"""
        
        logger.info(f"📦 Preparing deployment with {len(files)} files")
        
        # Create ZIP file in memory
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for filepath, content in files.items():
                # Ensure proper encoding
                if isinstance(content, str):
                    content = content.encode('utf-8')
                zip_file.writestr(filepath, content)
        
        zip_data = zip_buffer.getvalue()
        logger.info(f"📦 ZIP size: {len(zip_data)} bytes")
        
        # Upload via Netlify API
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/zip"
        }
        
        async with session.post(
            f"{self.base_url}/sites/{site_id}/deploys",
            headers=headers,
            data=zip_data
        ) as response:
            if response.status not in [200, 201]:
                error_text = await response.text()
                logger.error(f"Deployment failed: {error_text}")
                raise Exception(f"Failed to deploy: {response.status} - {error_text}")
            
            deploy_data = await response.json()
            logger.info(f"✅ Deployment uploaded successfully")
            return deploy_data
    
    async def _wait_for_build(self, session: aiohttp.ClientSession, deploy_id: str, max_wait: int = 180) -> Dict[str, Any]:
        """Wait for build to complete and return status"""
        
        import asyncio
        
        logger.info(f"⏳ Waiting for build to complete (max {max_wait}s)...")
        
        start_time = asyncio.get_event_loop().time()
        check_interval = 3  # seconds
        
        while True:
            elapsed = asyncio.get_event_loop().time() - start_time
            
            if elapsed > max_wait:
                logger.warning(f"⚠️ Build timeout after {max_wait}s")
                return {
                    "state": "timeout",
                    "message": f"Build did not complete within {max_wait} seconds"
                }
            
            # Check deploy status
            async with session.get(
                f"{self.base_url}/deploys/{deploy_id}",
                headers=self.headers
            ) as response:
                if response.status == 200:
                    deploy_data = await response.json()
                    state = deploy_data.get("state")
                    
                    logger.info(f"   Build state: {state} ({elapsed:.1f}s elapsed)")
                    
                    if state == "ready":
                        logger.info(f"✅ Build completed successfully!")
                        return {
                            "state": "ready",
                            "message": "Build completed successfully",
                            "deploy_time": deploy_data.get("deploy_time"),
                            "published_at": deploy_data.get("published_at")
                        }
                    elif state in ["error", "failed"]:
                        error_msg = deploy_data.get("error_message", "Unknown error")
                        logger.error(f"❌ Build failed: {error_msg}")
                        return {
                            "state": "error",
                            "message": error_msg
                        }
                    elif state in ["building", "processing", "enqueued", "preparing"]:
                        # Still building, wait and check again
                        await asyncio.sleep(check_interval)
                        continue
                    else:
                        logger.warning(f"⚠️ Unknown state: {state}")
                        await asyncio.sleep(check_interval)
                        continue
                else:
                    logger.error(f"Failed to check deploy status: {response.status}")
                    await asyncio.sleep(check_interval)
                    continue
    
    async def update_site(self, site_id: str, project_files: Dict[str, str]) -> Dict[str, Any]:
        """
        Update existing site with new deployment
        Creates a new deploy for the existing site
        """
        logger.info(f"🔄 Updating Netlify site: {site_id}")
        
        try:
            async with aiohttp.ClientSession() as session:
                # Deploy new version
                deploy_data = await self._deploy_files(session, site_id, project_files)
                deploy_id = deploy_data.get("id")
                deploy_url = deploy_data.get("deploy_ssl_url") or deploy_data.get("url")
                
                logger.info(f"✅ New deployment: {deploy_id}")
                
                # Wait for build
                build_status = await self._wait_for_build(session, deploy_id)
                
                return {
                    "site_id": site_id,
                    "deploy_id": deploy_id,
                    "deploy_url": deploy_url,
                    "deploy_preview_url": deploy_url,
                    "build_status": build_status
                }
                
        except Exception as e:
            logger.error(f"❌ Site update failed: {str(e)}")
            raise
    
    async def get_site_info(self, site_id: str) -> Dict[str, Any]:
        """Get information about a Netlify site"""
        
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.base_url}/sites/{site_id}",
                headers=self.headers
            ) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    error_text = await response.text()
                    raise Exception(f"Failed to get site info: {response.status} - {error_text}")
    
    async def get_deploy_status(self, deploy_id: str) -> Dict[str, Any]:
        """Get status of a specific deployment"""
        
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.base_url}/deploys/{deploy_id}",
                headers=self.headers
            ) as response:
                if response.status == 200:
                    deploy_data = await response.json()
                    return {
                        "deploy_id": deploy_id,
                        "state": deploy_data.get("state"),
                        "url": deploy_data.get("deploy_ssl_url") or deploy_data.get("url"),
                        "published_at": deploy_data.get("published_at"),
                        "error_message": deploy_data.get("error_message")
                    }
                else:
                    error_text = await response.text()
                    raise Exception(f"Failed to get deploy status: {response.status} - {error_text}")
    
    async def list_sites(self, limit: int = 10) -> List[Dict[str, Any]]:
        """List all sites in the account"""
        
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.base_url}/sites?per_page={limit}",
                headers=self.headers
            ) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    error_text = await response.text()
                    raise Exception(f"Failed to list sites: {response.status} - {error_text}")
    
    async def delete_site(self, site_id: str) -> bool:
        """Delete a Netlify site"""
        
        logger.info(f"🗑️  Deleting site: {site_id}")
        
        async with aiohttp.ClientSession() as session:
            async with session.delete(
                f"{self.base_url}/sites/{site_id}",
                headers=self.headers
            ) as response:
                if response.status in [200, 204]:
                    logger.info(f"✅ Site deleted successfully")
                    return True
                else:
                    error_text = await response.text()
                    logger.error(f"❌ Failed to delete site: {error_text}")
                    return False
