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
    
    def get_hero_image(self, website_type: str, seed: str = None) -> str:
        """Get a hero image URL (1920x1080)"""
        category = self.category_map.get(website_type, "business")
        image_id = self._get_image_id(category, seed, 0)
        
        # Use specific image ID for reliability
        return f"{self.picsum_base}/id/{image_id}/1920/1080"
    
    def get_section_images(self, website_type: str, count: int = 4, seed: str = None) -> List[str]:
        """Get section images (1200x800)"""
        category = self.category_map.get(website_type, "business")
        images = []
        
        for i in range(count):
            image_id = self._get_image_id(category, seed, i + 1)
            url = f"{self.picsum_base}/id/{image_id}/1200/800"
            images.append(url)
        
        return images
    
    def get_thumbnail_images(self, website_type: str, count: int = 6, seed: str = None) -> List[str]:
        """Get smaller thumbnail images (600x400)"""
        category = self.category_map.get(website_type, "business")
        images = []
        
        for i in range(count):
            image_id = self._get_image_id(category, seed, i + 10)
            url = f"{self.picsum_base}/id/{image_id}/600/400"
            images.append(url)
        
        return images
    
    def _get_image_id(self, category: str, seed: str, index: int) -> int:
        """Get a specific image ID from category"""
        ids = self.curated_ids.get(category, self.curated_ids["business"])
        
        if seed:
            # Use seed to pick a consistent starting point
            hash_val = int(hashlib.md5(f"{seed}_{index}".encode()).hexdigest()[:8], 16)
            base_index = hash_val % len(ids)
        else:
            base_index = index % len(ids)
        
        return ids[base_index]
    
    def get_css_gradient_fallback(self, colors: List[str]) -> str:
        """Generate CSS gradient as image fallback"""
        if len(colors) >= 2:
            return f"background: linear-gradient(135deg, {colors[0]}, {colors[1]});"
        return "background: linear-gradient(135deg, #667eea, #764ba2);"
    
    def generate_image_markup(self, url: str, alt: str, classes: str = "") -> str:
        """Generate proper img tag with fallback"""
        return f'''<img src="{url}" alt="{alt}" class="{classes} object-cover" loading="lazy" onerror="this.style.display='none'; this.parentElement.classList.add('bg-gradient-to-br', 'from-purple-600', 'to-pink-600');">'''
    
    def get_icon_backgrounds(self, count: int = 4) -> List[Dict[str, str]]:
        """Get gradient backgrounds for icon containers (no images)"""
        gradients = [
            {"from": "#667eea", "to": "#764ba2"},
            {"from": "#f093fb", "to": "#f5576c"},
            {"from": "#4facfe", "to": "#00f2fe"},
            {"from": "#43e97b", "to": "#38f9d7"},
            {"from": "#fa709a", "to": "#fee140"},
            {"from": "#30cfd0", "to": "#330867"},
        ]
        
        return [gradients[i % len(gradients)] for i in range(count)]
