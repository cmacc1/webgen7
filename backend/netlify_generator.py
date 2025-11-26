"""
Netlify Code Generation Service
Generates deployment-ready, serverless code for Netlify platform
"""
import os
import logging
import json
import re
import asyncio
from typing import Dict, Any, List, Optional
from emergentintegrations.llm.chat import LlmChat, UserMessage
from fastapi import HTTPException
from design_knowledge_base import (
    FRAMEWORKS, 
    DESIGN_PRINCIPLES, 
    COMPONENT_PATTERNS, 
    ANIMATION_PATTERNS,
    WEBSITE_PATTERNS
)

logger = logging.getLogger(__name__)

class NetlifyGenerator:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self._last_health_check = None
        self._health_check_interval = 60  # seconds
        self._service_healthy = True
        self._last_request_time = 0
        self._min_request_interval = 1.0  # Minimum 1 second between requests
        self._request_semaphore = asyncio.Semaphore(3)  # Max 3 concurrent requests
    
    async def _check_api_health(self, provider: str, model: str) -> bool:
        """
        Quick health check before expensive operations
        Returns True if API is responsive, False otherwise
        """
        import time
        
        # Skip if recently checked
        if self._last_health_check and (time.time() - self._last_health_check) < self._health_check_interval:
            return self._service_healthy
        
        try:
            logger.info("🏥 Performing API health check...")
            chat = LlmChat(
                api_key=self.api_key,
                session_id="health-check",
                system_message="You are a helpful assistant."
            )
            chat.with_model(provider, model)
            
            # Simple test request with timeout
            response = await asyncio.wait_for(
                chat.send_message(UserMessage(text="respond with ok")),
                timeout=10.0
            )
            
            self._service_healthy = len(response) > 0
            self._last_health_check = time.time()
            
            if self._service_healthy:
                logger.info("✅ API health check passed")
            else:
                logger.warning("⚠️ API health check returned empty response")
                
            return self._service_healthy
            
        except Exception as e:
            logger.warning(f"⚠️ API health check failed: {str(e)[:100]}")
            self._service_healthy = False
            self._last_health_check = time.time()
            return False
    
    def _get_model_config(self, model: str) -> tuple:
        """Map model ID to provider and model name"""
        model_map = {
            "claude-sonnet-4": ("anthropic", "claude-sonnet-4"),
            "gpt-5": ("openai", "gpt-5"),  
            "gpt-5-mini": ("openai", "gpt-5-mini"),
            "gpt-4o": ("openai", "gpt-4o"),
            "gpt-4o-mini": ("openai", "gpt-4o-mini"),
            "gpt-3.5-turbo": ("openai", "gpt-3.5-turbo"),
            "gemini-2.5-pro": ("google", "gemini-2.5-pro")
        }
        return model_map.get(model, ("openai", "gpt-4o"))  # Default to gpt-4o
    
    async def generate_netlify_project(self, prompt: str, model: str = "gpt-5", current_project: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Generate a complete Netlify-compatible project
        
        Returns:
            Dict with structure:
            {
                "files": {
                    "index.html": "content",
                    "netlify.toml": "content",
                    "netlify/functions/api.js": "content",
                    ...
                },
                "deploy_config": {
                    "build_command": "npm run build",
                    "publish_dir": "dist",
                    "functions_dir": "netlify/functions"
                }
            }
        """
        provider, model_name = self._get_model_config(model)
        session_id = f"netlify_{os.urandom(8).hex()}"
        
        logger.info("🚀 NETLIFY PROJECT GENERATION")
        logger.info(f"   Model: {provider}/{model_name}")
        logger.info(f"   Prompt: {prompt}")
        
        # Determine if this is editing or new generation
        is_editing = current_project is not None and len(current_project.get("files", {})) > 0
        
        if is_editing:
            logger.info("📝 EDIT MODE: Modifying existing Netlify project")
            return await self._edit_netlify_project(prompt, current_project, provider, model_name, session_id)
        else:
            logger.info("🆕 NEW PROJECT: Creating from scratch")
            return await self._create_netlify_project(prompt, provider, model_name, session_id)
    
    async def _create_netlify_project(self, prompt: str, provider: str, model: str, session_id: str) -> Dict[str, Any]:
        """Create a new Netlify project from scratch"""
        
        # REMOVED: Health check and analysis to save credits and time
        # These extra API calls were burning credits unnecessarily
        logger.info("⚡ AI GENERATION: Creating custom website with design quality")
        
        # MEGA DESIGN LIBRARY INTEGRATION - DETECT TYPE FIRST
        from advanced_design_library import COLOR_SCHEMES, BUTTON_STYLES, BACKGROUND_PATTERNS
        from website_type_detector import WebsiteTypeDetector
        from mega_design_library import WEBSITE_TYPES, NAVIGATION_DESIGNS
        from image_provider import ImageProvider
        import random
        
        # Detect website type using comprehensive system (100+ types)
        from website_types_comprehensive import detect_website_type, get_templates_for_type
        from template_definitions import get_template_definition, select_best_template
        from website_type_detector import WebsiteTypeDetector
        
        # Use new comprehensive detection
        website_type = detect_website_type(prompt)
        available_templates = get_templates_for_type(website_type)
        best_template = select_best_template(website_type, prompt, available_templates)
        template_def = get_template_definition(best_template)
        
        # Get business details from old detector
        detector = WebsiteTypeDetector()
        business_details = detector.extract_business_details(prompt)
        
        logger.info(f"🎯 Website Type: {website_type}")
        logger.info(f"📋 Business: {business_details.get('name', 'N/A')}")
        logger.info(f"🎨 Template: {template_def['name']}")
        logger.info(f"📐 Layout: {template_def['layout'][:60]}...")
        
        # Get HERO IMAGE ONLY from Pexels (not cluttered with images everywhere)
        from pexels_service import PexelsImageService
        from icon_library import get_icon_for_feature, get_multiple_icons, CATEGORY_ICONS
        image_provider = ImageProvider()
        pexels = PexelsImageService()
        
        # BUSINESS-SPECIFIC HIGH-QUALITY IMAGE - Ultra-relevant to business type
        from multi_image_service import MultiImageService
        from business_image_mapper import get_hero_image_query, get_alternative_queries
        
        try:
            # Get highly specific image query for this business type
            specific_query = get_hero_image_query(website_type, prompt)
            
            logger.info(f"🔍 BUSINESS-SPECIFIC image search: '{specific_query}'")
            logger.info(f"   Business type: {website_type}")
            
            # Use multi-source service (tries Unsplash, Pixabay, Pexels in order)
            multi_image = MultiImageService()
            hero_image_data = await multi_image.search_with_fallback(specific_query, orientation="landscape")
            
            if hero_image_data:
                hero_image = hero_image_data["url"]
                hero_photographer = hero_image_data.get("photographer", "Unknown")
                hero_source = hero_image_data.get("source", "unknown")
                logger.info(f"✅ Hero image from {hero_source.upper()}: {hero_image[:60]}...")
                logger.info(f"   Query used: {specific_query}")
                logger.info(f"   Photographer: {hero_photographer}")
            else:
                # Try alternative queries
                alternatives = get_alternative_queries(website_type)
                logger.info(f"⚠️ Primary query failed, trying {len(alternatives)} alternatives...")
                
                for alt_query in alternatives:
                    hero_image_data = await multi_image.search_with_fallback(alt_query, orientation="landscape")
                    if hero_image_data:
                        hero_image = hero_image_data["url"]
                        hero_photographer = hero_image_data.get("photographer", "Unknown")
                        hero_source = hero_image_data.get("source", "unknown")
                        logger.info(f"✅ Found with alternative: '{alt_query}'")
                        break
                
                if not hero_image_data:
                    hero_image = None
                    hero_photographer = None
                    hero_source = None
                    logger.warning(f"❌ No images found after trying all queries")
                
        except Exception as e:
            logger.error(f"❌ Image search failed: {str(e)}")
            hero_image = None
            hero_photographer = None
            hero_source = None
        
        # No section images or gallery - use ICONS instead
        section_images = []
        gallery_images = []
        
        # Get gradient backgrounds as fallback/complement
        hero_bg = image_provider.get_hero_background(website_type)
        section_bgs = image_provider.get_section_backgrounds(website_type, count=4)
        
        logger.info(f"🎨 Fallback gradients ready:")
        logger.info(f"   Hero gradient: {hero_bg['gradient']}")
        logger.info(f"   Hero icon: {hero_bg['icon']}")
        
        # Use the selected template definition
        logger.info(f"✅ Using template: {template_def['name']}")
        logger.info(f"   Best for: {template_def['best_for']}")
        logger.info(f"   Features: {', '.join(template_def['features'][:3])}...")
        
        # Get design randomization for additional variety
        from design_randomizer import DesignRandomizer
        randomizer = DesignRandomizer()
        design_system = randomizer.get_random_design_system()
        
        # Use randomized colors
        colors = design_system['colors']
        
        # Build image URLs for prompt
        hero_gradient = hero_bg.get('gradient', 'linear-gradient(135deg, #667eea, #764ba2)')
        if hero_image:
            hero_img_html = f'<img src="{hero_image}" alt="Hero" class="absolute inset-0 w-full h-full object-cover">'
        else:
            hero_img_html = f'<div class="absolute inset-0" style="background: {hero_gradient};"></div>'
        
        if section_images:
            section_imgs_list = [f'<img src="{img}" alt="Section" class="w-full h-96 object-cover rounded-2xl">' for img in section_images[:4]]
            section_imgs_html = ', '.join(section_imgs_list)
        else:
            section_imgs_html = 'Use gradient backgrounds'
        
        # Get appropriate navigation design
        from navigation_library import get_navigation_by_template
        nav_design = get_navigation_by_template(template_def['name'])
        
        logger.info(f"🧭 Navigation: {nav_design['name']}")
        
        system_prompt = f"""🚨 CRITICAL: DO NOT CREATE A BASIC WHITE WEBSITE! 🚨

You MUST create a STUNNING, COLORFUL, MODERN website with RICH VISUALS.

BUSINESS: {website_type.replace('_', ' ').title()} - {business_details.get('name', 'Professional Business')}

🚨 MANDATORY DESIGN RULES - NO EXCEPTIONS:

1️⃣ HERO SECTION (MUST BE FULL-SCREEN WITH IMAGE/GRADIENT):
EXAMPLE - USE THIS STRUCTURE:
```html
<section class="relative min-h-screen flex items-center justify-center" style="background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('{hero_image if hero_image else ''}'); background-size: cover; background-position: center; background-attachment: fixed;">
    <div class="absolute inset-0 bg-gradient-to-br from-blue-900/80 to-purple-900/80"></div>
    <div class="relative z-10 text-center px-6 max-w-5xl mx-auto text-white">
        <i class="fas fa-star text-8xl mb-6 animate-pulse"></i>
        <h1 class="text-6xl md:text-8xl font-black mb-6 leading-tight">YOUR HEADLINE HERE</h1>
        <p class="text-2xl md:text-3xl mb-12 opacity-90">Subtitle goes here</p>
        <div class="flex gap-6 justify-center flex-wrap">
            <button onclick="document.getElementById('contact').scrollIntoView({{behavior:'smooth'}})" class="px-12 py-5 bg-gradient-to-r from-blue-500 to-purple-600 text-white rounded-full font-bold text-xl hover:scale-110 hover:shadow-2xl transition-all">Get Started</button>
            <button onclick="document.getElementById('about').scrollIntoView({{behavior:'smooth'}})" class="px-12 py-5 bg-white text-gray-900 rounded-full font-bold text-xl hover:scale-110 hover:shadow-2xl transition-all">Learn More</button>
        </div>
    </div>
</section>
```

2️⃣ NAVIGATION (USE THIS CODE):
{nav_design['html']}

3️⃣ FEATURES/SERVICES SECTION (COLORFUL CARDS):
EXAMPLE - USE THIS STRUCTURE:
```html
<section class="py-24 bg-gradient-to-br from-gray-50 to-blue-50">
    <div class="max-w-7xl mx-auto px-6">
        <h2 class="text-5xl md:text-6xl font-black text-center mb-6 bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">Our Services</h2>
        <p class="text-xl text-gray-600 text-center mb-16 max-w-2xl mx-auto">Everything you need to succeed</p>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div class="group bg-white rounded-2xl p-8 shadow-xl hover:shadow-2xl hover:-translate-y-2 transition-all duration-300">
                <div class="w-20 h-20 bg-gradient-to-br from-blue-500 to-purple-600 rounded-xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
                    <i class="fas fa-star fa-3x text-white"></i>
                </div>
                <h3 class="text-2xl font-bold mb-4 text-gray-800">Service Name</h3>
                <p class="text-gray-600 leading-relaxed">Description of your amazing service goes here with details.</p>
            </div>
            <!-- REPEAT FOR EACH SERVICE -->
        </div>
    </div>
</section>
```

4️⃣ ABOUT SECTION (WITH GRADIENT BACKGROUND):
EXAMPLE:
```html
<section class="py-24 bg-gradient-to-br from-purple-900 to-indigo-900 text-white">
    <div class="max-w-7xl mx-auto px-6">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div>
                <h2 class="text-5xl md:text-6xl font-black mb-6">About Us</h2>
                <p class="text-xl leading-relaxed mb-6 opacity-90">Your compelling story goes here...</p>
                <button class="px-8 py-4 bg-white text-purple-900 rounded-xl font-bold hover:scale-105 hover:shadow-2xl transition-all">Learn More</button>
            </div>
            <div class="relative h-96 rounded-3xl overflow-hidden shadow-2xl">
                <div class="absolute inset-0 bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center">
                    <i class="fas fa-building text-9xl text-white opacity-30"></i>
                </div>
            </div>
        </div>
    </div>
</section>
```

5️⃣ CONTACT SECTION (COLORFUL FORM):
EXAMPLE:
```html
<section id="contact" class="py-24 bg-gradient-to-br from-blue-50 to-purple-50">
    <div class="max-w-4xl mx-auto px-6">
        <h2 class="text-5xl md:text-6xl font-black text-center mb-6 bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">Get In Touch</h2>
        <form onsubmit="handleFormSubmit(event)" class="bg-white rounded-2xl shadow-2xl p-8 md:p-12">
            <div class="mb-6">
                <input type="text" placeholder="Your Name" required class="w-full px-6 py-4 border-2 border-gray-200 rounded-xl focus:border-blue-500 focus:outline-none transition-colors text-lg">
            </div>
            <div class="mb-6">
                <input type="email" placeholder="Your Email" required class="w-full px-6 py-4 border-2 border-gray-200 rounded-xl focus:border-blue-500 focus:outline-none transition-colors text-lg">
            </div>
            <div class="mb-6">
                <textarea placeholder="Your Message" required rows="5" class="w-full px-6 py-4 border-2 border-gray-200 rounded-xl focus:border-blue-500 focus:outline-none transition-colors text-lg"></textarea>
            </div>
            <button type="submit" class="w-full px-12 py-5 bg-gradient-to-r from-blue-500 to-purple-600 text-white rounded-xl font-bold text-xl hover:scale-105 hover:shadow-2xl transition-all">Send Message</button>
        </form>
    </div>
</section>
```

6️⃣ COLORS TO USE:
- Primary: {colors['primary']}
- Secondary: {colors['secondary']}
- Accent: {colors['accent']}
- Use gradients: from-blue-500 to-purple-600, from-purple-900 to-indigo-900
- Background sections: bg-gray-50, bg-blue-50, bg-purple-50, bg-gradient-to-br

7️⃣ MANDATORY VISUAL ELEMENTS:
✅ Gradients on EVERY section (bg-gradient-to-br)
✅ Shadows on cards (shadow-xl, shadow-2xl)
✅ Hover effects (hover:-translate-y-2, hover:scale-110)
✅ Icons with gradient backgrounds
✅ Large, bold typography (text-5xl, text-6xl, font-black)
✅ Rounded corners (rounded-xl, rounded-2xl)
✅ Colorful buttons (gradient backgrounds)

🚨 WHAT NOT TO DO:
❌ NO plain white background for entire site
❌ NO basic black text on white
❌ NO minimal design
❌ NO text just going down the page
❌ NO boring layout

CRITICAL CDN REQUIREMENTS (MUST INCLUDE ALL):
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link href="styles.css" rel="stylesheet">
<script src="app.js"></script>

COMPREHENSIVE UI COMPONENT LIBRARY (1000+ Components Available):
✅ NAVIGATION: Sticky headers, mega menus, breadcrumbs, mobile hamburger menus
✅ FORMS: Inline validation, input masks, date pickers, toggle switches, field grouping
✅ DISPLAY: Modals (with ESC close), toast notifications, tooltips, progress bars, skeleton loaders
✅ LAYOUTS: Accordions/collapsible sections, cards with hover effects, pagination
✅ ANIMATIONS: Scroll reveal (fade-in-up, fade-in-left, scale-in), parallax, smooth scroll
✅ ACCESSIBILITY: ARIA labels, keyboard navigation, high contrast support

DESIGN STANDARDS (ULTRA-MODERN):
✨ USE TAILWIND EXTENSIVELY - Every element needs Tailwind classes
🖼️ REAL IMAGES: Use provided Pexels URLs in hero background and sections
🎨 Hero: min-h-screen relative with real image {'<img src="'+hero_image+'">' if hero_image else 'gradient background'}
🎭 Large Icons: <i class="fas {hero_bg['icon']} text-8xl md:text-9xl text-white mb-6"></i>
📐 Sections: py-20 md:py-24 max-w-7xl mx-auto px-6
🎯 Cards: bg-white shadow-2xl rounded-3xl p-8 md:p-12 hover:-translate-y-2 transition-all duration-300
🔤 Typography: text-6xl md:text-7xl lg:text-9xl font-black for headlines
💫 Effects: hover:scale-105 hover:shadow-2xl transition-all duration-300
📱 Grids: grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8
🌈 Gradients: bg-gradient-to-br from-purple-600 to-pink-600

SECTIONS REQUIRED (3-4 minimum with REAL IMAGES):
1. HERO - Full screen with REAL IMAGE background: {hero_img_html}
   Plus overlay for text readability, huge icon, headline, 2 CTA buttons
2. FEATURES/SERVICES - Grid of 3-4 cards, optionally with REAL images from: {', '.join(section_images[:2]) if section_images else 'gradients'}
3. ABOUT - Text + REAL IMAGE or gradient card with decorative icon
4. GALLERY (optional) - Grid showcase using provided Pexels images
5. CONTACT - Form with inline validation, input masks, gradient submit button

CRITICAL CSS FILE (500+ lines):
- @keyframes fadeInUp, slideIn, scaleIn, glowPulse
- .fade-in-up, .fade-in-left, .fade-in-right, .scale-in animation classes
- .hover-lift, .hover-glow, .hover-scale hover effects
- Custom accordion, modal, toast notification styles
- Responsive breakpoints (@media queries)
- Smooth transitions on all interactive elements

CRITICAL JS FILE (MUST INCLUDE ALL THESE FUNCTIONS):
```javascript
// Smooth scroll for all anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
    anchor.addEventListener('click', function (e) {{
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) target.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
    }});
}});

// Mobile menu toggle
function toggleMobileMenu() {{
    const menu = document.getElementById('mobile-menu');
    if (menu) menu.classList.toggle('hidden');
}}

// Form submission handler
function handleFormSubmit(event) {{
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    // Show success message
    alert('Thank you! We will contact you soon.');
    form.reset();
    return false;
}}

// Scroll reveal animations
const observerOptions = {{ threshold: 0.1, rootMargin: '0px 0px -100px 0px' }};
const observer = new IntersectionObserver((entries) => {{
    entries.forEach(entry => {{
        if (entry.isIntersecting) {{
            entry.target.classList.add('animate-fade-in-up');
            observer.unobserve(entry.target);
        }}
    }});
}}, observerOptions);
document.querySelectorAll('.fade-on-scroll').forEach(el => observer.observe(el));

// Navbar scroll effect
window.addEventListener('scroll', () => {{
    const navbar = document.getElementById('navbar');
    if (navbar) {{
        if (window.scrollY > 50) navbar.classList.add('scrolled');
        else navbar.classList.remove('scrolled');
    }}
}});
```

7️⃣ FUNCTIONALITY CHECKLIST (ALL MUST WORK):
✅ All navigation links scroll smoothly to sections
✅ Mobile menu toggles open/close
✅ Contact form submits and shows confirmation
✅ Hover states on all buttons
✅ Scroll animations trigger on view
✅ All buttons have proper onclick handlers
✅ Responsive layout works on all screen sizes

OUTPUT JSON ONLY: {{"files": {{"index.html": "FULL HTML", "styles.css": "500+ LINES CSS", "app.js": "INTERACTIVE JS WITH ALL FUNCTIONS"}}}}"""
        
        # Industry-specific sections
        recommended_sections = detector.get_recommended_sections(website_type)
        section_hints = ", ".join(recommended_sections[:5]) if recommended_sections else "hero, features, about, contact"
        
        # REQUIREMENT-FOCUSED user prompt
        user_prompt = f"""CREATE: "{prompt}"

🎯 TEMPLATE: {template_def['name']}
📐 LAYOUT: {template_def['layout']}
🧭 NAVIGATION: {template_def['navigation']}

🚨 CRITICAL REQUIREMENTS:
1. Follow {template_def['name']} layout EXACTLY as described above
2. Implement ALL these features: {', '.join(template_def['features'][:4])}
3. Extract ALL requirements from user prompt (sections, features, functionality)
4. Use ICONS for features/services (NO images except hero)
5. Make everything functional (forms, buttons, animations)

🖼️ IMAGE USAGE (STRICT):
- Hero section: {'Use this exact URL: ' + hero_image if hero_image else 'Use gradient background'}
- All other sections: ICONS ONLY (fa-solid fa-icon-name)
- Example icons: fa-dumbbell, fa-utensils, fa-code, fa-heart, fa-star, fa-check-circle

🎨 COLORS TO USE:
- Primary: {colors['primary']}
- Secondary: {colors['secondary']}  
- Accent: {colors['accent']}

🔥 OUTPUT:
Return complete website with index.html, styles.css, app.js in JSON format.
Follow the {template_def['name']} template structure. Make it UNIQUE for this business.

🚨 FINAL CHECKS:

1️⃣ ANALYZE THE USER'S PROMPT:
- Extract EVERY section mentioned (About, Services, Pricing, Team, FAQ, Testimonials, Blog, etc.)
- Extract EVERY feature/service listed - create icon card for each
- If pricing/plans/subscriptions mentioned → CREATE pricing section with 3 tiers
- If booking/appointments mentioned → ADD booking form
- If gallery/portfolio mentioned → CREATE grid with icon placeholders (no images)
- If team/staff mentioned → CREATE team section with icon avatars

2️⃣ IMPLEMENT EVERYTHING - NO SHORTCUTS:
✅ Create ALL sections requested in prompt
✅ Make forms functional (validation, error messages)
✅ Make buttons work (smooth scroll, modals, actions)
✅ Add animations (fade-in-up on scroll)
✅ Make it responsive (mobile, tablet, desktop)

3️⃣ USE ICONS - NOT IMAGES (except hero):
✅ Features/Services: Icon cards with fa-solid icons
✅ Team members: Icon avatars (fa-user-circle)
✅ Pricing: Plan-specific icons (fa-cube, fa-crown, fa-building)
✅ Process steps: Numbered icons (fa-1, fa-2, fa-3)
✅ Benefits: Checkmark icons (fa-check-circle)

4️⃣ DESIGN VARIETY:
✅ Use the randomized design system provided above
✅ Apply random colors from palette: {colors['name']}
✅ Use random layout: {design_system['layout_pattern']}
✅ Apply random animations from list

5️⃣ OUTPUT FORMAT:
Return JSON with 3 files:
- index.html: Complete HTML with ALL sections from prompt
- styles.css: 400+ lines with animations, hover effects, responsive
- app.js: Interactive features (scroll, forms, animations)

EXAMPLE ICON USAGE:
Fitness: fa-dumbbell, fa-heart-pulse, fa-trophy
Restaurant: fa-utensils, fa-burger, fa-martini-glass
Tech: fa-code, fa-server, fa-rocket
Business: fa-briefcase, fa-chart-line, fa-handshake
Medical: fa-stethoscope, fa-pills, fa-user-doctor
✅ Make it industry-appropriate, visually STUNNING, with smooth animations!"""

        # Try multiple models if one fails
        # ONLY use models that actually work with this Emergent API key
        # Tested: gpt-5, gpt-5-mini, gpt-4o, gpt-4o-mini all WORK
        # claude-sonnet-4 and gemini-2.5-pro return "Invalid model name" errors
        models_to_try = [
            (provider, model),  # Try requested model first
            ("openai", "gpt-4o"),  # Fallback to GPT-4o (very reliable)
            ("openai", "gpt-4o-mini"),  # Fallback to GPT-4o mini
            ("openai", "gpt-5-mini"),  # Last resort - fast
        ]
        
        # Remove duplicates while preserving order
        seen = set()
        unique_models = []
        for p, m in models_to_try:
            key = f"{p}/{m}"
            if key not in seen:
                seen.add(key)
                unique_models.append((p, m))
        
        response = None
        all_errors = []
        total_attempts = 0
        max_total_attempts = 6  # 🚨 BALANCED: 6 attempts across multiple models (2 per model) to generate custom content
        
        for model_idx, (try_provider, try_model) in enumerate(unique_models):
            # Stop if we've already made too many attempts
            if total_attempts >= max_total_attempts:
                logger.warning(f"🛑 STOPPING: Already made {total_attempts} attempts to save credits")
                logger.warning(f"🛡️ Activating failsafe to prevent credit waste")
                break
            
            try:
                logger.info(f"🤖 Trying model {model_idx + 1}/{len(unique_models)}: {try_provider}/{try_model}")
                
                chat = LlmChat(
                    api_key=self.api_key,
                    session_id=f"{session_id}_{model_idx}",
                    system_message=system_prompt
                )
                chat.with_model(try_provider, try_model)
                
                # Set max_tokens to allow complete responses
                chat.with_params(max_tokens=16000)
                
                # 🚨 BALANCED RETRIES: 2 retries per model for custom generation
                max_retries = 2  # Balanced between credit protection and custom generation
                last_error = None
                
                for attempt in range(max_retries):
                    total_attempts += 1
                    
                    # Check if we've exceeded total attempts
                    if total_attempts > max_total_attempts:
                        logger.warning(f"🛑 Exceeded {max_total_attempts} total attempts")
                        break
                    
                    try:
                        logger.info(f"🔄 Attempt {total_attempts}/{max_total_attempts} TOTAL with {try_provider}/{try_model}")
                        
                        # Request with 60s timeout (reduced from 90s to fail faster)
                        response = await asyncio.wait_for(
                            chat.send_message(UserMessage(text=user_prompt)),
                            timeout=60.0
                        )
                        logger.info(f"✅ AI Response received: {len(response)} characters from {try_provider}/{try_model}")
                        logger.info(f"   Response preview: {response[:200]}...")
                        break  # Success! Exit retry loop
                        
                    except asyncio.TimeoutError:
                        last_error = "Request timed out after 60 seconds"
                        logger.warning(f"⏱️ Timeout on attempt {total_attempts}")
                        # 🚨 NO RETRY on timeout - it wastes time and credits
                        break
                        
                    except Exception as e:
                        error_str = str(e)
                        last_error = error_str
                        logger.error(f"❌ Error: {error_str[:150]}")
                        
                        # 🚨 Detect 502/503 errors but DON'T stop - try next model
                        is_502 = '502' in error_str or 'BadGateway' in error_str.lower()
                        is_503 = '503' in error_str or 'service unavailable' in error_str.lower()
                        
                        if is_502 or is_503:
                            logger.warning(f"⚠️ 502/503 error on {try_provider}/{try_model} - will try next model")
                            # Don't stop - let the system try other models
                            break  # Break from retry loop, continue to next model
                        
                        # Don't retry for other errors either
                        break
                
                # If we got a response, break out of model loop
                if response is not None:
                    logger.info(f"🎉 SUCCESS with {try_provider}/{try_model}!")
                    break
                
                # If we hit credit protection limit, stop trying other models
                if total_attempts >= max_total_attempts:
                    logger.warning(f"🛑 Credit protection activated after {total_attempts} attempts")
                    break
                    
                # Store this model's error and try next model
                all_errors.append(f"{try_provider}/{try_model}: {last_error}")
                logger.warning(f"❌ {try_provider}/{try_model} failed, trying next model...")
                
            except Exception as model_error:
                total_attempts += 1
                all_errors.append(f"{try_provider}/{try_model}: {str(model_error)}")
                logger.error(f"❌ Fatal error with {try_provider}/{try_model}: {str(model_error)[:100]}")
                
                # Check for 502 in fatal errors too
                if '502' in str(model_error) or 'BadGateway' in str(model_error):
                    logger.error(f"🚨 502 ERROR in fatal error - stopping all attempts")
                    break
                continue
        
        # Check if we got a response from any model
        if response is None:
            # Check if it was a 502 error
            has_502_error = any('502' in err or 'BadGateway' in err for err in all_errors)
            
            logger.error(f"❌ ALL MODELS FAILED - {len(unique_models)} models tried, {total_attempts} total attempts")
            logger.error(f"   Models attempted: {[f'{p}/{m}' for p, m in unique_models]}")
            logger.error(f"   Errors encountered:")
            for i, err in enumerate(all_errors, 1):
                logger.error(f"      {i}. {err[:200]}")
            
            if has_502_error:
                logger.warning(f"🚨 AI SERVICE UNAVAILABLE - 502 errors detected across all models")
                logger.warning(f"🛡️ Triggering smart failsafe - user will get customized website based on prompt")
            else:
                logger.error(f"🚨 GENERATION FAILED - Non-502 errors")
                logger.warning(f"🛡️ Triggering smart failsafe - user will get customized website")
            
            # Trigger failsafe by raising exception (will be caught below)
            raise Exception(f"AI generation failed after {total_attempts} attempts with {len(unique_models)} models")
        
        # Parse the JSON response
        try:
            project_data = self._parse_project_response(response)
            
            if not project_data.get("files"):
                logger.error("❌ CRITICAL: No files parsed from AI response")
                logger.error(f"❌ Response length: {len(response)}")
                logger.error(f"❌ Response starts: {response[:1000]}")
                
                # Try alternative text extraction as last resort
                logger.warning("Attempting alternative text extraction...")
                project_data = self._extract_files_from_text(response)
                
                if not project_data.get("files"):
                    logger.error("❌ PARSING COMPLETELY FAILED")
                    logger.error("This should NOT happen - AI should return valid JSON")
                    
                    # Save the failed response for debugging
                    with open("/tmp/failed_ai_response.txt", "w") as f:
                        f.write(response)
                    logger.error("Failed response saved to /tmp/failed_ai_response.txt")
                    
                    raise Exception("AI response parsing failed - check logs and /tmp/failed_ai_response.txt")
                else:
                    logger.warning(f"⚠️ Extracted {len(project_data['files'])} files from text (not JSON)")
            else:
                logger.info(f"✅ Successfully parsed {len(project_data['files'])} files from JSON response")
            
            # Basic validation only (removed extra requirement checks that burn credits)
            self._validate_netlify_project(project_data)
            
            # CRITICAL: Validate and enhance HTML to ensure it has design frameworks
            project_data = self._ensure_design_quality(project_data, prompt)
            
            logger.info(f"✅ Netlify project ready with {len(project_data['files'])} files")
            return project_data
            
        except Exception as e:
            error_msg = str(e).lower()
            logger.error(f"⚠️ AI Generation failed: {str(e)[:200]}")
            
            # SMART FALLBACK when API is unavailable (502 errors)
            # This generates CUSTOM code based on the prompt, NOT a generic template
            logger.warning("🛡️ SMART FAILSAFE: API unavailable (502), generating custom code from prompt")
            
            try:
                # Analyze the prompt to understand what to build
                fallback_analysis = self._analyze_prompt_for_fallback(prompt)
                logger.info(f"📋 Prompt analysis: {fallback_analysis.get('business_type')} - {fallback_analysis.get('business_name')}")
                
                # Generate custom code based on the prompt analysis
                fallback_project = self._generate_smart_fallback(prompt, fallback_analysis)
                
                logger.info(f"✅ SMART FALLBACK SUCCESS: Generated custom website")
                logger.info(f"   HTML: {len(fallback_project['files'].get('index.html', ''))} chars")
                logger.info(f"   CSS: {len(fallback_project['files'].get('styles.css', ''))} chars")
                logger.info(f"   JS: {len(fallback_project['files'].get('app.js', ''))} chars")
                
                return fallback_project
                
            except Exception as fallback_error:
                logger.error(f"❌ Smart fallback also failed: {str(fallback_error)}")
                raise HTTPException(
                    status_code=500,
                    detail=f"Generation failed: {str(e)[:100]}. Please try again."
                )
    
    async def _edit_netlify_project(self, prompt: str, current_project: Dict, provider: str, model: str, session_id: str) -> Dict[str, Any]:
        """Edit an existing Netlify project"""
        
        current_files = current_project.get("files", {})
        logger.info(f"Editing project with {len(current_files)} existing files")
        
        # Extract what user wants to change/add
        edit_requirements = self._extract_requirements(prompt)
        logger.info(f"📝 Edit requirements: {edit_requirements}")
        
        edit_requirements_json = json.dumps(edit_requirements, indent=2)
        edit_checklist = self._generate_requirement_checklist(edit_requirements)
        
        system_prompt = f"""You are an expert full-stack developer editing a Netlify-deployed project.

🔄 EDITING MODE - PRESERVE EXISTING STRUCTURE + ADD NEW REQUIREMENTS

USER WANTS TO MAKE THESE CHANGES:
{edit_requirements_json}

CRITICAL RULES:
1. You are EDITING existing code, NOT creating from scratch
2. PRESERVE all existing files unless explicitly asked to remove them
3. ADD/MODIFY the specific items user requested
4. Make SURGICAL changes - only modify what's requested
5. Maintain Netlify Functions format and structure
6. Keep netlify.toml configuration unless changes are needed
7. Return the COMPLETE project with modifications

⚠️ VERIFICATION CHECKLIST FOR EDITS:
{edit_checklist}

EVERY item above MUST be present in your edited code. Check before submitting.

OUTPUT FORMAT: JSON with same structure as creation, but with edited files.
"""
        
        # Build context with current files
        files_context = "\n".join([
            f"=== {path} ({len(content)} chars) ===\n{content[:500]}..." 
            for path, content in list(current_files.items())[:10]
        ])
        
        user_prompt = f"""Edit this Netlify project:

USER'S EDIT REQUEST:
{prompt}

CURRENT PROJECT FILES:
{files_context}

INSTRUCTIONS:
1. Analyze what the user wants to change
2. Modify ONLY the affected files
3. Preserve all other files exactly as they are
4. Return the complete project JSON with edits applied

Ensure the edited project remains Netlify-compatible!"""

        try:
            chat = LlmChat(
                api_key=self.api_key,
                session_id=session_id,
                system_message=system_prompt
            )
            chat.with_model(provider, model)
            
            # Set max_tokens to allow complete responses
            chat.with_params(max_tokens=16000)
            
            response = await chat.send_message(UserMessage(text=user_prompt))
            logger.info(f"✅ Edit response received: {len(response)} characters")
            
            # Parse edited project
            edited_project = self._parse_project_response(response)
            
            if not edited_project.get("files"):
                logger.warning("Could not parse edited project from response")
                logger.info("Attempting alternative extraction...")
                edited_project = self._extract_files_from_text(response)
                
                if not edited_project.get("files"):
                    logger.error("❌ Edit failed - could not extract files")
                    logger.warning("Returning original project unchanged")
                    return current_project
                else:
                    logger.info(f"✅ Extracted {len(edited_project['files'])} files from text")
            
            logger.info(f"✅ Edit complete: {len(edited_project['files'])} files")
            return edited_project
            
        except Exception as e:
            error_msg = str(e).lower()
            if "budget" in error_msg or "exceeded" in error_msg:
                logger.error(f"❌ BUDGET ERROR during edit: {str(e)}")
                raise HTTPException(status_code=402, detail=f"API budget exceeded: {str(e)}")
            
            logger.error(f"❌ Edit failed: {str(e)}")
            logger.warning("Returning original project unchanged")
            return current_project
    
    async def _retry_with_missing_requirements(
        self, 
        original_prompt: str,
        requirements: Dict[str, List[str]],
        missing_requirements: List[str],
        provider: str,
        model: str,
        session_id: str
    ) -> Optional[Dict[str, Any]]:
        """
        Retry generation with explicit focus on missing requirements
        """
        logger.info("🔄 RETRY: Adding missing requirements to generation")
        
        missing_list = "\n".join([f"- {req}" for req in missing_requirements])
        
        enhanced_prompt = f"""CRITICAL RETRY - MISSING REQUIREMENTS DETECTED

Original request: {original_prompt}

YOU FAILED TO INCLUDE THESE REQUIRED ITEMS:
{missing_list}

Generate a COMPLETE project that includes:
1. Everything from the original request
2. SPECIFICALLY add all the missing items listed above

This is your LAST CHANCE to get it right. Include EVERY requirement."""

        retry_system = """You are an expert developer who NEVER misses requirements.

Your previous attempt was INCOMPLETE. You MUST now generate code that includes EVERY SINGLE requirement.

Focus especially on the missing items, but don't remove anything you already had."""

        try:
            chat = LlmChat(
                api_key=self.api_key,
                session_id=f"{session_id}_retry",
                system_message=retry_system
            )
            chat.with_model(provider, model)
            
            # Set max_tokens to allow complete responses
            chat.with_params(max_tokens=16000)
            
            response = await chat.send_message(UserMessage(text=enhanced_prompt))
            logger.info(f"✅ Retry response received: {len(response)} characters")
            
            project_data = self._parse_project_response(response)
            
            if project_data.get("files"):
                # Validate retry attempt
                html_content = project_data.get("files", {}).get("index.html", "")
                retry_validation = self._validate_requirements(html_content, requirements)
                
                logger.info(f"📊 Retry validation: {retry_validation['completeness_score']:.1f}%")
                
                if retry_validation["completeness_score"] > 70:
                    logger.info("✅ Retry successful! Completeness improved.")
                    return project_data
                else:
                    logger.warning("⚠️ Retry still incomplete. Proceeding with best effort.")
                    return project_data
            
        except Exception as e:
            logger.error(f"Retry failed: {str(e)}")
        
        return None
    
    async def _analyze_project_requirements(self, prompt: str, provider: str, model: str, session_id: str) -> Dict[str, Any]:
        """Analyze what the user wants to build"""
        
        analysis_prompt = f"""Analyze this project request and extract requirements:

"{prompt}"

Respond with JSON:
{{
  "project_type": "landing_page|web_app|dashboard|e_commerce|blog|portfolio",
  "framework": "react|nextjs|vanilla",
  "needs_backend": true|false,
  "needs_database": true|false,
  "features": ["contact_form", "user_auth", "api_integration", etc],
  "database_type": "supabase|faunadb|firebase|none"
}}"""

        try:
            chat = LlmChat(
                api_key=self.api_key,
                session_id=f"{session_id}_analysis",
                system_message="You are a project requirements analyzer. Respond ONLY with valid JSON."
            )
            chat.with_model(provider, model)
            
            # Set max_tokens to allow complete responses
            chat.with_params(max_tokens=16000)
            
            response = await chat.send_message(UserMessage(text=analysis_prompt))
            
            # Extract JSON from response
            json_match = response[response.find("{"):response.rfind("}")+1]
            return json.loads(json_match)
            
        except Exception as e:
            logger.error(f"Analysis failed: {str(e)}")
            # Return default analysis
            return {
                "project_type": "web_app",
                "framework": "vanilla",
                "needs_backend": False,
                "needs_database": False,
                "features": [],
                "database_type": "none"
            }
    
    def _parse_project_response(self, response: str) -> Dict[str, Any]:
        """Parse AI response to extract project structure"""
        try:
            # Log first 500 chars of response for debugging
            logger.info(f"Response preview: {response[:500]}")
            
            # Strip any leading/trailing whitespace
            response = response.strip()
            
            # SMART APPROACH: Try multiple parsing strategies
            
            # Strategy 1: Try standard JSON parsing with increased limits
            if response.startswith('{'):
                logger.info("✅ Response starts with JSON object")
                
                try:
                    # Try direct JSON parsing first
                    project_data = json.loads(response)
                    
                    if "files" in project_data and isinstance(project_data["files"], dict):
                        logger.info(f"✅ Standard JSON parse successful: {len(project_data['files'])} files")
                        return self._process_files(project_data)
                except json.JSONDecodeError as e:
                    logger.warning(f"Standard JSON parse failed: {str(e)}")
                    
                    # Try manual extraction of files object
                    try:
                        logger.info("Attempting manual JSON files extraction...")
                        files_match = re.search(r'"files"\s*:\s*\{', response)
                        if files_match:
                            # Find the start of the files object
                            files_start = files_match.end() - 1
                            
                            # Manually extract each file using quotes
                            extracted_files = {}
                            
                            # Find all file entries
                            file_patterns = [
                                (r'"index\.html"\s*:\s*"', 'index.html'),
                                (r'"styles\.css"\s*:\s*"', 'styles.css'),
                                (r'"app\.js"\s*:\s*"', 'app.js'),
                                (r'"script\.js"\s*:\s*"', 'script.js'),
                                (r'"netlify\.toml"\s*:\s*"', 'netlify.toml'),
                            ]
                            
                            for pattern, filename in file_patterns:
                                match = re.search(pattern, response, re.IGNORECASE)
                                if match:
                                    logger.info(f"Found pattern for {filename} at position {match.start()}")
                                    content_start = match.end()
                                    closing_pos = self._find_closing_quote(response, content_start)
                                    
                                    logger.info(f"Closing quote for {filename} at position {closing_pos}")
                                    
                                    if closing_pos > content_start:
                                        content = response[content_start:closing_pos]
                                        # Unescape
                                        content = content.replace('\\n', '\n')
                                        content = content.replace('\\"', '"')
                                        content = content.replace('\\\\', '\\')
                                        content = content.replace('\\/', '/')
                                        
                                        logger.info(f"Content length after unescape: {len(content)}")
                                        
                                        if len(content) > 50:
                                            extracted_files[filename] = content
                                            logger.info(f"✅ Manually extracted {filename} ({len(content)} chars)")
                                        else:
                                            logger.warning(f"Content too short for {filename}: {len(content)} chars")
                                    else:
                                        logger.warning(f"Could not find closing quote for {filename} (start: {content_start}, close: {closing_pos})")
                                else:
                                    logger.warning(f"Pattern not found for {filename}")
                            
                            if extracted_files:
                                logger.info(f"✅ Manual JSON extraction successful: {len(extracted_files)} files")
                                return {
                                    "files": extracted_files,
                                    "deploy_config": {
                                        "build_command": "",
                                        "publish_dir": ".",
                                        "functions_dir": "netlify/functions"
                                    }
                                }
                    except Exception as manual_e:
                        logger.warning(f"Manual extraction also failed: {str(manual_e)}")
                    
                    logger.info("Trying alternative extraction methods...")
            
            # Strategy 2: Extract using regex for file blocks
            logger.info("Attempting regex-based file extraction...")
            files = self._extract_files_with_regex(response)
            
            if files:
                logger.info(f"✅ Regex extraction successful: {len(files)} files")
                return {
                    "files": files,
                    "deploy_config": {
                        "build_command": "",
                        "publish_dir": ".",
                        "functions_dir": "netlify/functions",
                        "environment_variables": {}
                    }
                }
            
            # Strategy 3: Try the old text extraction
            logger.info("Attempting text-based extraction...")
            return self._extract_files_from_text(response)
            
            # Fallback: Try to find JSON block within response
            json_start = response.find('{"files"')
            if json_start < 0:
                json_start = response.find('{')
            
            if json_start < 0:
                logger.error("No JSON block found in response")
                logger.info(f"Response length: {len(response)}, starts with: {response[:200]}")
                return {}
            
            json_end = response.rfind("}") + 1
            
            if json_end <= json_start:
                logger.error("Invalid JSON boundaries")
                return {}
            
            json_str = response[json_start:json_end]
            logger.info(f"Attempting to parse JSON substring of length: {len(json_str)}")
            
            # Try parsing
            project_data = json.loads(json_str)
            
            # Validate structure
            if "files" in project_data and isinstance(project_data["files"], dict):
                logger.info(f"✅ Valid project structure with {len(project_data['files'])} files")
                return project_data
            else:
                logger.warning("JSON parsed but missing 'files' key or invalid structure")
                logger.info(f"Keys found: {list(project_data.keys())}")
                return {}
                
        except json.JSONDecodeError as e:
            logger.error(f"JSON parse error: {str(e)}")
            logger.error(f"Error at position {e.pos}")
            if 'json_str' in locals():
                logger.error(f"Context: ...{json_str[max(0, e.pos-50):min(len(json_str), e.pos+50)]}...")
            return {}
        except Exception as e:
            logger.error(f"Unexpected error parsing response: {str(e)}")
            return {}
    
    def _extract_requirements(self, prompt: str) -> Dict[str, List[str]]:
        """
        Extract explicit requirements from user prompt
        Returns categorized list of what user asked for
        """
        requirements = {
            "sections": [],
            "features": [],
            "elements": [],
            "styling": [],
            "content": [],
            "functionality": []
        }
        
        prompt_lower = prompt.lower()
        
        # Common section keywords
        section_keywords = [
            "hero", "header", "footer", "navbar", "navigation", "menu",
            "about", "features", "pricing", "testimonials", "gallery",
            "contact", "form", "blog", "portfolio", "services", "team",
            "faq", "banner", "sidebar", "carousel", "slider"
        ]
        
        # Feature keywords
        feature_keywords = [
            "search", "filter", "authentication", "login", "signup",
            "cart", "checkout", "payment", "subscribe", "newsletter",
            "social", "share", "comment", "rating", "review"
        ]
        
        # Element keywords
        element_keywords = [
            "button", "link", "image", "video", "icon", "card",
            "modal", "popup", "dropdown", "tooltip", "badge",
            "alert", "notification", "progress", "spinner"
        ]
        
        # Extract sections
        for keyword in section_keywords:
            if keyword in prompt_lower:
                requirements["sections"].append(keyword)
        
        # Extract features
        for keyword in feature_keywords:
            if keyword in prompt_lower:
                requirements["features"].append(keyword)
        
        # Extract elements
        for keyword in element_keywords:
            if keyword in prompt_lower:
                requirements["elements"].append(keyword)
        
        # Look for numbered lists or bullet points
        import re
        
        # Find numbered requirements (1. 2. 3.)
        numbered = re.findall(r'\d+\.\s*([^\n]+)', prompt)
        if numbered:
            requirements["content"].extend(numbered)
        
        # Find bullet points (- or *)
        bullets = re.findall(r'[-*]\s*([^\n]+)', prompt)
        if bullets:
            requirements["content"].extend(bullets)
        
        # Extract specific counts (e.g., "3 cards", "5 testimonials")
        counts = re.findall(r'(\d+)\s+([a-zA-Z]+)', prompt)
        for count, item in counts:
            requirements["content"].append(f"{count} {item}")
        
        # Extract quoted text (specific content requested)
        quoted = re.findall(r'["\']([^"\']+)["\']', prompt)
        if quoted:
            requirements["content"].extend(quoted)
        
        # If no specific requirements found, parse the whole prompt
        if not any(requirements.values()):
            # Split by common separators
            parts = re.split(r'[,;]|\s+with\s+|\s+and\s+|\s+including\s+', prompt)
            requirements["content"] = [p.strip() for p in parts if len(p.strip()) > 3]
        
        return requirements
    
    def _generate_requirement_checklist(self, requirements: Dict[str, List[str]]) -> str:
        """Generate a checklist string from requirements"""
        checklist = []
        
        if requirements["sections"]:
            checklist.append("SECTIONS TO INCLUDE:")
            for section in requirements["sections"]:
                checklist.append(f"  ☐ {section.title()} section")
        
        if requirements["features"]:
            checklist.append("\nFEATURES TO IMPLEMENT:")
            for feature in requirements["features"]:
                checklist.append(f"  ☐ {feature.title()} functionality")
        
        if requirements["elements"]:
            checklist.append("\nELEMENTS TO ADD:")
            for element in requirements["elements"]:
                checklist.append(f"  ☐ {element.title()} elements")
        
        if requirements["content"]:
            checklist.append("\nSPECIFIC CONTENT REQUESTED:")
            for content in requirements["content"]:
                checklist.append(f"  ☐ {content}")
        
        if not checklist:
            checklist.append("☐ Implement all features described in the prompt")
        
        return "\n".join(checklist)
    
    def _validate_requirements(self, generated_html: str, requirements: Dict[str, List[str]]) -> Dict[str, Any]:
        """
        Validate that generated HTML contains all requested requirements
        Returns validation report
        """
        html_lower = generated_html.lower()
        
        validation_report = {
            "all_requirements_met": True,
            "missing_requirements": [],
            "found_requirements": [],
            "completeness_score": 0.0
        }
        
        total_requirements = 0
        found_requirements = 0
        
        # Check sections
        for section in requirements.get("sections", []):
            total_requirements += 1
            # Look for section in HTML (as class, id, or text)
            if section.lower() in html_lower:
                found_requirements += 1
                validation_report["found_requirements"].append(f"Section: {section}")
            else:
                validation_report["missing_requirements"].append(f"Section: {section}")
        
        # Check features
        for feature in requirements.get("features", []):
            total_requirements += 1
            if feature.lower() in html_lower:
                found_requirements += 1
                validation_report["found_requirements"].append(f"Feature: {feature}")
            else:
                validation_report["missing_requirements"].append(f"Feature: {feature}")
        
        # Check elements
        for element in requirements.get("elements", []):
            total_requirements += 1
            if element.lower() in html_lower:
                found_requirements += 1
                validation_report["found_requirements"].append(f"Element: {element}")
            else:
                validation_report["missing_requirements"].append(f"Element: {element}")
        
        # Check specific content
        for content in requirements.get("content", []):
            total_requirements += 1
            # More lenient check for content - look for key words
            content_words = content.lower().split()
            if any(word in html_lower for word in content_words if len(word) > 3):
                found_requirements += 1
                validation_report["found_requirements"].append(f"Content: {content}")
            else:
                validation_report["missing_requirements"].append(f"Content: {content}")
        
        # Calculate completeness
        if total_requirements > 0:
            validation_report["completeness_score"] = (found_requirements / total_requirements) * 100
        else:
            validation_report["completeness_score"] = 100.0
        
        validation_report["all_requirements_met"] = len(validation_report["missing_requirements"]) == 0
        
        return validation_report
    
    def _process_files(self, project_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process files - decode base64 if needed"""
        if "files" not in project_data:
            return project_data
        
        decoded_files = {}
        for filepath, content in project_data["files"].items():
            if isinstance(content, str):
                # Try to decode from base64
                try:
                    import base64
                    decoded_content = base64.b64decode(content).decode('utf-8')
                    decoded_files[filepath] = decoded_content
                    logger.info(f"✅ Decoded {filepath} from base64")
                except Exception:
                    # Not base64, use as-is
                    decoded_files[filepath] = content
            else:
                decoded_files[filepath] = content
        
        project_data["files"] = decoded_files
        return project_data
    
    def _extract_files_with_regex(self, response: str) -> Dict[str, str]:
        """
        Extract files using regex patterns when JSON parsing fails
        Handles BOTH escaped JSON strings AND raw unescaped content
        """
        files = {}
        
        try:
            import re
            
            # Strategy 1: Try to extract from properly escaped JSON
            # Pattern: "filename.ext": "escaped content"
            pattern = r'"([^"]+\.(html|css|js|toml|md|txt))"\s*:\s*"'
            matches = list(re.finditer(pattern, response, re.IGNORECASE))
            
            logger.info(f"Found {len(matches)} file pattern matches")
            
            for match in matches:
                filename = match.group(1)
                start_pos = match.end()  # Position after the opening quote of content
                
                # Find the closing quote (accounting for escaped quotes)
                content_end = self._find_closing_quote(response, start_pos)
                
                if content_end > start_pos:
                    raw_content = response[start_pos:content_end]
                    
                    # Unescape the content
                    unescaped_content = raw_content.replace('\\n', '\n')
                    unescaped_content = unescaped_content.replace('\\"', '"')
                    unescaped_content = unescaped_content.replace('\\\\', '\\')
                    unescaped_content = unescaped_content.replace('\\t', '\t')
                    
                    files[filename] = unescaped_content
                    logger.info(f"✅ Extracted {filename} ({len(unescaped_content)} chars)")
            
            # Strategy 2: If that didn't work, try extracting raw content
            # The AI might be outputting: "index.html": <!DOCTYPE html>...
            # Instead of: "index.html": "<!DOCTYPE html>..."
            if not files:
                logger.info("Strategy 1 failed, trying raw content extraction...")
                files = self._extract_raw_content(response)
            
            # Strategy 3: If we have HTML but no separate CSS/JS, extract embedded content
            if files and 'index.html' in files and ('styles.css' not in files or 'app.js' not in files):
                logger.info("Found HTML-only, extracting embedded CSS and JS...")
                files = self._extract_embedded_content(files)
            
        except Exception as e:
            logger.error(f"Regex extraction error: {str(e)}")
        
        return files
    
    def _extract_raw_content(self, response: str) -> Dict[str, str]:
        """
        Extract files when AI outputs raw content without proper JSON escaping
        Example: "index.html": <!DOCTYPE html>... instead of "index.html": "<!DOCTYPE..."
        """
        files = {}
        
        try:
            import re
            
            # Look for: "filename.ext": followed by content (not in quotes)
            # We need to find where the file starts and where it ends
            
            # Pattern to find file declarations
            pattern = r'"(index\.html|styles\.css|app\.js|script\.js|netlify\.toml|README\.md)"\s*:\s*'
            matches = list(re.finditer(pattern, response, re.IGNORECASE))
            
            logger.info(f"Found {len(matches)} raw content patterns")
            
            for i, match in enumerate(matches):
                filename = match.group(1)
                content_start = match.end()
                
                # Check if content is in quotes
                if response[content_start:content_start+1] == '"':
                    # Content is properly quoted - find the closing quote
                    content_start += 1  # Skip opening quote
                    
                    # Find the closing quote (handling escaped quotes)
                    closing_pos = self._find_closing_quote(response, content_start)
                    
                    if closing_pos > content_start:
                        raw_content = response[content_start:closing_pos]
                        
                        # Unescape the content
                        raw_content = raw_content.replace('\\n', '\n')
                        raw_content = raw_content.replace('\\"', '"')
                        raw_content = raw_content.replace('\\\\', '\\')
                        raw_content = raw_content.replace('\\/', '/')
                        
                        if len(raw_content) > 50:
                            files[filename] = raw_content
                            logger.info(f"✅ Extracted {filename} ({len(raw_content)} chars) via raw extraction")
                    else:
                        logger.warning(f"Could not find closing quote for {filename}")
                else:
                    # Content is NOT quoted - try to find the end
                    if i < len(matches) - 1:
                        content_end = matches[i + 1].start()
                    else:
                        # Last file - try to find reasonable endpoint
                        # Look for the end of the files object
                        remaining = response[content_start:]
                        
                        # Try multiple patterns for finding the end
                        end_patterns = [
                            r'"\s*,\s*"deploy_config"',  # Next key
                            r'"\s*\}',  # End of files object
                            r'\}\s*,\s*"deploy_config"',  # End with deploy_config
                        ]
                        
                        content_end = len(response)
                        for pattern in end_patterns:
                            match_end = re.search(pattern, remaining)
                            if match_end:
                                content_end = content_start + match_end.start()
                                break
                    
                    raw_content = response[content_start:content_end].strip()
                    raw_content = raw_content.rstrip(',').strip()
                    
                    if raw_content and len(raw_content) > 50:
                        files[filename] = raw_content
                        logger.info(f"✅ Extracted {filename} ({len(raw_content)} chars) via raw extraction")
            
        except Exception as e:
            logger.error(f"Raw content extraction error: {str(e)}")
        
        return files
    
    def _extract_embedded_content(self, files: Dict[str, str]) -> Dict[str, str]:
        """
        Extract embedded <style> and <script> tags from HTML and create separate files
        """
        if 'index.html' not in files:
            return files
        
        html = files['index.html']
        extracted_files = files.copy()
        
        try:
            import re
            
            # Extract CSS from <style> tags
            if 'styles.css' not in files:
                style_pattern = r'<style[^>]*>(.*?)</style>'
                style_matches = re.findall(style_pattern, html, re.DOTALL | re.IGNORECASE)
                
                if style_matches:
                    css_content = '\n\n'.join(style_matches)
                    extracted_files['styles.css'] = css_content
                    logger.info(f"✅ Extracted CSS from <style> tags ({len(css_content)} chars)")
                    
                    # Remove <style> tags from HTML and add <link>
                    html = re.sub(style_pattern, '', html, flags=re.DOTALL | re.IGNORECASE)
                    
                    # Add link to external CSS if not present
                    if 'href="styles.css"' not in html and "href='styles.css'" not in html:
                        # Insert after <head> tag
                        html = html.replace('</head>', '    <link rel="stylesheet" href="styles.css">\n</head>')
            
            # Extract JavaScript from <script> tags (excluding external scripts)
            if 'app.js' not in files and 'script.js' not in files:
                # Match script tags that don't have src attribute
                script_pattern = r'<script(?![^>]*\ssrc=)[^>]*>(.*?)</script>'
                script_matches = re.findall(script_pattern, html, re.DOTALL | re.IGNORECASE)
                
                if script_matches:
                    js_content = '\n\n'.join(script_matches)
                    extracted_files['app.js'] = js_content
                    logger.info(f"✅ Extracted JavaScript from <script> tags ({len(js_content)} chars)")
                    
                    # Remove inline scripts from HTML and add external script
                    html = re.sub(script_pattern, '', html, flags=re.DOTALL | re.IGNORECASE)
                    
                    # Add script tag before </body> if not present
                    if 'src="app.js"' not in html and "src='app.js'" not in html:
                        html = html.replace('</body>', '    <script src="app.js"></script>\n</body>')
            
            # Update HTML in files
            extracted_files['index.html'] = html
            
        except Exception as e:
            logger.error(f"Error extracting embedded content: {str(e)}")
        
        return extracted_files
    
    def _find_closing_quote(self, text: str, start_pos: int) -> int:
        """Find the closing quote position, handling escaped quotes"""
        i = start_pos
        while i < len(text):
            if text[i] == '"':
                # Check if it's escaped by counting preceding backslashes
                num_backslashes = 0
                j = i - 1
                while j >= 0 and text[j] == '\\':  # Changed from >= start_pos to >= 0
                    num_backslashes += 1
                    j -= 1
                
                # If even number of backslashes (or zero), this quote is not escaped
                if num_backslashes % 2 == 0:
                    return i
            i += 1
        
        return -1
    
    def _extract_files_from_text(self, response: str) -> Dict[str, Any]:
        """
        Extract files from text response when JSON parsing fails
        Looks for code blocks and file markers
        """
        files = {}
        
        # Try to find file markers like "index.html:", "styles.css:", etc.
        file_pattern = r'([a-zA-Z0-9_\-/\.]+\.(html|css|js|toml|json|md)):\s*```([a-z]*)\n(.*?)```'
        matches = re.finditer(file_pattern, response, re.DOTALL | re.IGNORECASE)
        
        for match in matches:
            filename = match.group(1)
            content = match.group(4).strip()
            files[filename] = content
            logger.info(f"Extracted file: {filename} ({len(content)} chars)")
        
        if files:
            return {
                "files": files,
                "deploy_config": {
                    "build_command": "",
                    "publish_dir": ".",
                    "functions_dir": "netlify/functions",
                    "environment_variables": {}
                }
            }
        
        return {}
    
    def _validate_netlify_project(self, project: Dict[str, Any]) -> bool:
        """Validate that project meets Netlify requirements"""
        files = project.get("files", {})
        
        # Check for netlify.toml
        if "netlify.toml" not in files:
            logger.warning("Missing netlify.toml - adding default")
            files["netlify.toml"] = self._generate_default_netlify_toml()
        
        # Check for package.json if using Node/React
        has_js_files = any(f.endswith('.jsx') or f.endswith('.tsx') for f in files.keys())
        if has_js_files and "package.json" not in files:
            logger.warning("Missing package.json - adding default")
            files["package.json"] = self._generate_default_package_json()
        
        return True
    
    def _generate_default_netlify_toml(self) -> str:
        """Generate a default netlify.toml configuration"""
        return """[build]
  publish = "."
  functions = "netlify/functions"

[[redirects]]
  from = "/api/*"
  to = "/.netlify/functions/:splat"
  status = 200
"""
    
    def _generate_default_package_json(self) -> str:
        """Generate a default package.json"""
        return json.dumps({
            "name": "netlify-project",
            "version": "1.0.0",
            "scripts": {
                "build": "echo 'No build step required for static site'"
            },
            "dependencies": {}
        }, indent=2)
    
    def _generate_fallback_project(self, prompt: str, analysis: Dict) -> Dict[str, Any]:
        """Generate a simple fallback project if AI generation fails"""
        logger.warning("Using fallback project generation")
        
        project_name = analysis.get("project_type", "web-app").replace("_", "-")
        
        return {
            "files": {
                "index.html": self._get_fallback_html(prompt),
                "styles.css": self._get_fallback_css(),
                "app.js": self._get_fallback_js(),
                "netlify.toml": self._generate_default_netlify_toml(),
                "README.md": f"# {project_name.title()}\n\nGenerated by Code Weaver for Netlify deployment.\n\n## Deploy\n\nDeploy to Netlify for instant live preview!"
            },
            "deploy_config": {
                "build_command": "",
                "publish_dir": ".",
                "functions_dir": "netlify/functions",
                "environment_variables": {}
            }
        }
    
    
    def _format_frameworks_knowledge(self) -> str:
        """Format comprehensive framework knowledge for AI"""
        output = ["═══════════════════════════════════════════════════════════════"]
        output.append("📚 COMPREHENSIVE FRAMEWORK & LIBRARY ACCESS")
        output.append("═══════════════════════════════════════════════════════════════\n")
        
        # CSS Frameworks
        output.append("**CSS FRAMEWORKS:**")
        for name, info in FRAMEWORKS['css_frameworks'].items():
            output.append(f"- {name.upper()}: {info['cdn'][0] if isinstance(info['cdn'], list) else info['cdn']}")
            output.append(f"  Usage: {info['usage']}")
        
        # Animation Libraries
        output.append("\n**ANIMATION LIBRARIES:**")
        for name, info in FRAMEWORKS['animation_libraries'].items():
            output.append(f"- {name.upper()}: {info['cdn'][0] if isinstance(info['cdn'], list) else info['cdn']}")
            output.append(f"  Usage: {info['usage']}")
        
        output.append("\n**3D & GRAPHICS:**")
        for name, info in FRAMEWORKS['3d_graphics'].items():
            output.append(f"- {name.upper()}: {info['cdn'][0]}")
            output.append(f"  Usage: {info['usage']}")
        
        output.append("\n**CHARTS & DATA VIZ:**")
        for name, info in FRAMEWORKS['charts_data_viz'].items():
            output.append(f"- {name.upper()}: {info['cdn'][0]}")
            output.append(f"  When: {info['when']}")
        
        output.append("\n**INTERACTIONS:**")
        for name, info in FRAMEWORKS['interaction_libraries'].items():
            output.append(f"- {name.upper()}: {', '.join(info['cdn']) if isinstance(info['cdn'], list) else info['cdn']}")
            output.append(f"  Usage: {info['usage']}")
        
        output.append("\n**FORMS & VALIDATION:**")
        for name, info in FRAMEWORKS['forms_validation'].items():
            output.append(f"- {name.upper()}: {info['cdn'][0]}")
        
        output.append("\n**NOTIFICATIONS:**")
        for name, info in FRAMEWORKS['notifications_modals'].items():
            output.append(f"- {name.upper()}: {info['cdn'][0]}")
            output.append(f"  Usage: {info['usage']}")
        
        return "\n".join(output)

    def _format_design_knowledge(self) -> str:
        """Format design principles and best practices"""
        output = ["\n═══════════════════════════════════════════════════════════════"]
        output.append("🎨 DESIGN KNOWLEDGE BASE")
        output.append("═══════════════════════════════════════════════════════════════\n")
        
        # Color Theory
        output.append("**COLOR THEORY:**")
        output.append("Popular Palettes:")
        for style, colors in DESIGN_PRINCIPLES['color_theory']['popular_palettes'].items():
            output.append(f"- {style.title()}: {', '.join(colors)}")
        
        output.append("\nColor Best Practices:")
        for practice in DESIGN_PRINCIPLES['color_theory']['best_practices']:
            output.append(f"• {practice}")
        
        # Typography
        output.append("\n**TYPOGRAPHY:**")
        output.append("Font Pairings:")
        for style, pairing in DESIGN_PRINCIPLES['typography']['font_pairings'].items():
            output.append(f"- {style.title()}: {pairing}")
        
        output.append("\nTypography Best Practices:")
        for practice in DESIGN_PRINCIPLES['typography']['best_practices']:
            output.append(f"• {practice}")
        
        # Spacing
        output.append("\n**SPACING & LAYOUT:**")
        output.append("Spacing Scale:")
        for size, value in DESIGN_PRINCIPLES['spacing_layout']['spacing_scale'].items():
            output.append(f"- {size}: {value}")
        
        output.append("\nLayout Best Practices:")
        for practice in DESIGN_PRINCIPLES['spacing_layout']['best_practices']:
            output.append(f"• {practice}")
        
        return "\n".join(output)

    def _format_component_patterns(self) -> str:
        """Format component design patterns"""
        output = ["\n═══════════════════════════════════════════════════════════════"]
        output.append("🧩 COMPONENT DESIGN PATTERNS")
        output.append("═══════════════════════════════════════════════════════════════\n")
        
        # Buttons
        output.append("**BUTTON PATTERNS:**")
        output.append("Primary Button CSS:")
        output.append(COMPONENT_PATTERNS['buttons']['primary_button']['css'])
        
        # Cards
        output.append("\n**CARD PATTERNS:**")
        output.append("Elevated Card CSS:")
        output.append(COMPONENT_PATTERNS['cards']['elevated_card']['css'])
        
        output.append("\nGlass Morphism Card CSS:")
        output.append(COMPONENT_PATTERNS['cards']['glass_card']['css'])
        
        # Forms
        output.append("\n**FORM PATTERNS:**")
        output.append("Modern Input CSS:")
        output.append(COMPONENT_PATTERNS['forms']['modern_input']['css'])
        
        # Website Patterns
        output.append("\n**WEBSITE TYPE PATTERNS:**")
        for web_type, info in WEBSITE_PATTERNS.items():
            output.append(f"\n{web_type.upper().replace('_', ' ')}:")
            output.append(f"Structure: {' → '.join(info['structure'])}")
            output.append(f"Color Scheme: {info['color_scheme']}")
            output.append("Design Tips:")
            for tip in info['design_tips']:
                output.append(f"• {tip}")
        
        return "\n".join(output)

    def _get_fallback_html(self, prompt: str) -> str:
        """Generate fallback HTML"""
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Code Weaver Project</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <header class="header">
            <h1>Welcome to Your Project</h1>
            <p class="subtitle">{prompt}</p>
        </header>
        
        <main class="content">
            <div class="card">
                <h2>🚀 Deployed on Netlify</h2>
                <p>This project is ready for instant deployment with Netlify Deploy Previews.</p>
            </div>
            
            <div class="card">
                <h2>✨ Features</h2>
                <ul>
                    <li>Serverless Functions Ready</li>
                    <li>Responsive Design</li>
                    <li>Modern UI</li>
                </ul>
            </div>
        </main>
        
        <footer class="footer">
            <p>Generated by Code Weaver | Powered by Netlify</p>
        </footer>
    </div>
    
    <script src="app.js"></script>
</body>
</html>"""
    
    def _get_fallback_css(self) -> str:
        """Generate fallback CSS"""
        return """* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
}

.container {
    max-width: 800px;
    width: 100%;
}

.header {
    text-align: center;
    color: white;
    margin-bottom: 40px;
}

.header h1 {
    font-size: 3rem;
    margin-bottom: 10px;
    animation: fadeInDown 0.8s ease;
}

.subtitle {
    font-size: 1.2rem;
    opacity: 0.9;
}

.content {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    margin-bottom: 40px;
}

.card {
    background: white;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
    animation: fadeInUp 0.8s ease;
}

.card h2 {
    font-size: 1.5rem;
    margin-bottom: 15px;
    color: #333;
}

.card p {
    color: #666;
    line-height: 1.6;
}

.card ul {
    list-style: none;
    padding: 0;
}

.card li {
    padding: 10px 0;
    color: #555;
    border-bottom: 1px solid #eee;
}

.card li:last-child {
    border-bottom: none;
}

.footer {
    text-align: center;
    color: white;
    opacity: 0.8;
}

@keyframes fadeInDown {
    from {
        opacity: 0;
        transform: translateY(-20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@media (max-width: 768px) {
    .header h1 {
        font-size: 2rem;
    }
    
    .content {
        grid-template-columns: 1fr;
    }
}"""
    
    def _get_fallback_js(self) -> str:
        """Generate fallback JavaScript"""
        return """// Code Weaver - Netlify Project
console.log('🚀 Netlify project loaded successfully!');

// Add smooth scroll behavior
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

// Log deployment info
console.log('Deployed on Netlify with instant Deploy Previews');
console.log('Environment:', window.location.hostname);
"""

    
    
    def _get_industry_hints(self, website_type: str) -> str:
        """Get industry-specific component hints for the AI"""
        hints = {
            "law_firm": "- Practice areas grid\n   - Attorney bios with credentials\n   - Case results/testimonials\n   - Free consultation CTA",
            "gym": "- Class schedule grid\n   - Membership pricing (3-tier)\n   - Trainer profiles\n   - Before/after transformations",
            "restaurant": "- Menu preview with prices\n   - Online reservation form\n   - Photo gallery of dishes\n   - Hours and location map",
            "consultant_coaching": "- Methodology/process (4 steps)\n   - Client testimonials with photos\n   - Booking calendar/form\n   - Lead magnet (free resource)",
            "saas": "- Feature comparison table\n   - Pricing tiers (3 plans, highlight middle)\n   - Demo video or screenshots\n   - API documentation link",
            "medical_clinic": "- Services offered\n   - Doctor profiles with specialties\n   - Online appointment booking\n   - Patient portal login",
            "real_estate": "- Featured properties grid\n   - Agent profiles\n   - Search filters\n   - Mortgage calculator",
            "ecommerce": "- Product showcase grid\n   - Featured/bestsellers\n   - Shopping cart icon\n   - Trust badges"
        }
        return hints.get(website_type, "- Relevant service/product showcase\n   - Trust indicators\n   - Clear value proposition")

    def _analyze_prompt_for_fallback(self, prompt: str) -> Dict[str, Any]:
        """Analyze prompt to determine what type of website to generate as fallback"""
        prompt_lower = prompt.lower()
        
        # Detect business type with MORE specificity
        business_type = "general"
        if any(word in prompt_lower for word in ["restaurant", "cafe", "coffee", "food", "dining", "bar", "bistro"]):
            business_type = "restaurant"
        elif any(word in prompt_lower for word in ["renovation", "construction", "remodeling", "contractor", "builder", "flooring", "roofing"]):
            business_type = "renovation"
        elif any(word in prompt_lower for word in ["portfolio", "designer", "photographer", "artist", "creative", "gallery"]):
            business_type = "portfolio"
        elif any(word in prompt_lower for word in ["shop", "store", "ecommerce", "e-commerce", "product", "buy", "sell", "cart"]):
            business_type = "ecommerce"
        elif any(word in prompt_lower for word in ["tech", "software", "saas", "app", "startup", "platform", "api"]):
            business_type = "tech"
        elif any(word in prompt_lower for word in ["landing", "marketing", "agency", "consulting"]):
            business_type = "landing"
        elif any(word in prompt_lower for word in ["blog", "article", "news", "magazine"]):
            business_type = "blog"
        elif any(word in prompt_lower for word in ["fitness", "gym", "health", "wellness", "yoga"]):
            business_type = "fitness"
        
        # Extract business name if mentioned - ENHANCED extraction
        business_name = None
        import re
        
        # Try multiple patterns in order of specificity
        patterns = [
            r'called\s+"([^"]+)"',  # called "Name"
            r'named\s+"([^"]+)"',  # named "Name"
            r'for\s+"([^"]+)"',  # for "Name"
            r'"([A-Z][A-Za-z0-9\s&\'-]{2,40}?)"\s*(?:website|business|company|platform)',  # "Name" website
            r'(?:create|build|make|generate).*?(?:for|called|named)\s+([A-Z][A-Za-z0-9\s&\'-]{2,40}?)(?:\s+that|\s+with|\s+which|\s*[,.])',  # create for Name
            r'website.*?(?:for|called|named)\s+([A-Z][A-Za-z0-9\s&\'-]{2,40}?)(?:\s+that|\s+with|\s+which|\s*[,.])',  # website for Name
        ]
        
        for pattern in patterns:
            match = re.search(pattern, prompt)
            if match:
                business_name = match.group(1).strip()
                # Clean up common artifacts
                business_name = business_name.rstrip(',. ')
                break
        
        # If no name found, extract from context or use business type
        if not business_name:
            # Try to find ANY capitalized words that might be a name
            cap_words = re.findall(r'\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)\b', prompt)
            if cap_words and len(cap_words[0]) > 2:
                business_name = cap_words[0]
            else:
                business_name = f"Professional {business_type.title()}"
        
        # Detect required sections with MORE keywords
        sections = []
        if any(word in prompt_lower for word in ["about", "who we are", "our story"]):
            sections.append("about")
        if any(word in prompt_lower for word in ["service", "what we do", "offerings", "solutions"]):
            sections.append("services")
        if any(word in prompt_lower for word in ["contact", "get in touch", "reach us", "email", "phone"]):
            sections.append("contact")
        if any(word in prompt_lower for word in ["portfolio", "work", "projects", "gallery", "showcase"]):
            sections.append("portfolio")
        if any(word in prompt_lower for word in ["team", "our team", "staff", "people"]):
            sections.append("team")
        if any(word in prompt_lower for word in ["testimonial", "review", "feedback", "client"]):
            sections.append("testimonials")
        if any(word in prompt_lower for word in ["pricing", "price", "plans", "packages"]):
            sections.append("pricing")
        if any(word in prompt_lower for word in ["blog", "news", "articles"]):
            sections.append("blog")
        
        # Default sections if none detected
        if not sections:
            sections = ["about", "services", "contact"]
        
        # Extract color preferences if mentioned
        colors = []
        if "blue" in prompt_lower:
            colors.append("blue")
        if "green" in prompt_lower:
            colors.append("green")
        if "red" in prompt_lower:
            colors.append("red")
        if "purple" in prompt_lower:
            colors.append("purple")
        if "modern" in prompt_lower or "contemporary" in prompt_lower:
            colors.append("modern")
        
        return {
            "business_type": business_type,
            "business_name": business_name,
            "sections": sections,
            "style": "modern",
            "colors": colors,
            "full_prompt": prompt  # Keep full prompt for reference
        }
    
    def _generate_smart_fallback(self, prompt: str, analysis: Dict) -> Dict[str, Any]:
        """Generate an intelligent, customized fallback based on prompt analysis"""
        business_type = analysis.get("business_type", "general")
        business_name = analysis.get("business_name", "Your Business")
        sections = analysis.get("sections", ["about", "services", "contact"])
        
        logger.info(f"🎨 Generating smart fallback: {business_type} for '{business_name}'")
        
        # Get contextual visuals for fallback
        from image_provider import ImageProvider
        image_provider = ImageProvider()
        hero_bg = image_provider.get_hero_background(business_type)
        section_bgs = image_provider.get_section_backgrounds(business_type, count=4)
        
        # Generate customized HTML based on business type
        html = self._generate_customized_html(business_type, business_name, sections, prompt, hero_bg, section_bgs)
        css = self._generate_modern_css()
        js = self._generate_interactive_js()
        
        return {
            "files": {
                "index.html": html,
                "styles.css": css,
                "app.js": js,
                "netlify.toml": self._generate_netlify_toml()
            },
            "deploy_config": {
                "build_command": "",
                "publish_dir": ".",
                "functions_dir": "netlify/functions"
            }
        }
    
    def _generate_customized_html(self, business_type: str, business_name: str, sections: List[str], prompt: str, hero_bg: Dict = None, section_bgs: List[Dict] = None) -> str:
        """Generate customized HTML based on business type using advanced design library"""
        from advanced_design_library import COLOR_SCHEMES, ICON_LIBRARY
        import random
        
        # Default visuals if not provided
        if not hero_bg:
            from image_provider import ImageProvider
            img_provider = ImageProvider()
            hero_bg = img_provider.get_hero_background(business_type)
        if not section_bgs:
            from image_provider import ImageProvider
            img_provider = ImageProvider()
            section_bgs = img_provider.get_section_backgrounds(business_type, count=4)
        
        # Select premium color scheme based on business type
        color_map = {
            "fitness": "health_wellness",
            "restaurant": "creative_vibrant", 
            "tech": "modern_tech",
            "business": "business_professional",
            "portfolio": "creative_vibrant",
            "renovation": "business_professional",
        }
        color_category = color_map.get(business_type, "modern_tech")
        colors = random.choice(COLOR_SCHEMES.get(color_category, COLOR_SCHEMES["modern_tech"]))
        primary_color = colors["colors"][0]
        secondary_color = colors["colors"][1]
        
        # Get contextual icons
        icons = ICON_LIBRARY.get(business_type, ICON_LIBRARY["business"])
        
        # Business-specific content
        if business_type == "renovation":
            hero_title = f"{business_name}"
            hero_subtitle = "Professional Renovation Services"
            services_list = [
                {"icon": "fa-hammer", "title": "Flooring", "desc": "Professional flooring installation"},
                {"icon": "fa-bath", "title": "Bathrooms", "desc": "Complete bathroom remodeling"},
                {"icon": "fa-kitchen-set", "title": "Kitchens", "desc": "Modern kitchen renovations"},
                {"icon": "fa-house-chimney", "title": "Full Houses", "desc": "Whole home renovations"}
            ]
        elif business_type == "restaurant":
            hero_title = f"{business_name}"
            hero_subtitle = "Delicious Food, Amazing Experience"
            services_list = [
                {"icon": "fa-utensils", "title": "Fine Dining", "desc": "Gourmet cuisine"},
                {"icon": "fa-mug-hot", "title": "Beverages", "desc": "Coffee and drinks"},
                {"icon": "fa-birthday-cake", "title": "Desserts", "desc": "Sweet treats"},
                {"icon": "fa-truck", "title": "Delivery", "desc": "Fast delivery service"}
            ]
        elif business_type == "tech":
            hero_title = f"{business_name}"
            hero_subtitle = "Innovative Technology Solutions"
            services_list = [
                {"icon": "fa-code", "title": "Development", "desc": "Custom software development"},
                {"icon": "fa-mobile-screen", "title": "Mobile Apps", "desc": "iOS and Android apps"},
                {"icon": "fa-cloud", "title": "Cloud Services", "desc": "Scalable cloud solutions"},
                {"icon": "fa-shield", "title": "Security", "desc": "Enterprise security"}
            ]
        elif business_type == "portfolio":
            hero_title = f"{business_name}"
            hero_subtitle = "Creative Professional"
            services_list = [
                {"icon": "fa-palette", "title": "Design", "desc": "Creative design work"},
                {"icon": "fa-camera", "title": "Photography", "desc": "Professional photos"},
                {"icon": "fa-video", "title": "Video", "desc": "Video production"},
                {"icon": "fa-pen-nib", "title": "Branding", "desc": "Brand identity"}
            ]
        elif business_type == "ecommerce":
            hero_title = f"{business_name}"
            hero_subtitle = "Shop Quality Products Online"
            services_list = [
                {"icon": "fa-shopping-cart", "title": "Shop", "desc": "Browse our collection"},
                {"icon": "fa-truck", "title": "Fast Shipping", "desc": "Quick delivery"},
                {"icon": "fa-shield", "title": "Secure", "desc": "Safe payments"},
                {"icon": "fa-headset", "title": "Support", "desc": "24/7 customer service"}
            ]
        elif business_type == "fitness":
            hero_title = f"{business_name}"
            hero_subtitle = "Transform Your Body & Mind"
            services_list = [
                {"icon": "fa-dumbbell", "title": "Training", "desc": "Personal training sessions"},
                {"icon": "fa-heart-pulse", "title": "Cardio", "desc": "Cardio workouts"},
                {"icon": "fa-spa", "title": "Wellness", "desc": "Mind & body wellness"},
                {"icon": "fa-users", "title": "Classes", "desc": "Group fitness classes"}
            ]
        elif business_type == "blog":
            hero_title = f"{business_name}"
            hero_subtitle = "Stories, Insights & Ideas"
            services_list = [
                {"icon": "fa-newspaper", "title": "Articles", "desc": "Latest blog posts"},
                {"icon": "fa-rss", "title": "Subscribe", "desc": "Get updates"},
                {"icon": "fa-comments", "title": "Community", "desc": "Join discussions"},
                {"icon": "fa-bookmark", "title": "Save", "desc": "Bookmark favorites"}
            ]
        elif business_type == "landing":
            hero_title = f"{business_name}"
            hero_subtitle = "Solutions That Drive Results"
            services_list = [
                {"icon": "fa-rocket", "title": "Fast", "desc": "Quick implementation"},
                {"icon": "fa-chart-line", "title": "Growth", "desc": "Proven results"},
                {"icon": "fa-shield", "title": "Secure", "desc": "Enterprise security"},
                {"icon": "fa-headset", "title": "Support", "desc": "24/7 assistance"}
            ]
        else:
            # Extract key words from prompt for generic case
            hero_title = f"{business_name}"
            hero_subtitle = "Professional Services You Can Trust"
            
            # Try to extract specific services from prompt
            prompt_lower = prompt.lower()
            detected_services = []
            
            if "website" in prompt_lower or "web" in prompt_lower:
                detected_services.append({"icon": "fa-globe", "title": "Web Solutions", "desc": "Professional web services"})
            if "design" in prompt_lower:
                detected_services.append({"icon": "fa-palette", "title": "Design", "desc": "Creative design services"})
            if "consulting" in prompt_lower or "advice" in prompt_lower:
                detected_services.append({"icon": "fa-lightbulb", "title": "Consulting", "desc": "Expert consulting"})
            if "marketing" in prompt_lower:
                detected_services.append({"icon": "fa-bullhorn", "title": "Marketing", "desc": "Marketing solutions"})
            
            # Use detected services or defaults
            if detected_services:
                services_list = detected_services
            else:
                services_list = [
                    {"icon": "fa-star", "title": "Quality", "desc": "High-quality service"},
                    {"icon": "fa-users", "title": "Team", "desc": "Expert professionals"},
                    {"icon": "fa-clock", "title": "Fast", "desc": "Quick turnaround"},
                    {"icon": "fa-check", "title": "Reliable", "desc": "Dependable results"}
                ]
        
        # Build services HTML
        services_html = ""
        for service in services_list:
            services_html += f'''
                <div class="service-card">
                    <i class="fas {service['icon']} service-icon"></i>
                    <h3>{service['title']}</h3>
                    <p>{service['desc']}</p>
                </div>'''
        
        # Build navigation based on sections
        nav_items = []
        if "about" in sections:
            nav_items.append('<a href="#about">About</a>')
        if "services" in sections:
            nav_items.append('<a href="#services">Services</a>')
        if "portfolio" in sections:
            nav_items.append('<a href="#portfolio">Portfolio</a>')
        if "team" in sections:
            nav_items.append('<a href="#team">Team</a>')
        if "testimonials" in sections:
            nav_items.append('<a href="#testimonials">Testimonials</a>')
        if "contact" in sections:
            nav_items.append('<a href="#contact">Contact</a>')
        
        nav_html = '\n                '.join(nav_items)
        
        # Build sections HTML
        sections_html = ""
        
        if "about" in sections:
            about_bg = section_bgs[0] if section_bgs else {"gradient": "linear-gradient(135deg, #667eea, #764ba2)", "icon": "fa-star"}
            sections_html += f'''
        <section id="about" class="section">
            <div class="container">
                <h2 class="section-title">About Us</h2>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; align-items: center; margin-top: 2rem;">
                    <div>
                        <p class="section-text">We are dedicated professionals committed to delivering exceptional results. Our team brings years of experience and expertise to every project.</p>
                    </div>
                    <div style="{about_bg['css']} border-radius: 20px; padding: 4rem; display: flex; align-items: center; justify-center; min-height: 400px; box-shadow: 0 20px 50px rgba(0,0,0,0.2);">
                        <i class="fas {about_bg['icon']}" style="font-size: 12rem; color: white; opacity: 0.9;"></i>
                    </div>
                </div>
            </div>
        </section>'''
        
        if "services" in sections:
            sections_html += f'''
        <section id="services" class="section section-alt">
            <div class="container">
                <h2 class="section-title">Our Services</h2>
                <div class="services-grid">
                    {services_html}
                </div>
            </div>
        </section>'''
        
        if "contact" in sections:
            sections_html += f'''
        <section id="contact" class="section">
            <div class="container">
                <h2 class="section-title">Get In Touch</h2>
                <form class="contact-form">
                    <input type="text" placeholder="Your Name" required>
                    <input type="email" placeholder="Your Email" required>
                    <textarea placeholder="Your Message" rows="5" required></textarea>
                    <button type="submit" class="cta-button">Send Message</button>
                </form>
            </div>
        </section>'''
        
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{business_name}</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <div class="nav-brand">{business_name}</div>
            <div class="nav-links">
                {nav_html}
            </div>
        </div>
    </nav>

    <header class="hero" style="{hero_bg['css']}">
        <div class="hero-icon-bg">
            <i class="fas {hero_bg['icon']}"></i>
        </div>
        <div class="hero-content">
            <div class="hero-icon-main">
                <i class="fas {hero_bg['icon']}"></i>
            </div>
            <h1 class="hero-title">{hero_title}</h1>
            <p class="hero-subtitle">{hero_subtitle}</p>
            <button class="cta-button" onclick="document.getElementById('services').scrollIntoView({{behavior:'smooth'}})">Get Started</button>
        </div>
    </header>

    {sections_html}

    <footer class="footer">
        <div class="container">
            <p>&copy; 2025 {business_name}. All rights reserved.</p>
        </div>
    </footer>

    <script src="app.js"></script>
</body>
</html>'''
    
    def _generate_modern_css(self) -> str:
        """Generate ultra-modern, comprehensive CSS with advanced effects"""
        return '''/* ═══════════════════════════════════════════════════════════════
   ULTRA-MODERN CSS WITH ADVANCED DESIGN FEATURES
   ═══════════════════════════════════════════════════════════════ */

/* CSS Custom Properties - Rich Color Palette */
:root {
    --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    --hero-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
    --accent-gradient: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
    --dark-gradient: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    
    --color-primary: #667eea;
    --color-secondary: #764ba2;
    --color-accent: #f093fb;
    --color-success: #10b981;
    --color-warning: #f59e0b;
    --color-danger: #ef4444;
    
    --font-heading: 'Playfair Display', 'Georgia', serif;
    --font-body: 'Poppins', 'Inter', -apple-system, sans-serif;
    
    --shadow-sm: 0 2px 8px rgba(0,0,0,0.1);
    --shadow-md: 0 4px 16px rgba(0,0,0,0.15);
    --shadow-lg: 0 8px 32px rgba(0,0,0,0.2);
    --shadow-xl: 0 20px 60px rgba(0,0,0,0.3);
    --shadow-glow: 0 0 40px rgba(102, 126, 234, 0.4);
    
    --glass-bg: rgba(255, 255, 255, 0.1);
    --glass-border: rgba(255, 255, 255, 0.2);
}

/* Reset & Base Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
    overflow-x: hidden;
}

body {
    font-family: var(--font-body);
    line-height: 1.7;
    color: #2d3748;
    background: linear-gradient(180deg, #f7fafc 0%, #edf2f7 100%);
    overflow-x: hidden;
}

.container {
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 2rem;
}

/* Advanced Typography */
h1, h2, h3, h4, h5, h6 {
    font-family: var(--font-heading);
    font-weight: 800;
    line-height: 1.2;
    margin-bottom: 1rem;
}

h1 { font-size: clamp(2.5rem, 6vw, 5rem); }
h2 { font-size: clamp(2rem, 5vw, 4rem); }
h3 { font-size: clamp(1.5rem, 4vw, 3rem); }

/* ═══════════════════════════════════════════════════════════════
   NAVIGATION - Modern Glassmorphism
   ═══════════════════════════════════════════════════════════════ */
.navbar {
    background: var(--glass-bg);
    backdrop-filter: blur(20px) saturate(180%);
    border-bottom: 1px solid var(--glass-border);
    padding: 1.5rem 0;
    position: fixed;
    width: 100%;
    top: 0;
    z-index: 1000;
    box-shadow: var(--shadow-md);
    transition: all 0.3s ease;
}

.navbar.scrolled {
    padding: 1rem 0;
    background: rgba(102, 126, 234, 0.95);
    backdrop-filter: blur(20px);
    box-shadow: var(--shadow-lg);
}

.navbar .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.nav-brand {
    color: white;
    font-size: 1.5rem;
    font-weight: 700;
}

.nav-links {
    display: flex;
    gap: 2rem;
}

.nav-links a {
    color: white;
    text-decoration: none;
    font-weight: 500;
    transition: opacity 0.3s;
}

.nav-links a:hover {
    opacity: 0.8;
}

/* Hero Section */
.hero {
    position: relative;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 150px 20px 100px;
    text-align: center;
    margin-top: 60px;
    min-height: 600px;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
}

.hero-icon-bg {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0.1;
    z-index: 1;
}

.hero-icon-bg i {
    font-size: 40rem;
    color: white;
}

.hero-icon-main {
    margin-bottom: 2rem;
}

.hero-icon-main i {
    font-size: 8rem;
    color: white;
    opacity: 0.9;
}

.hero-content {
    position: relative;
    z-index: 2;
    max-width: 800px;
    margin: 0 auto;
}

.hero-title {
    font-size: 3.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
    animation: fadeInUp 0.8s ease;
}

.hero-subtitle {
    font-size: 1.5rem;
    margin-bottom: 2rem;
    opacity: 0.9;
    animation: fadeInUp 0.8s ease 0.2s both;
}

.cta-button {
    background: white;
    color: #667eea;
    padding: 1rem 3rem;
    border: none;
    border-radius: 50px;
    font-size: 1.1rem;
    font-weight: 600;
    cursor: pointer;
    transition: transform 0.3s, box-shadow 0.3s;
    animation: fadeInUp 0.8s ease 0.4s both;
}

.cta-button:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}

/* Sections */
.section {
    padding: 80px 20px;
}

.section-alt {
    background: #f8f9fa;
}

.section-title {
    text-align: center;
    font-size: 2.5rem;
    margin-bottom: 3rem;
    color: #2d3748;
}

.section-text {
    text-align: center;
    font-size: 1.2rem;
    max-width: 700px;
    margin: 0 auto;
    color: #4a5568;
    line-height: 1.8;
}

/* Services Grid */
.services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.service-card {
    background: white;
    padding: 2rem;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 5px 20px rgba(0,0,0,0.08);
    transition: transform 0.3s, box-shadow 0.3s;
}

.service-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 40px rgba(0,0,0,0.15);
}

.service-icon {
    font-size: 3rem;
    color: #667eea;
    margin-bottom: 1rem;
}

.service-card h3 {
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
    color: #2d3748;
}

.service-card p {
    color: #718096;
}

/* Contact Form */
.contact-form {
    max-width: 600px;
    margin: 0 auto;
}

.contact-form input,
.contact-form textarea {
    width: 100%;
    padding: 1rem;
    margin-bottom: 1rem;
    border: 2px solid #e2e8f0;
    border-radius: 8px;
    font-family: inherit;
    font-size: 1rem;
    transition: border-color 0.3s;
}

.contact-form input:focus,
.contact-form textarea:focus {
    outline: none;
    border-color: #667eea;
}

.contact-form button {
    width: 100%;
}

/* Footer */
.footer {
    background: #2d3748;
    color: white;
    text-align: center;
    padding: 2rem;
}

/* ═══════════════════════════════════════════════════════════════
   ADVANCED ANIMATIONS & KEYFRAMES
   ═══════════════════════════════════════════════════════════════ */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(50px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeInDown {
    from {
        opacity: 0;
        transform: translateY(-50px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes float {
    0%, 100% {
        transform: translateY(0px);
    }
    50% {
        transform: translateY(-20px);
    }
}

@keyframes pulse {
    0%, 100% {
        opacity: 1;
        transform: scale(1);
    }
    50% {
        opacity: 0.8;
        transform: scale(1.05);
    }
}

@keyframes glow {
    0%, 100% {
        box-shadow: 0 0 20px rgba(102, 126, 234, 0.3);
    }
    50% {
        box-shadow: 0 0 40px rgba(102, 126, 234, 0.6), 0 0 60px rgba(118, 75, 162, 0.4);
    }
}

@keyframes slideInLeft {
    from {
        opacity: 0;
        transform: translateX(-100px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes slideInRight {
    from {
        opacity: 0;
        transform: translateX(100px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes rotate {
    from {
        transform: rotate(0deg);
    }
    to {
        transform: rotate(360deg);
    }
}

@keyframes gradient-shift {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}

/* Utility Animation Classes */
.animate-float {
    animation: float 3s ease-in-out infinite;
}

.animate-pulse {
    animation: pulse 2s ease-in-out infinite;
}

.animate-glow {
    animation: glow 2s ease-in-out infinite;
}

/* ═══════════════════════════════════════════════════════════════
   GLASSMORPHISM UTILITIES
   ═══════════════════════════════════════════════════════════════ */
.glass {
    background: var(--glass-bg);
    backdrop-filter: blur(16px) saturate(180%);
    border: 1px solid var(--glass-border);
    border-radius: 20px;
}

.glass-strong {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(20px) saturate(200%);
    border: 1px solid rgba(255, 255, 255, 0.3);
}

/* ═══════════════════════════════════════════════════════════════
   GRADIENT TEXT UTILITIES
   ═══════════════════════════════════════════════════════════════ */
.text-gradient {
    background: var(--primary-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.text-gradient-secondary {
    background: var(--secondary-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

/* ═══════════════════════════════════════════════════════════════
   RESPONSIVE DESIGN
   ═══════════════════════════════════════════════════════════════ */
@media (max-width: 1024px) {
    .container {
        padding: 0 1.5rem;
    }
    
    h1 { font-size: clamp(2rem, 5vw, 3.5rem); }
    h2 { font-size: clamp(1.75rem, 4vw, 3rem); }
}

@media (max-width: 768px) {
    .hero {
        min-height: 80vh;
        padding: 8rem 0 4rem;
    }
    
    .hero-title {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    
    .hero-subtitle {
        font-size: 1.2rem;
    }
    
    .nav-links {
        gap: 1rem;
        font-size: 0.9rem;
    }
    
    .services-grid {
        grid-template-columns: 1fr;
        gap: 1.5rem;
    }
    
    .service-card {
        padding: 1.5rem;
    }
    
    .service-icon {
        font-size: 2.5rem;
    }
}

@media (max-width: 480px) {
    .hero-title {
        font-size: 2rem;
    }
    
    .cta-button {
        padding: 0.9rem 2rem;
        font-size: 1rem;
    }
    
    .container {
        padding: 0 1rem;
    }
}

/* ═══════════════════════════════════════════════════════════════
   SCROLL EFFECTS & PERFORMANCE
   ═══════════════════════════════════════════════════════════════ */
.parallax {
    background-attachment: fixed;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
}

.fade-in-section {
    opacity: 0;
    transform: translateY(30px);
    transition: opacity 0.6s ease-out, transform 0.6s ease-out;
}

.fade-in-section.is-visible {
    opacity: 1;
    transform: translateY(0);
}

/* Performance Optimizations */
.will-change-transform {
    will-change: transform;
}

.gpu-accelerated {
    transform: translateZ(0);
    backface-visibility: hidden;
    perspective: 1000px;
}'''
    
    def _ensure_design_quality(self, project_data: Dict, prompt: str) -> Dict:
        """
        CRITICAL: Ensure generated HTML has proper design frameworks
        Adds CDN links if missing, validates CSS exists and is substantial
        """
        files = project_data.get("files", {})
        html = files.get("index.html", "")
        css = files.get("styles.css", "")
        js = files.get("app.js", "")
        
        logger.info("🎨 Validating design quality...")
        
        # Check if HTML has required CDN links
        has_tailwind = "cdn.tailwindcss.com" in html
        has_fontawesome = "font-awesome" in html
        has_animate = "animate.css" in html
        has_google_fonts = "fonts.googleapis.com" in html or "fonts.google.com" in html
        has_aos = "aos" in html.lower()
        has_css_link = 'href="styles.css"' in html or "href='styles.css'" in html
        has_js_link = 'src="app.js"' in html or "src='app.js'" in html
        
        logger.info(f"   Tailwind CDN: {'✅' if has_tailwind else '❌'}")
        logger.info(f"   Font Awesome: {'✅' if has_fontawesome else '❌'}")
        logger.info(f"   Animate.css: {'✅' if has_animate else '❌'}")
        logger.info(f"   Google Fonts: {'✅' if has_google_fonts else '❌'}")
        logger.info(f"   AOS Library: {'✅' if has_aos else '❌'}")
        logger.info(f"   CSS Link: {'✅' if has_css_link else '❌'}")
        logger.info(f"   JS Link: {'✅' if has_js_link else '❌'}")
        logger.info(f"   CSS Size: {len(css)} chars")
        logger.info(f"   JS Size: {len(js)} chars")
        
        # If HTML is missing critical design frameworks, enhance it
        if not has_tailwind or not has_fontawesome or not has_animate or not has_google_fonts or not has_aos or not has_css_link:
            logger.warning("⚠️ HTML missing design frameworks - enhancing...")
            html = self._enhance_html_with_frameworks(html)
            files["index.html"] = html
            logger.info("✅ Enhanced HTML with CDN links")
        
        # If CSS is too small or missing, generate proper CSS
        if len(css) < 1000:
            logger.warning(f"⚠️ CSS too small ({len(css)} chars) - generating comprehensive CSS...")
            css = self._generate_modern_css()
            files["styles.css"] = css
            logger.info(f"✅ Generated comprehensive CSS ({len(css)} chars)")
        
        # If JS is missing or too small, generate proper JS
        if len(js) < 200:
            logger.warning(f"⚠️ JS too small ({len(js)} chars) - generating interactive JS...")
            js = self._generate_interactive_js()
            files["app.js"] = js
            logger.info(f"✅ Generated interactive JS ({len(js)} chars)")
        
        project_data["files"] = files
        return project_data
    
    def _enhance_html_with_frameworks(self, html: str) -> str:
        """Add missing CDN links and framework references to HTML"""
        
        # Define ALL the CDN links that MUST be present for stunning design
        tailwind_cdn = '<script src="https://cdn.tailwindcss.com"></script>'
        fontawesome_cdn = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">'
        animate_css = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css">'
        google_fonts = '<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Playfair+Display:wght@700;800&display=swap" rel="stylesheet">'
        aos_css = '<link rel="stylesheet" href="https://unpkg.com/aos@2.3.1/dist/aos.css">'
        css_link = '<link rel="stylesheet" href="styles.css">'
        aos_js = '<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>'
        js_link = '<script src="app.js"></script>'
        
        # Find the </head> tag and add links before it
        if '</head>' in html:
            # Build the links to add
            links_to_add = []
            
            if 'cdn.tailwindcss.com' not in html:
                links_to_add.append(tailwind_cdn)
            if 'font-awesome' not in html:
                links_to_add.append(fontawesome_cdn)
            if 'animate.css' not in html:
                links_to_add.append(animate_css)
            if 'fonts.googleapis.com' not in html and 'fonts.google.com' not in html:
                links_to_add.append(google_fonts)
            if 'aos' not in html.lower() and 'aos.css' not in html:
                links_to_add.append(aos_css)
            if 'styles.css' not in html:
                links_to_add.append(css_link)
            
            # Add all links before </head>
            if links_to_add:
                links_html = '\n    ' + '\n    '.join(links_to_add) + '\n    '
                html = html.replace('</head>', f'{links_html}</head>')
            
            # Add JS libraries before </body> if missing
            scripts_to_add = []
            if 'aos.js' not in html.lower() and 'aos' not in html.lower():
                scripts_to_add.append(aos_js)
            if 'app.js' not in html:
                scripts_to_add.append(js_link)
            
            if scripts_to_add and '</body>' in html:
                scripts_html = '\n    ' + '\n    '.join(scripts_to_add) + '\n'
                html = html.replace('</body>', f'{scripts_html}</body>')
        else:
            # HTML is malformed - wrap it with proper structure
            logger.warning("⚠️ HTML missing <head> tag - creating proper structure with ALL design libraries")
            html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Website</title>
    {tailwind_cdn}
    {fontawesome_cdn}
    {animate_css}
    {google_fonts}
    {aos_css}
    {css_link}
</head>
<body>
{html}
    {aos_js}
    {js_link}
</body>
</html>"""
        
        return html
    
    def _generate_interactive_js(self) -> str:
        """Generate comprehensive interactive JavaScript with AOS and advanced features"""
        return '''// ═══════════════════════════════════════════════════════════════
// ULTRA-INTERACTIVE JAVASCRIPT - NO ALERT POPUPS!
// ═══════════════════════════════════════════════════════════════

// 🚨 CRITICAL: NEVER USE alert() - Use inline messages instead!

// Initialize AOS (Animate On Scroll) Library
if (typeof AOS !== 'undefined') {
    AOS.init({
        duration: 1000,
        easing: 'ease-in-out-cubic',
        once: false,
        mirror: true,
        offset: 100,
        delay: 100,
        anchorPlacement: 'top-bottom'
    });
}

// ═══════════════════════════════════════════════════════════════
// SMOOTH SCROLLING
// ═══════════════════════════════════════════════════════════════
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ 
                behavior: 'smooth', 
                block: 'start'
            });
        }
    });
});

// ═══════════════════════════════════════════════════════════════
// NAVBAR SCROLL EFFECT
// ═══════════════════════════════════════════════════════════════
const navbar = document.querySelector('.navbar');
let lastScroll = 0;

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    
    // Add scrolled class for styling
    if (currentScroll > 50) {
        navbar?.classList.add('scrolled');
    } else {
        navbar?.classList.remove('scrolled');
    }
    
    // Hide/show navbar on scroll
    if (currentScroll > lastScroll && currentScroll > 500) {
        navbar?.style.transform = 'translateY(-100%)';
    } else {
        navbar?.style.transform = 'translateY(0)';
    }
    
    lastScroll = currentScroll;
});

// ═══════════════════════════════════════════════════════════════
// FORM HANDLING WITH VALIDATION
// ═══════════════════════════════════════════════════════════════
const forms = document.querySelectorAll('form');
forms.forEach(form => {
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Add loading state
        const submitBtn = this.querySelector('[type="submit"]');
        const originalText = submitBtn?.textContent;
        if (submitBtn) {
            submitBtn.textContent = 'Sending...';
            submitBtn.disabled = true;
        }
        
        // Simulate form submission
        setTimeout(() => {
            if (submitBtn) {
                submitBtn.textContent = '✓ Sent!';
                submitBtn.style.background = 'linear-gradient(135deg, #10b981 0%, #059669 100%)';
            }
            
            // Show success message
            const successMsg = document.createElement('div');
            successMsg.className = 'form-success animate__animated animate__fadeInUp';
            successMsg.innerHTML = '<i class="fas fa-check-circle"></i> Thank you! We will get back to you soon.';
            successMsg.style.cssText = 'padding: 1rem; background: #d1fae5; color: #065f46; border-radius: 10px; margin-top: 1rem; text-align: center;';
            this.appendChild(successMsg);
            
            // Reset form
            this.reset();
            
            // Reset button after delay
            setTimeout(() => {
                if (submitBtn) {
                    submitBtn.textContent = originalText || 'Submit';
                    submitBtn.disabled = false;
                    submitBtn.style.background = '';
                }
                successMsg.remove();
            }, 3000);
        }, 1500);
    });
});

// ═══════════════════════════════════════════════════════════════
// COUNTER ANIMATION FOR STATS
// ═══════════════════════════════════════════════════════════════
function animateCounter(element) {
    const target = parseInt(element.getAttribute('data-count') || element.textContent);
    const duration = 2000;
    const increment = target / (duration / 16);
    let current = 0;
    
    const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
            element.textContent = target.toLocaleString();
            clearInterval(timer);
        } else {
            element.textContent = Math.floor(current).toLocaleString();
        }
    }, 16);
}

// Observe stat counters
const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            animateCounter(entry.target);
            counterObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.5 });

document.querySelectorAll('.stat-number, .counter').forEach(counter => {
    counterObserver.observe(counter);
});

// ═══════════════════════════════════════════════════════════════
// INTERSECTION OBSERVER FOR ANIMATIONS
// ═══════════════════════════════════════════════════════════════
const fadeObserverOptions = {
    threshold: 0.15,
    rootMargin: '0px 0px -100px 0px'
};

const fadeObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, fadeObserverOptions);

// Apply to various elements
const elementsToAnimate = [
    '.service-card',
    '.feature-card',
    '.card',
    '.pricing-card',
    '.testimonial',
    'section'
];

elementsToAnimate.forEach(selector => {
    document.querySelectorAll(selector).forEach(element => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(40px)';
        element.style.transition = 'opacity 0.8s ease, transform 0.8s ease';
        fadeObserver.observe(element);
    });
});

// ═══════════════════════════════════════════════════════════════
// PARALLAX EFFECT
// ═══════════════════════════════════════════════════════════════
window.addEventListener('scroll', () => {
    const parallaxElements = document.querySelectorAll('.parallax');
    parallaxElements.forEach(element => {
        const speed = element.getAttribute('data-speed') || 0.5;
        const yPos = -(window.pageYOffset * parseFloat(speed));
        element.style.transform = `translateY(${yPos}px)`;
    });
});

// ═══════════════════════════════════════════════════════════════
// MOBILE MENU TOGGLE
// ═══════════════════════════════════════════════════════════════
const menuToggle = document.querySelector('.menu-toggle');
const navLinks = document.querySelector('.nav-links');

if (menuToggle && navLinks) {
    menuToggle.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        menuToggle.classList.toggle('active');
    });
    
    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.navbar')) {
            navLinks.classList.remove('active');
            menuToggle.classList.remove('active');
        }
    });
}

// ═══════════════════════════════════════════════════════════════
// BUTTON HANDLERS (NO ALERT POPUPS!)
// ═══════════════════════════════════════════════════════════════

// 🚨 CRITICAL: All buttons scroll to sections - NO alert() popups!

// CTA buttons scroll to contact
document.querySelectorAll('.cta-button, .btn-primary, button[data-scroll]').forEach(button => {
    button.addEventListener('click', function(e) {
        e.preventDefault();
        const contactSection = document.getElementById('contact');
        if (contactSection) {
            contactSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});

// Generic buttons - check for data-target attribute
document.querySelectorAll('button:not([type="submit"])').forEach(button => {
    if (!button.hasAttribute('onclick') && !button.closest('form')) {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            // Scroll to contact by default
            const contactSection = document.getElementById('contact');
            if (contactSection) {
                contactSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    }
});

// Add ripple effect to buttons
document.querySelectorAll('button, .btn').forEach(button => {
    button.addEventListener('click', function(e) {
        const ripple = document.createElement('span');
        ripple.classList.add('ripple');
        this.appendChild(ripple);
        
        const rect = this.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        ripple.style.width = ripple.style.height = size + 'px';
        ripple.style.left = e.clientX - rect.left - size/2 + 'px';
        ripple.style.top = e.clientY - rect.top - size/2 + 'px';
        
        setTimeout(() => ripple.remove(), 600);
    });
});

// ═══════════════════════════════════════════════════════════════
// LAZY LOADING IMAGES
// ═══════════════════════════════════════════════════════════════
const imageObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const img = entry.target;
            if (img.dataset.src) {
                img.src = img.dataset.src;
                img.classList.add('loaded');
                imageObserver.unobserve(img);
            }
        }
    });
});

document.querySelectorAll('img[data-src]').forEach(img => {
    imageObserver.observe(img);
});

// ═══════════════════════════════════════════════════════════════
// PAGE LOADED
// ═══════════════════════════════════════════════════════════════
console.log('🚀 Website fully loaded with advanced interactivity!');

console.log('🚀 Website loaded successfully!');'''
    
    def _generate_netlify_toml(self) -> str:
        """Generate netlify.toml configuration"""
        return '''[build]
  publish = "."
  functions = "netlify/functions"

[[redirects]]
  from = "/api/*"
  to = "/.netlify/functions/:splat"
  status = 200'''
    
    def _generate_minimal_viable_project(self, prompt: str) -> Dict[str, Any]:
        """Absolute last resort - generate minimal but functional project"""
        logger.warning("🆘 Generating minimal viable project as last resort")
        
        return {
            "files": {
                "index.html": '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Website</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            text-align: center;
            padding: 20px;
        }
        .container {
            max-width: 800px;
        }
        h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
            animation: fadeIn 1s ease;
        }
        p {
            font-size: 1.3rem;
            opacity: 0.9;
            margin-bottom: 2rem;
            animation: fadeIn 1s ease 0.3s both;
        }
        .button {
            background: white;
            color: #667eea;
            padding: 1rem 2rem;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            display: inline-block;
            animation: fadeIn 1s ease 0.6s both;
            transition: transform 0.3s;
        }
        .button:hover {
            transform: scale(1.05);
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome</h1>
        <p>Your website is being created. This is a placeholder while we finalize the design.</p>
        <a href="#" class="button">Get Started</a>
    </div>
</body>
</html>''',
                "styles.css": "/* Styles embedded in HTML */",
                "app.js": "console.log('Website loaded');",
                "netlify.toml": "[build]\n  publish = \".\""
            },
            "deploy_config": {
                "build_command": "",
                "publish_dir": ".",
                "functions_dir": "netlify/functions"
            }
        }

