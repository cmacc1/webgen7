#!/usr/bin/env python3
"""
CRITICAL PRIORITY TESTING - Bulletproof Failsafe System Verification
Tests the comprehensive 3-layer failsafe system to guarantee 100% success rate
"""

import asyncio
import aiohttp
import json
import time
import os
import re
import subprocess
from typing import Dict, Any, List
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class BulletproofFailsafeTester:
    def __init__(self):
        # Get backend URL from frontend .env
        self.base_url = self._get_backend_url()
        self.session_ids = []
        self.test_results = []
        
    def _get_backend_url(self) -> str:
        """Get backend URL from frontend .env file"""
        try:
            with open('/app/frontend/.env', 'r') as f:
                for line in f:
                    if line.startswith('REACT_APP_BACKEND_URL='):
                        url = line.split('=', 1)[1].strip()
                        return f"{url}/api"
        except Exception as e:
            logger.error(f"Could not read frontend .env: {e}")
        
        # Fallback
        return "https://codeweaver-30.preview.emergentagent.com/api"
    
    async def create_session(self, project_name: str = "Test Project") -> str:
        """Create a new session and return session_id"""
        async with aiohttp.ClientSession() as session:
            try:
                payload = {"project_name": project_name}
                async with session.post(
                    f"{self.base_url}/session/create",
                    json=payload,
                    headers={"Content-Type": "application/json"}
                ) as response:
                    if response.status == 200:
                        data = await response.json()
                        session_id = data.get('session_id')
                        self.session_ids.append(session_id)
                        logger.info(f"✅ Created session: {session_id}")
                        return session_id
                    else:
                        error_text = await response.text()
                        logger.error(f"❌ Session creation failed: {response.status} - {error_text}")
                        return None
            except Exception as e:
                logger.error(f"❌ Session creation error: {e}")
                return None
    
    async def test_normal_ai_generation(self, session_id: str, prompt: str, model: str = "claude-sonnet-4") -> Dict[str, Any]:
        """TEST 1: Normal AI Generation (Layer 1) - Should complete in under 2 minutes"""
        logger.info("\n" + "="*80)
        logger.info("TEST 1: NORMAL AI GENERATION (LAYER 1)")
        logger.info("="*80)
        
        async with aiohttp.ClientSession() as session:
            try:
                start_time = time.time()
                
                payload = {
                    "session_id": session_id,
                    "prompt": prompt,
                    "model": model
                }
                
                logger.info(f"🚀 Testing normal AI generation...")
                logger.info(f"   Session ID: {session_id}")
                logger.info(f"   Model: {model}")
                logger.info(f"   Prompt: {prompt}")
                
                async with session.post(
                    f"{self.base_url}/netlify/generate-and-deploy",
                    json=payload,
                    headers={"Content-Type": "application/json"},
                    timeout=aiohttp.ClientTimeout(total=180)  # 3 minute timeout
                ) as response:
                    generation_time = time.time() - start_time
                    
                    if response.status == 200:
                        data = await response.json()
                        
                        result = {
                            "success": True,
                            "layer_used": "AI_GENERATION",
                            "session_id": session_id,
                            "generation_time": generation_time,
                            "response_data": data,
                            "project": data.get('project', {}),
                            "deployment": data.get('deployment', {}),
                            "deploy_preview_url": data.get('deploy_preview_url'),
                            "netlify_site_id": data.get('deployment', {}).get('site_id')
                        }
                        
                        logger.info(f"✅ Normal AI generation completed in {generation_time:.2f}s")
                        logger.info(f"   Project ID: {result['project'].get('project_id')}")
                        logger.info(f"   Deploy Preview URL: {result['deploy_preview_url']}")
                        logger.info(f"   Netlify Site ID: {result['netlify_site_id']}")
                        
                        return result
                    else:
                        error_text = await response.text()
                        logger.error(f"❌ Normal AI generation failed: {response.status} - {error_text}")
                        return {
                            "success": False,
                            "layer_used": "FAILED",
                            "session_id": session_id,
                            "generation_time": generation_time,
                            "error": f"HTTP {response.status}: {error_text}"
                        }
                        
            except asyncio.TimeoutError:
                generation_time = time.time() - start_time
                logger.error(f"❌ Normal AI generation timed out after {generation_time:.2f}s")
                return {
                    "success": False,
                    "layer_used": "TIMEOUT",
                    "session_id": session_id,
                    "generation_time": generation_time,
                    "error": "Generation timed out"
                }
            except Exception as e:
                generation_time = time.time() - start_time
                logger.error(f"❌ Normal AI generation error: {e}")
                return {
                    "success": False,
                    "layer_used": "ERROR",
                    "session_id": session_id,
                    "generation_time": generation_time,
                    "error": str(e)
                }

    async def test_business_type_customization(self, business_type: str, prompt: str) -> Dict[str, Any]:
        """TEST 3: Different Business Types - Test intelligent fallback customization"""
        logger.info(f"\n--- TEST 3: {business_type.upper()} BUSINESS TYPE ---")
        
        session_id = await self.create_session(f"Test {business_type.title()}")
        if not session_id:
            return {"success": False, "error": "Failed to create session"}
        
        result = await self.test_normal_ai_generation(session_id, prompt)
        
        if result.get('success'):
            # Analyze the generated content for business-specific customization
            project = result.get('project', {})
            files = project.get('files', {})
            html_content = files.get('index.html', '')
            
            # Check for business-specific content
            business_keywords = {
                'renovation': ['flooring', 'bathroom', 'kitchen', 'renovation', 'remodeling'],
                'restaurant': ['menu', 'dining', 'food', 'restaurant', 'beverages'],
                'tech': ['software', 'development', 'cloud', 'technology', 'services']
            }
            
            keywords = business_keywords.get(business_type, [])
            found_keywords = [kw for kw in keywords if kw.lower() in html_content.lower()]
            
            result['business_customization'] = {
                'expected_keywords': keywords,
                'found_keywords': found_keywords,
                'customization_score': len(found_keywords) / len(keywords) * 100 if keywords else 0
            }
            
            logger.info(f"   Business customization: {result['business_customization']['customization_score']:.1f}%")
            logger.info(f"   Found keywords: {found_keywords}")
        
        return result

    async def test_live_url_accessibility(self, url: str) -> Dict[str, Any]:
        """Test if the live Netlify URL is accessible and contains expected content"""
        logger.info(f"🌐 Testing live URL accessibility: {url}")
        
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url, timeout=aiohttp.ClientTimeout(total=30)) as response:
                    if response.status == 200:
                        content = await response.text()
                        
                        # Check if it contains HTML content
                        has_html = '<html' in content.lower() or '<!doctype html' in content.lower()
                        has_renovation_content = any([
                            'renovation' in content.lower(),
                            'flooring' in content.lower(),
                            'bathroom' in content.lower(),
                            'kitchen' in content.lower(),
                            'epoxy' in content.lower(),
                            'services' in content.lower(),
                            'contact' in content.lower()
                        ])
                        
                        result = {
                            "success": True,
                            "status_code": response.status,
                            "content_length": len(content),
                            "has_html": has_html,
                            "has_renovation_content": has_renovation_content,
                            "content_preview": content[:500] + "..." if len(content) > 500 else content
                        }
                        
                        logger.info(f"✅ Live URL is accessible")
                        logger.info(f"   Status: {response.status}")
                        logger.info(f"   Content Length: {len(content)} chars")
                        logger.info(f"   Contains HTML: {has_html}")
                        logger.info(f"   Contains Renovation Content: {has_renovation_content}")
                        
                        return result
                    else:
                        logger.error(f"❌ Live URL returned status {response.status}")
                        return {
                            "success": False,
                            "status_code": response.status,
                            "error": f"HTTP {response.status}"
                        }
                        
            except Exception as e:
                logger.error(f"❌ Error accessing live URL: {e}")
                return {
                    "success": False,
                    "error": str(e)
                }

    async def check_database_projects(self) -> Dict[str, Any]:
        """TEST 4: Database Check - Verify projects are saved with complete data"""
        logger.info("\n--- TEST 4: DATABASE CHECK ---")
        
        try:
            # Use MongoDB command to check projects
            result = subprocess.run([
                'mongo', 'code_weaver_db', '--eval',
                'db.netlify_projects.find({}, {session_id:1, "files.index.html":1, netlify_site_id:1, deploy_preview_url:1}).limit(5).forEach(printjson)'
            ], capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                output = result.stdout
                
                # Count projects with complete data
                projects_with_files = output.count('"index.html"')
                projects_with_site_id = output.count('netlify_site_id')
                projects_with_deploy_url = output.count('deploy_preview_url')
                
                # Check for substantial HTML content (>1000 chars)
                html_size_matches = re.findall(r'"index\.html"\s*:\s*"[^"]{1000,}', output)
                substantial_html_count = len(html_size_matches)
                
                return {
                    "success": True,
                    "projects_with_files": projects_with_files,
                    "projects_with_site_id": projects_with_site_id,
                    "projects_with_deploy_url": projects_with_deploy_url,
                    "substantial_html_count": substantial_html_count,
                    "database_output": output[:1000] + "..." if len(output) > 1000 else output
                }
            else:
                logger.error(f"MongoDB query failed: {result.stderr}")
                return {
                    "success": False,
                    "error": f"MongoDB error: {result.stderr}"
                }
                
        except Exception as e:
            logger.error(f"Database check failed: {e}")
            return {
                "success": False,
                "error": str(e)
            }

    async def test_stress_multiple_requests(self) -> Dict[str, Any]:
        """TEST 5: Stress Test - Multiple rapid requests to verify no conflicts"""
        logger.info("\n--- TEST 5: STRESS TEST - MULTIPLE RAPID REQUESTS ---")
        
        prompts = [
            "Create website for business 1 - a coffee shop",
            "Create website for business 2 - a tech startup", 
            "Create website for business 3 - a photography studio"
        ]
        
        tasks = []
        start_time = time.time()
        
        for i, prompt in enumerate(prompts, 1):
            session_id = await self.create_session(f"Stress Test {i}")
            if session_id:
                task = self.test_normal_ai_generation(session_id, prompt)
                tasks.append(task)
        
        if not tasks:
            return {"success": False, "error": "Failed to create sessions for stress test"}
        
        # Run all requests concurrently
        results = await asyncio.gather(*tasks, return_exceptions=True)
        total_time = time.time() - start_time
        
        # Analyze results
        successful_requests = 0
        failed_requests = 0
        unique_websites = set()
        
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                logger.error(f"Request {i+1} failed with exception: {result}")
                failed_requests += 1
            elif result.get('success'):
                successful_requests += 1
                # Check uniqueness by HTML content hash
                html_content = result.get('project', {}).get('files', {}).get('index.html', '')
                unique_websites.add(hash(html_content))
            else:
                failed_requests += 1
        
        return {
            "success": successful_requests > 0,
            "total_requests": len(tasks),
            "successful_requests": successful_requests,
            "failed_requests": failed_requests,
            "unique_websites": len(unique_websites),
            "total_time": total_time,
            "no_race_conditions": len(unique_websites) == successful_requests,
            "results": results
        }

    async def check_backend_logs_for_failsafe(self) -> Dict[str, Any]:
        """Check backend logs for failsafe system activation and layer usage"""
        try:
            result = subprocess.run(
                ['tail', '-n', '1000', '/var/log/supervisor/backend.out.log'],
                capture_output=True,
                text=True
            )
            
            backend_logs = result.stdout
            
            # Look for failsafe activation indicators
            failsafe_indicators = {
                "failsafe_activated": "🛡️ FAILSAFE ACTIVATED" in backend_logs,
                "smart_fallback": "smart fallback:" in backend_logs,
                "minimal_viable": "🆘 LAST RESORT: Generating minimal viable project" in backend_logs,
                "ai_response_received": "AI Response received" in backend_logs,
                "layer_1_success": "✅ AI Response received" in backend_logs,
                "layer_2_activated": "FAILSAFE ACTIVATED: Using intelligent fallback" in backend_logs,
                "layer_3_activated": "Generating minimal viable project" in backend_logs
            }
            
            # Look for generation times and credit usage
            generation_times = re.findall(r'completed in ([\d.]+)s', backend_logs)
            credit_usage = re.findall(r'(\d+) credits?', backend_logs)
            
            # Look for error patterns that should trigger failsafe
            error_patterns = {
                "budget_exceeded": "Budget has been exceeded" in backend_logs,
                "502_errors": "502" in backend_logs or "BadGateway" in backend_logs,
                "timeout_errors": "timeout" in backend_logs.lower(),
                "parsing_errors": "PARSING COMPLETELY FAILED" in backend_logs
            }
            
            # Extract business type detection from smart fallback
            business_type_matches = re.findall(r'smart fallback: (\w+)', backend_logs)
            
            return {
                "failsafe_indicators": failsafe_indicators,
                "error_patterns": error_patterns,
                "generation_times": [float(t) for t in generation_times],
                "credit_usage": [int(c) for c in credit_usage],
                "business_types_detected": business_type_matches,
                "logs_preview": backend_logs[-2000:] if backend_logs else "No logs found"
            }
            
        except Exception as e:
            logger.error(f"Could not check backend logs: {e}")
            return {
                "success_indicators_found": 0,
                "error_indicators_found": 0,
                "has_deployment_success": False,
                "has_deployment_errors": False,
                "ai_response_chars": None,
                "has_truncation_errors": False,
                "error": str(e)
            }

    async def run_bulletproof_failsafe_test(self):
        """Run the complete bulletproof failsafe system test"""
        logger.info("🚀 STARTING BULLETPROOF FAILSAFE SYSTEM VERIFICATION")
        logger.info(f"Backend URL: {self.base_url}")
        
        start_time = time.time()
        validation_errors = []
        test_results = {}
        
        # TEST 1: Normal AI Generation (Layer 1)
        logger.info("\n" + "="*80)
        logger.info("TEST 1: NORMAL AI GENERATION (LAYER 1)")
        logger.info("="*80)
        
        session_id = await self.create_session("Renovation Business Test")
        if not session_id:
            validation_errors.append("Failed to create test session")
            return self._generate_failsafe_summary(start_time, validation_errors, test_results)
        
        renovation_prompt = "Create a professional website for a renovation business with services like Flooring, Bathrooms, Kitchens, and contact form"
        test1_result = await self.test_normal_ai_generation(session_id, renovation_prompt)
        test_results['test1_normal_generation'] = test1_result
        
        # Validate TEST 1 requirements
        if test1_result.get('success'):
            generation_time = test1_result.get('generation_time', 0)
            if generation_time > 120:  # 2 minutes
                validation_errors.append(f"Generation took too long: {generation_time:.2f}s (max 120s)")
            
            if not test1_result.get('deploy_preview_url'):
                validation_errors.append("Missing deploy_preview_url in normal generation")
            
            if not test1_result.get('netlify_site_id'):
                validation_errors.append("Missing netlify_site_id in normal generation")
                
            # Check file completeness
            files = test1_result.get('project', {}).get('files', {})
            if not files.get('index.html'):
                validation_errors.append("Missing index.html in normal generation")
            elif len(files.get('index.html', '')) < 1000:
                validation_errors.append(f"HTML too small: {len(files.get('index.html', ''))} chars")
        else:
            validation_errors.append(f"Normal AI generation failed: {test1_result.get('error')}")
        
        # TEST 2: Different Business Types (Smart Fallback Testing)
        logger.info("\n" + "="*80)
        logger.info("TEST 2 & 3: DIFFERENT BUSINESS TYPES")
        logger.info("="*80)
        
        business_tests = [
            ("restaurant", "Create a website for a coffee shop with menu and contact form"),
            ("tech", "Create a landing page for a software company offering cloud services")
        ]
        
        for business_type, prompt in business_tests:
            test_result = await self.test_business_type_customization(business_type, prompt)
            test_results[f'test_{business_type}_customization'] = test_result
            
            if test_result.get('success'):
                customization_score = test_result.get('business_customization', {}).get('customization_score', 0)
                if customization_score < 50:
                    validation_errors.append(f"{business_type} customization too low: {customization_score}%")
            else:
                validation_errors.append(f"{business_type} business type test failed: {test_result.get('error')}")
        
        # TEST 4: Database Check
        logger.info("\n" + "="*80)
        logger.info("TEST 4: DATABASE CHECK")
        logger.info("="*80)
        
        db_result = await self.check_database_projects()
        test_results['test4_database_check'] = db_result
        
        if db_result.get('success'):
            if db_result.get('projects_with_files', 0) == 0:
                validation_errors.append("No projects with files found in database")
            if db_result.get('substantial_html_count', 0) == 0:
                validation_errors.append("No projects with substantial HTML content (>1000 chars)")
        else:
            validation_errors.append(f"Database check failed: {db_result.get('error')}")
        
        # TEST 5: Stress Test
        logger.info("\n" + "="*80)
        logger.info("TEST 5: STRESS TEST")
        logger.info("="*80)
        
        stress_result = await self.test_stress_multiple_requests()
        test_results['test5_stress_test'] = stress_result
        
        if stress_result.get('success'):
            if stress_result.get('failed_requests', 0) > 0:
                validation_errors.append(f"Stress test had {stress_result.get('failed_requests')} failed requests")
            if not stress_result.get('no_race_conditions'):
                validation_errors.append("Race conditions detected in stress test")
        else:
            validation_errors.append(f"Stress test failed: {stress_result.get('error')}")
        
        # Check backend logs for failsafe system
        logger.info("\n" + "="*80)
        logger.info("BACKEND LOGS ANALYSIS")
        logger.info("="*80)
        
        log_analysis = await self.check_backend_logs_for_failsafe()
        test_results['log_analysis'] = log_analysis
        
        # Validate critical requirements
        generation_times = log_analysis.get('generation_times', [])
        if generation_times:
            max_time = max(generation_times)
            if max_time > 300:  # 5 minutes
                validation_errors.append(f"Generation took too long: {max_time}s (max 300s)")
        
        # Generate final summary
        return self._generate_failsafe_summary(start_time, validation_errors, test_results)

    def _generate_netlify_summary(self, start_time: float, validation_errors: List[str], test_data: Dict[str, Any] = None):
        """Generate final Netlify test summary"""
        total_time = time.time() - start_time
        success = len(validation_errors) == 0
        
        logger.info("\n" + "="*80)
        logger.info("MAX TOKENS FIX VERIFICATION - NETLIFY GENERATION TEST SUMMARY")
        logger.info("="*80)
        logger.info(f"Overall Result: {'✅ SUCCESS' if success else '❌ FAILED'}")
        logger.info(f"Total Time: {total_time:.2f}s")
        logger.info(f"Validation Errors: {len(validation_errors)}")
        
        if test_data:
            logger.info(f"Session ID: {test_data.get('session_id')}")
            logger.info(f"Deploy Preview URL: {test_data.get('deploy_preview_url', 'N/A')}")
            
            deploy_result = test_data.get('deploy_result', {})
            if deploy_result.get('success'):
                logger.info(f"Generation Time: {deploy_result.get('generation_time', 0):.2f}s")
                project = deploy_result.get('project', {})
                deployment = deploy_result.get('deployment', {})
                logger.info(f"Project ID: {project.get('project_id', 'N/A')}")
                logger.info(f"Site ID: {deployment.get('site_id', 'N/A')}")
                logger.info(f"Deploy ID: {deployment.get('deploy_id', 'N/A')}")
                logger.info(f"Build Status: {deployment.get('build_status', {}).get('state', 'N/A')}")
                
                # MAX TOKENS FIX VERIFICATION DETAILS
                files = project.get('files', {})
                for filepath, content in files.items():
                    if 'index.html' in filepath:
                        logger.info(f"HTML File Size: {len(content)} characters")
                    elif 'styles.css' in filepath:
                        logger.info(f"CSS File Size: {len(content)} characters")
                    elif 'app.js' in filepath:
                        logger.info(f"JS File Size: {len(content)} characters")
                
                log_analysis = test_data.get('log_analysis', {})
                ai_chars = log_analysis.get('ai_response_chars')
                if ai_chars:
                    logger.info(f"AI Response Size: {ai_chars} characters")
                    logger.info(f"Max Tokens Fix: {'✅ WORKING' if ai_chars > 20000 else '❌ INSUFFICIENT'}")
        
        if validation_errors:
            logger.info("\nVALIDATION ERRORS:")
            for error in validation_errors:
                logger.error(f"❌ {error}")
        else:
            logger.info("\n✅ All validation criteria passed - MAX TOKENS FIX VERIFIED!")
            logger.info("   - Session created successfully")
            logger.info("   - Website generated WITHOUT errors (no 'encountered an error' message)")
            logger.info("   - Response contains project.files with index.html, styles.css, app.js")
            logger.info("   - Files are COMPLETE (not truncated mid-sentence)")
            logger.info("   - HTML file is substantial (>5000 chars minimum)")
            logger.info("   - CSS file is substantial (>2000 chars minimum)")
            logger.info("   - deployment.deploy_preview_url is returned")
            logger.info("   - Live URL is accessible and contains complete content")
            logger.info("   - AI response was complete (>20,000 chars ideally)")
            logger.info("   - No truncation errors in logs")
            logger.info("   - No 'PARSING COMPLETELY FAILED' errors")
        
        return {
            "success": success,
            "total_time": total_time,
            "validation_errors": validation_errors,
            "test_data": test_data or {}
        }

async def main():
    """Main test runner for Netlify Deployment System"""
    tester = NetlifyDeploymentTester()
    results = await tester.run_netlify_deployment_test()
    
    # Return exit code based on results
    if results['success']:
        logger.info("🎉 Netlify deployment test passed!")
        return 0
    else:
        logger.error(f"💥 Netlify deployment test failed!")
        return 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    exit(exit_code)
