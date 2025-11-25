"""
Image/Video Search Service using reliable placeholder and free stock photo services
"""
import httpx
import logging
from typing import List, Dict, Optional
import asyncio
import hashlib
import random

logger = logging.getLogger(__name__)

class ImageSearchService:
    """Service to provide high-quality images using multiple free, reliable sources"""
    
    # Color schemes for contextual images
    COLOR_SCHEMES = {
        'restaurant': ['FF6B35', 'F7931E', 'FDC830'],
        'fitness': ['FF6B6B', '4ECDC4', '45B7D1'],
        'business': ['2C3E50', '3498DB', '95A5A6'],
        'tech': ['667EEA', '764BA2', 'F093FB'],
        'health': ['4FACFE', '00F2FE', '43E97B'],
        'education': ['FA709A', 'FEE140', '30CFD0'],
        'travel': ['38EF7D', '11998E', '0ABFBC'],
        'portfolio': ['833AB4', 'FD1D1D', 'FCB045'],
        'ecommerce': ['F857A6', 'FF5858', 'FCFCFC'],
        'default': ['667EEA', 'F093FB', '4FACFE']
    }
    
    def __init__(self):
        self.timeout = 10
    
    def _detect_category(self, prompt: str) -> str:
        """Detect the category of website from the prompt"""
        prompt_lower = prompt.lower()
        for category in self.COLOR_SCHEMES.keys():
            if category in prompt_lower:
                return category
        return 'default'
    
    def _get_color_from_seed(self, seed: str, index: int = 0) -> str:
        """Generate a consistent color hex from seed"""
        hash_input = f"{seed}_{index}".encode('utf-8')
        hash_value = hashlib.md5(hash_input).hexdigest()[:6]
        return hash_value.upper()
    
    async def search_images(self, query: str, count: int = 4) -> List[Dict[str, str]]:
        """
        Generate contextual placeholder images based on query
        Returns list of image URLs with metadata
        Uses placehold.co - reliable, free, professional-looking placeholders
        """
        try:
            images = []
            
            # Detect category for better color scheme
            category = self._detect_category(query)
            colors = self.COLOR_SCHEMES.get(category, self.COLOR_SCHEMES['default'])
            
            # Clean query for display
            clean_query = query.replace('+', ' ').replace('_', ' ').title()
            
            # Generate multiple image URLs with different colors for variety
            for i in range(count):
                # Cycle through colors
                bg_color = colors[i % len(colors)]
                text_color = 'FFFFFF' if i % 2 == 0 else '000000'
                
                # Using placehold.co with custom colors and text
                url = f"https://placehold.co/1600x900/{bg_color}/{text_color}/png?text={clean_query}+{i+1}"
                images.append({
                    "url": url,
                    "description": f"{clean_query} image {i+1}",
                    "source": "placehold.co",
                    "bg_color": bg_color
                })
            
            logger.info(f"✅ Generated {len(images)} images for query: {query} (category: {category})")
            return images
            
        except Exception as e:
            logger.error(f"❌ Image search error: {str(e)}")
            # Return empty list on error - don't fail generation
            return []
    
    async def get_hero_image(self, keywords: List[str]) -> Optional[str]:
        """
        Get a hero image based on keywords
        Returns single high-quality image URL with gradient background
        """
        try:
            # Use first keyword for hero
            main_keyword = keywords[0] if keywords else "modern"
            
            # Detect category
            category = self._detect_category(main_keyword)
            colors = self.COLOR_SCHEMES.get(category, self.COLOR_SCHEMES['default'])
            
            # Use first color from scheme
            bg_color = colors[0]
            text_color = 'FFFFFF'
            
            # Create hero text
            hero_text = main_keyword.replace('_', ' ').replace('+', ' ').title()
            
            # Get high-res hero image
            url = f"https://placehold.co/1920x1080/{bg_color}/{text_color}/png?text={hero_text}"
            
            logger.info(f"✅ Generated hero image for: {main_keyword} (category: {category}, color: {bg_color})")
            return url
            
        except Exception as e:
            logger.error(f"❌ Hero image error: {str(e)}")
            return None
    
    def extract_keywords_from_prompt(self, prompt: str) -> List[str]:
        """
        Extract relevant keywords from user prompt for image search
        """
        # Remove common words and get meaningful keywords
        common_words = {
            'create', 'build', 'make', 'website', 'for', 'a', 'an', 'the',
            'with', 'and', 'or', 'modern', 'professional', 'beautiful'
        }
        
        # Split and clean
        words = prompt.lower().split()
        keywords = [w.strip('.,!?') for w in words if w not in common_words and len(w) > 3]
        
        # Get first 3 meaningful keywords
        return keywords[:3] if keywords else ['business', 'professional']
    
    async def search_contextual_images(self, prompt: str) -> Dict[str, any]:
        """
        Search for images based on the full prompt context
        Returns dict with hero image and section images
        """
        try:
            keywords = self.extract_keywords_from_prompt(prompt)
            logger.info(f"🔍 Searching images for keywords: {keywords}")
            
            # Get hero image
            hero_image = await self.get_hero_image(keywords)
            
            # Get section images (features, about, etc.)
            section_images = await self.search_images(
                query='+'.join(keywords),
                count=4
            )
            
            return {
                "hero_image": hero_image,
                "section_images": section_images,
                "keywords": keywords
            }
            
        except Exception as e:
            logger.error(f"❌ Contextual image search error: {str(e)}")
            return {
                "hero_image": None,
                "section_images": [],
                "keywords": []
            }
