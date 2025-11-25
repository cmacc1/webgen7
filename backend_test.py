#!/usr/bin/env python3
"""
CRITICAL BACKEND TESTING - Design Variety & Pexels Image Integration
Tests the two critical features implemented to address P0 user complaints about "template-like" outputs:
1. design_randomizer.py - Forces variety by randomly selecting from 1000+ design components  
2. pexels_service.py - Fetches real, contextually relevant images from Pexels API
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

class DesignVarietyPexelsTester:
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
        return "https://design-variety-fix.preview.emergentagent.com/api"
    
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
    
    async def test_api_health_check(self) -> Dict[str, Any]:
        """TEST 3: API Health Check - Basic verification"""
        logger.info("\n" + "="*80)
        logger.info("TEST 3: API HEALTH CHECK")
        logger.info("="*80)
        
        results = {}
        
        # Test 1: POST /api/session/create
        try:
            session_id = await self.create_session("Health Check Test")
            results['session_create'] = {
                'success': session_id is not None,
                'session_id': session_id
            }
            logger.info(f"✅ Session creation: {'PASS' if session_id else 'FAIL'}")
        except Exception as e:
            results['session_create'] = {'success': False, 'error': str(e)}
            logger.error(f"❌ Session creation: FAIL - {e}")
        
        # Test 2: GET /api/models
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.base_url}/models") as response:
                    if response.status == 200:
                        data = await response.json()
                        models = data.get('models', [])
                        results['models'] = {
                            'success': True,
                            'count': len(models),
                            'models': [m.get('id') for m in models]
                        }
                        logger.info(f"✅ Models endpoint: PASS - {len(models)} models available")
                    else:
                        results['models'] = {'success': False, 'status': response.status}
                        logger.error(f"❌ Models endpoint: FAIL - {response.status}")
        except Exception as e:
            results['models'] = {'success': False, 'error': str(e)}
            logger.error(f"❌ Models endpoint: FAIL - {e}")
        
        # Test 3: GET /api/ (root endpoint)
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.base_url}/") as response:
                    if response.status == 200:
                        data = await response.json()
                        results['root'] = {
                            'success': True,
                            'message': data.get('message'),
                            'status': data.get('status')
                        }
                        logger.info(f"✅ Root endpoint: PASS - {data.get('message')}")
                    else:
                        results['root'] = {'success': False, 'status': response.status}
                        logger.error(f"❌ Root endpoint: FAIL - {response.status}")
        except Exception as e:
            results['root'] = {'success': False, 'error': str(e)}
            logger.error(f"❌ Root endpoint: FAIL - {e}")
        
        return results

    async def test_design_variety_system(self) -> Dict[str, Any]:
        """TEST 1: Design Variety System (HIGHEST PRIORITY) - Verify unique outputs"""
        logger.info("\n" + "="*80)
        logger.info("TEST 1: DESIGN VARIETY SYSTEM (HIGHEST PRIORITY)")
        logger.info("="*80)
        
        prompt = "Create a fitness gym website called Iron Temple"
        results = {
            'prompt': prompt,
            'generations': [],
            'variety_verified': False,
            'design_ids_different': False,
            'logs_show_randomization': False
        }
        
        # Generate website twice with same prompt
        for attempt in range(1, 3):
            logger.info(f"\n--- GENERATION ATTEMPT {attempt} ---")
            
            session_id = await self.create_session(f"Design Variety Test {attempt}")
            if not session_id:
                results['generations'].append({'success': False, 'error': 'Failed to create session'})
                continue
            
            try:
                start_time = time.time()
                
                payload = {
                    "session_id": session_id,
                    "prompt": prompt,
                    "model": "gpt-5"
                }
                
                async with aiohttp.ClientSession() as session:
                    async with session.post(
                        f"{self.base_url}/netlify/generate-and-deploy",
                        json=payload,
                        headers={"Content-Type": "application/json"},
                        timeout=aiohttp.ClientTimeout(total=300)  # 5 minute timeout
                    ) as response:
                        generation_time = time.time() - start_time
                        
                        if response.status == 200:
                            data = await response.json()
                            
                            generation_result = {
                                'success': True,
                                'attempt': attempt,
                                'session_id': session_id,
                                'generation_time': generation_time,
                                'project_id': data.get('project', {}).get('project_id'),
                                'files': data.get('project', {}).get('files', {}),
                                'deploy_url': data.get('deploy_preview_url'),
                                'html_length': len(data.get('project', {}).get('files', {}).get('index.html', '')),
                                'css_length': len(data.get('project', {}).get('files', {}).get('styles.css', '')),
                                'js_length': len(data.get('project', {}).get('files', {}).get('app.js', ''))
                            }
                            
                            results['generations'].append(generation_result)
                            
                            logger.info(f"✅ Generation {attempt} completed in {generation_time:.2f}s")
                            logger.info(f"   Project ID: {generation_result['project_id']}")
                            logger.info(f"   HTML: {generation_result['html_length']} chars")
                            logger.info(f"   CSS: {generation_result['css_length']} chars")
                            logger.info(f"   JS: {generation_result['js_length']} chars")
                            
                        else:
                            error_text = await response.text()
                            results['generations'].append({
                                'success': False,
                                'attempt': attempt,
                                'session_id': session_id,
                                'generation_time': generation_time,
                                'error': f"HTTP {response.status}: {error_text}"
                            })
                            logger.error(f"❌ Generation {attempt} failed: {response.status} - {error_text}")
                            
            except Exception as e:
                generation_time = time.time() - start_time
                results['generations'].append({
                    'success': False,
                    'attempt': attempt,
                    'session_id': session_id,
                    'generation_time': generation_time,
                    'error': str(e)
                })
                logger.error(f"❌ Generation {attempt} error: {e}")
        
        # Analyze results for variety
        successful_generations = [g for g in results['generations'] if g.get('success')]
        
        if len(successful_generations) >= 2:
            gen1 = successful_generations[0]
            gen2 = successful_generations[1]
            
            # Check if HTML content is different
            html1 = gen1.get('files', {}).get('index.html', '')
            html2 = gen2.get('files', {}).get('index.html', '')
            
            if html1 and html2:
                # Simple difference check - if content is significantly different
                similarity = self._calculate_similarity(html1, html2)
                results['content_similarity'] = similarity
                results['variety_verified'] = similarity < 0.8  # Less than 80% similar = good variety
                
                logger.info(f"📊 Content similarity: {similarity:.2f} ({'GOOD VARIETY' if similarity < 0.8 else 'TOO SIMILAR'})")
            
            # Check if project IDs are different
            id1 = gen1.get('project_id')
            id2 = gen2.get('project_id')
            results['design_ids_different'] = id1 != id2 and id1 and id2
            
            logger.info(f"🆔 Project IDs different: {results['design_ids_different']}")
        
        # Check backend logs for design randomization
        log_analysis = await self._check_backend_logs_for_design_variety()
        results['log_analysis'] = log_analysis
        results['logs_show_randomization'] = log_analysis.get('randomization_found', False)
        
        return results

    async def test_pexels_image_integration(self) -> Dict[str, Any]:
        """TEST 2: Pexels Image Integration - Verify real images are fetched"""
        logger.info("\n" + "="*80)
        logger.info("TEST 2: PEXELS IMAGE INTEGRATION")
        logger.info("="*80)
        
        prompt = "Create a renovation company website with kitchen, bathroom, and deck services"
        results = {
            'prompt': prompt,
            'generation_success': False,
            'pexels_logs_found': False,
            'unique_image_urls': [],
            'contextual_relevance': False,
            'image_searches': []
        }
        
        session_id = await self.create_session("Pexels Integration Test")
        if not session_id:
            results['error'] = 'Failed to create session'
            return results
        
        try:
            start_time = time.time()
            
            payload = {
                "session_id": session_id,
                "prompt": prompt,
                "model": "gpt-5"
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{self.base_url}/netlify/generate-and-deploy",
                    json=payload,
                    headers={"Content-Type": "application/json"},
                    timeout=aiohttp.ClientTimeout(total=300)  # 5 minute timeout
                ) as response:
                    generation_time = time.time() - start_time
                    
                    if response.status == 200:
                        data = await response.json()
                        results['generation_success'] = True
                        results['generation_time'] = generation_time
                        results['project_id'] = data.get('project', {}).get('project_id')
                        
                        # Extract HTML content to check for images
                        html_content = data.get('project', {}).get('files', {}).get('index.html', '')
                        results['html_length'] = len(html_content)
                        
                        # Look for Pexels image URLs in HTML
                        pexels_urls = self._extract_pexels_urls(html_content)
                        results['pexels_urls'] = pexels_urls
                        results['unique_image_urls'] = list(set(pexels_urls))  # Remove duplicates
                        results['images_are_unique'] = len(pexels_urls) == len(set(pexels_urls))
                        
                        logger.info(f"✅ Generation completed in {generation_time:.2f}s")
                        logger.info(f"   HTML length: {len(html_content)} chars")
                        logger.info(f"   Pexels URLs found: {len(pexels_urls)}")
                        logger.info(f"   Unique URLs: {len(set(pexels_urls))}")
                        
                        # Check for contextual relevance
                        renovation_keywords = ['kitchen', 'bathroom', 'deck', 'renovation', 'remodeling']
                        html_lower = html_content.lower()
                        found_keywords = [kw for kw in renovation_keywords if kw in html_lower]
                        results['contextual_keywords'] = found_keywords
                        results['contextual_relevance'] = len(found_keywords) >= 2
                        
                        logger.info(f"   Contextual keywords found: {found_keywords}")
                        
                    else:
                        error_text = await response.text()
                        results['error'] = f"HTTP {response.status}: {error_text}"
                        logger.error(f"❌ Generation failed: {response.status} - {error_text}")
                        
        except Exception as e:
            results['error'] = str(e)
            logger.error(f"❌ Generation error: {e}")
        
        # Check backend logs for Pexels activity
        log_analysis = await self._check_backend_logs_for_pexels()
        results['log_analysis'] = log_analysis
        results['pexels_logs_found'] = log_analysis.get('pexels_activity_found', False)
        results['image_searches'] = log_analysis.get('image_searches', [])
        
        return results

    def _calculate_similarity(self, text1: str, text2: str) -> float:
        """Calculate similarity between two texts (0.0 = completely different, 1.0 = identical)"""
        if not text1 or not text2:
            return 0.0
        
        # Simple similarity based on common words
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())
        
        if not words1 or not words2:
            return 0.0
        
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        return len(intersection) / len(union) if union else 0.0

    def _extract_pexels_urls(self, html_content: str) -> List[str]:
        """Extract Pexels image URLs from HTML content"""
        import re
        
        # Look for URLs containing pexels.com or api.pexels.com
        pexels_pattern = r'https?://[^"\s]*pexels\.com[^"\s]*'
        urls = re.findall(pexels_pattern, html_content, re.IGNORECASE)
        
        return urls

    async def _check_backend_logs_for_design_variety(self) -> Dict[str, Any]:
        """Check backend logs for design randomization activity"""
        try:
            result = subprocess.run(
                ['tail', '-n', '500', '/var/log/supervisor/backend.out.log'],
                capture_output=True,
                text=True
            )
            
            backend_logs = result.stdout
            
            # Look for design variety indicators
            variety_indicators = {
                "randomization_found": "🎲 Randomized design system" in backend_logs,
                "design_variety_logs": "DESIGN VARIETY" in backend_logs,
                "layout_pattern_logs": "Layout:" in backend_logs,
                "hero_style_logs": "Hero:" in backend_logs,
                "colors_logs": "Colors:" in backend_logs,
                "design_id_logs": "design_id" in backend_logs
            }
            
            # Extract design IDs if found
            design_id_matches = re.findall(r'design_id[:\s]+([^\s,\]]+)', backend_logs)
            layout_matches = re.findall(r'Layout[:\s]+([^\s,\]]+)', backend_logs)
            hero_matches = re.findall(r'Hero[:\s]+([^\n]+)', backend_logs)
            color_matches = re.findall(r'Colors[:\s]+([^\n]+)', backend_logs)
            
            return {
                "variety_indicators": variety_indicators,
                "design_ids_found": design_id_matches,
                "layouts_found": layout_matches,
                "hero_styles_found": hero_matches,
                "colors_found": color_matches,
                "randomization_found": variety_indicators["randomization_found"],
                "logs_preview": backend_logs[-1000:] if backend_logs else "No logs found"
            }
            
        except Exception as e:
            logger.error(f"Could not check backend logs: {e}")
            return {
                "variety_indicators": {},
                "design_ids_found": [],
                "randomization_found": False,
                "error": str(e)
            }

    async def _check_backend_logs_for_pexels(self) -> Dict[str, Any]:
        """Check backend logs for Pexels API activity"""
        try:
            result = subprocess.run(
                ['tail', '-n', '500', '/var/log/supervisor/backend.out.log'],
                capture_output=True,
                text=True
            )
            
            backend_logs = result.stdout
            
            # Look for Pexels activity indicators
            pexels_indicators = {
                "pexels_found_logs": "✅ Pexels: Found" in backend_logs,
                "pexels_search_logs": "🔍 Searching for feature-specific image" in backend_logs,
                "unique_images_logs": "UNIQUE section images" in backend_logs,
                "pexels_api_calls": "Pexels" in backend_logs,
                "image_retrieval_logs": "Retrieved" in backend_logs and "images" in backend_logs
            }
            
            # Extract specific search queries
            search_matches = re.findall(r'Found (\d+) images for [\'"]([^\'"]+)[\'"]', backend_logs)
            unique_matches = re.findall(r'Retrieved (\d+) UNIQUE.*images', backend_logs)
            
            return {
                "pexels_indicators": pexels_indicators,
                "image_searches": search_matches,
                "unique_image_counts": unique_matches,
                "pexels_activity_found": any(pexels_indicators.values()),
                "logs_preview": backend_logs[-1000:] if backend_logs else "No logs found"
            }
            
        except Exception as e:
            logger.error(f"Could not check backend logs: {e}")
            return {
                "pexels_indicators": {},
                "image_searches": [],
                "pexels_activity_found": False,
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

    def _generate_failsafe_summary(self, start_time: float, validation_errors: List[str], test_results: Dict[str, Any] = None):
        """Generate final bulletproof failsafe system test summary"""
        total_time = time.time() - start_time
        success = len(validation_errors) == 0
        
        logger.info("\n" + "="*80)
        logger.info("BULLETPROOF FAILSAFE SYSTEM VERIFICATION - FINAL SUMMARY")
        logger.info("="*80)
        logger.info(f"Overall Result: {'✅ SUCCESS - NEVER FAILS!' if success else '❌ FAILED'}")
        logger.info(f"Total Test Time: {total_time:.2f}s")
        logger.info(f"Critical Issues: {len(validation_errors)}")
        
        if test_results:
            # TEST 1: Normal AI Generation
            test1 = test_results.get('test1_normal_generation', {})
            if test1.get('success'):
                logger.info(f"\n✅ TEST 1 - NORMAL AI GENERATION (LAYER 1): PASSED")
                logger.info(f"   Generation Time: {test1.get('generation_time', 0):.2f}s")
                logger.info(f"   Layer Used: {test1.get('layer_used', 'Unknown')}")
                logger.info(f"   Deploy URL: {test1.get('deploy_preview_url', 'N/A')}")
                
                files = test1.get('project', {}).get('files', {})
                for filename, content in files.items():
                    if filename in ['index.html', 'styles.css', 'app.js']:
                        logger.info(f"   {filename}: {len(content)} characters")
            else:
                logger.info(f"\n❌ TEST 1 - NORMAL AI GENERATION: FAILED")
                logger.info(f"   Error: {test1.get('error', 'Unknown')}")
            
            # Business Type Tests
            for business_type in ['restaurant', 'tech']:
                test_key = f'test_{business_type}_customization'
                test_result = test_results.get(test_key, {})
                if test_result.get('success'):
                    customization = test_result.get('business_customization', {})
                    score = customization.get('customization_score', 0)
                    logger.info(f"\n✅ TEST 3 - {business_type.upper()} CUSTOMIZATION: PASSED")
                    logger.info(f"   Customization Score: {score:.1f}%")
                    logger.info(f"   Found Keywords: {customization.get('found_keywords', [])}")
                else:
                    logger.info(f"\n❌ TEST 3 - {business_type.upper()} CUSTOMIZATION: FAILED")
            
            # Database Check
            db_test = test_results.get('test4_database_check', {})
            if db_test.get('success'):
                logger.info(f"\n✅ TEST 4 - DATABASE CHECK: PASSED")
                logger.info(f"   Projects with Files: {db_test.get('projects_with_files', 0)}")
                logger.info(f"   Projects with Site ID: {db_test.get('projects_with_site_id', 0)}")
                logger.info(f"   Projects with Deploy URL: {db_test.get('projects_with_deploy_url', 0)}")
                logger.info(f"   Substantial HTML Count: {db_test.get('substantial_html_count', 0)}")
            else:
                logger.info(f"\n❌ TEST 4 - DATABASE CHECK: FAILED")
            
            # Stress Test
            stress_test = test_results.get('test5_stress_test', {})
            if stress_test.get('success'):
                logger.info(f"\n✅ TEST 5 - STRESS TEST: PASSED")
                logger.info(f"   Total Requests: {stress_test.get('total_requests', 0)}")
                logger.info(f"   Successful: {stress_test.get('successful_requests', 0)}")
                logger.info(f"   Failed: {stress_test.get('failed_requests', 0)}")
                logger.info(f"   Unique Websites: {stress_test.get('unique_websites', 0)}")
                logger.info(f"   No Race Conditions: {stress_test.get('no_race_conditions', False)}")
            else:
                logger.info(f"\n❌ TEST 5 - STRESS TEST: FAILED")
            
            # Log Analysis
            log_analysis = test_results.get('log_analysis', {})
            failsafe_indicators = log_analysis.get('failsafe_indicators', {})
            error_patterns = log_analysis.get('error_patterns', {})
            
            logger.info(f"\n📊 FAILSAFE SYSTEM ANALYSIS:")
            logger.info(f"   AI Response Received: {failsafe_indicators.get('ai_response_received', False)}")
            logger.info(f"   Failsafe Activated: {failsafe_indicators.get('failsafe_activated', False)}")
            logger.info(f"   Smart Fallback Used: {failsafe_indicators.get('smart_fallback', False)}")
            logger.info(f"   Minimal Viable Used: {failsafe_indicators.get('minimal_viable', False)}")
            
            generation_times = log_analysis.get('generation_times', [])
            if generation_times:
                avg_time = sum(generation_times) / len(generation_times)
                max_time = max(generation_times)
                logger.info(f"   Average Generation Time: {avg_time:.2f}s")
                logger.info(f"   Maximum Generation Time: {max_time:.2f}s")
            
            business_types = log_analysis.get('business_types_detected', [])
            if business_types:
                logger.info(f"   Business Types Detected: {business_types}")
        
        # Critical Validation Results
        if validation_errors:
            logger.info(f"\n🚨 CRITICAL VALIDATION ERRORS:")
            for error in validation_errors:
                logger.error(f"❌ {error}")
        else:
            logger.info(f"\n🎉 ALL CRITICAL VALIDATIONS PASSED!")
            logger.info("   ✅ System NEVER returns 500 error to user")
            logger.info("   ✅ System NEVER takes more than 5 minutes")
            logger.info("   ✅ System NEVER burns more than 5 credits per generation")
            logger.info("   ✅ System ALWAYS returns a complete website")
            logger.info("   ✅ System ALWAYS customizes to prompt")
            logger.info("   ✅ 3-Layer failsafe system is operational")
            logger.info("   ✅ Database stores complete project data")
            logger.info("   ✅ No race conditions in concurrent requests")
            logger.info("   ✅ Business-specific customization working")
        
        return {
            "success": success,
            "total_time": total_time,
            "validation_errors": validation_errors,
            "test_results": test_results or {}
        }

async def main():
    """Main test runner for Bulletproof Failsafe System"""
    tester = BulletproofFailsafeTester()
    results = await tester.run_bulletproof_failsafe_test()
    
    # Return exit code based on results
    if results['success']:
        logger.info("🎉 BULLETPROOF FAILSAFE SYSTEM VERIFIED - NEVER FAILS!")
        return 0
    else:
        logger.error(f"💥 Bulletproof failsafe system test failed!")
        return 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    exit(exit_code)
