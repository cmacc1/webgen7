"""
IMAGE PROVIDER - Contextual Visual Backgrounds for Website Generation
Uses CSS gradients with relevant Font Awesome icons - ALWAYS loads, ALWAYS contextual
"""

import hashlib
from typing import List, Dict

class ImageProvider:
    """Provides contextual visual backgrounds using CSS gradients and icons"""
    
    def __init__(self):
        # Icon and gradient mappings for each website type
        self.visual_themes = {
            "law_firm": {
                "icon": "fa-scale-balanced",
                "gradients": [
                    "linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%)",
                    "linear-gradient(135deg, #1f2937 0%, #4b5563 100%)",
                    "linear-gradient(135deg, #92400e 0%, #d97706 100%)"
                ]
            },
            "consultant_coaching": {
                "icon": "fa-lightbulb",
                "gradients": [
                    "linear-gradient(135deg, #7c3aed 0%, #a78bfa 100%)",
                    "linear-gradient(135deg, #059669 0%, #10b981 100%)",
                    "linear-gradient(135deg, #ea580c 0%, #fb923c 100%)"
                ]
            },
            "gym": {
                "icon": "fa-dumbbell",
                "gradients": [
                    "linear-gradient(135deg, #dc2626 0%, #ef4444 100%)",
                    "linear-gradient(135deg, #1e40af 0%, #3b82f6 100%)",
                    "linear-gradient(135deg, #16a34a 0%, #22c55e 100%)"
                ]
            },
            "restaurant": {
                "icon": "fa-utensils",
                "gradients": [
                    "linear-gradient(135deg, #92400e 0%, #d97706 100%)",
                    "linear-gradient(135deg, #15803d 0%, #22c55e 100%)",
                    "linear-gradient(135deg, #881337 0%, #be123c 100%)"
                ]
            },
            "renovation": {
                "icon": "fa-hammer",
                "gradients": [
                    "linear-gradient(135deg, #854d0e 0%, #ca8a04 100%)",
                    "linear-gradient(135deg, #4b5563 0%, #6b7280 100%)",
                    "linear-gradient(135deg, #92400e 0%, #d97706 100%)"
                ]
            },
            "tech": {
                "icon": "fa-laptop-code",
                "gradients": [
                    "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
                    "linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%)",
                    "linear-gradient(135deg, #0891b2 0%, #06b6d4 100%)"
                ]
            },
            "saas": {
                "icon": "fa-rocket",
                "gradients": [
                    "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
                    "linear-gradient(135deg, #2563eb 0%, #7c3aed 100%)"
                ]
            },
            "medical_clinic": {
                "icon": "fa-stethoscope",
                "gradients": [
                    "linear-gradient(135deg, #0891b2 0%, #06b6d4 100%)",
                    "linear-gradient(135deg, #059669 0%, #10b981 100%)"
                ]
            },
            "dental": {
                "icon": "fa-tooth",
                "gradients": [
                    "linear-gradient(135deg, #0891b2 0%, #06b6d4 100%)",
                    "linear-gradient(135deg, #ffffff 0%, #e0f2fe 100%)"
                ]
            },
            "landscaping": {
                "icon": "fa-tree",
                "gradients": [
                    "linear-gradient(135deg, #15803d 0%, #22c55e 100%)",
                    "linear-gradient(135deg, #166534 0%, #16a34a 100%)"
                ]
            },
            "real_estate": {
                "icon": "fa-building",
                "gradients": [
                    "linear-gradient(135deg, #1e40af 0%, #3b82f6 100%)",
                    "linear-gradient(135deg, #1f2937 0%, #4b5563 100%)"
                ]
            },
            "ecommerce": {
                "icon": "fa-shopping-cart",
                "gradients": [
                    "linear-gradient(135deg, #9333ea 0%, #c026d3 100%)",
                    "linear-gradient(135deg, #db2777 0%, #f472b6 100%)"
                ]
            },
            "default": {
                "icon": "fa-star",
                "gradients": [
                    "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
                    "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)"
                ]
            }
        }
    
    def get_hero_background(self, website_type: str) -> Dict[str, str]:
        """Get hero background - gradient with contextual icon"""
        theme = self.visual_themes.get(website_type, self.visual_themes["default"])
        
        return {
            "gradient": theme["gradients"][0],
            "icon": theme["icon"],
            "css": f"""background: {theme["gradients"][0]};
position: relative;"""
        }
    
    def get_section_backgrounds(self, website_type: str, count: int = 4) -> List[Dict[str, str]]:
        """Get section backgrounds - different gradient variations"""
        theme = self.visual_themes.get(website_type, self.visual_themes["default"])
        backgrounds = []
        
        for i in range(count):
            gradient = theme["gradients"][i % len(theme["gradients"])]
            backgrounds.append({
                "gradient": gradient,
                "icon": theme["icon"],
                "css": f"background: {gradient};"
            })
        
        return backgrounds
    
    def get_hero_html(self, website_type: str, title: str, subtitle: str) -> str:
        """Generate complete hero section HTML with gradient and icon"""
        theme = self.visual_themes.get(website_type, self.visual_themes["default"])
        gradient = theme["gradients"][0]
        icon = theme["icon"]
        
        return f'''<section class="relative min-h-screen flex items-center justify-center overflow-hidden" style="background: {gradient};">
    <div class="absolute inset-0 opacity-10">
        <i class="fas {icon} absolute text-[40rem] text-white" style="top: 50%; left: 50%; transform: translate(-50%, -50%);"></i>
    </div>
    <div class="relative z-10 text-center px-6 max-w-5xl mx-auto">
        <div class="mb-6">
            <i class="fas {icon} text-9xl text-white opacity-90"></i>
        </div>
        <h1 class="text-7xl md:text-9xl font-black text-white mb-6 leading-tight">
            {title}
        </h1>
        <p class="text-2xl md:text-3xl text-white mb-12 opacity-90">
            {subtitle}
        </p>
        <div class="flex gap-6 justify-center flex-wrap">
            <button onclick="document.getElementById('services').scrollIntoView({{behavior:'smooth'}})" class="px-12 py-5 bg-white text-gray-900 rounded-full text-xl font-bold hover:scale-110 transition-transform duration-300 shadow-2xl">
                Get Started
            </button>
            <button onclick="document.getElementById('about').scrollIntoView({{behavior:'smooth'}})" class="px-12 py-5 bg-white bg-opacity-20 backdrop-blur-md text-white border-3 border-white rounded-full text-xl font-bold hover:bg-opacity-30 transition-all">
                Learn More
            </button>
        </div>
    </div>
</section>'''
    
    def get_section_card_html(self, website_type: str, icon: str, title: str, description: str, index: int = 0) -> str:
        """Generate a section card with gradient background"""
        theme = self.visual_themes.get(website_type, self.visual_themes["default"])
        gradient = theme["gradients"][index % len(theme["gradients"])]
        
        return f'''<div class="relative group overflow-hidden rounded-3xl shadow-2xl hover:shadow-3xl hover:-translate-y-2 transition-all duration-300" style="background: {gradient};">
    <div class="p-10 h-full">
        <div class="w-20 h-20 bg-white bg-opacity-20 backdrop-blur-md rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform">
            <i class="fas {icon} text-5xl text-white"></i>
        </div>
        <h3 class="text-3xl font-bold text-white mb-4">{title}</h3>
        <p class="text-white text-lg opacity-90 leading-relaxed">{description}</p>
    </div>
</div>'''
