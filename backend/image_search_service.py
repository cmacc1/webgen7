"""
Image/Video Search Service using Picsum Photos (free, reliable, no auth needed)
"""
import httpx
import logging
from typing import List, Dict, Optional
import asyncio
import hashlib

logger = logging.getLogger(__name__)

class ImageSearchService:
    """Service to search for images and videos from free APIs"""
    
    # Using Picsum Photos - reliable, free, no auth needed
    PICSUM_BASE_URL = "https://picsum.photos"
    
    def __init__(self):
        self.timeout = 10
    
    def _get_seed_from_keyword(self, keyword: str, index: int = 0) -> str:
        """Generate a consistent seed from keyword for reproducible random images"""
        # Create hash from keyword + index for variety
        hash_input = f"{keyword}_{index}".encode('utf-8')
        hash_value = hashlib.md5(hash_input).hexdigest()[:8]
        return hash_value
    
    async def search_images(self, query: str, count: int = 4) -> List[Dict[str, str]]:
        """
        Search for images based on query
        Returns list of image URLs with metadata
        Uses Picsum Photos with seeded random for consistent, high-quality images
        """
        try:
            images = []
            
            # Clean query for seed
            clean_query = query.replace('+', '_').replace(' ', '_').lower()
            
            # Generate multiple image URLs with different seeds for variety
            for i in range(count):
                seed = self._get_seed_from_keyword(clean_query, i)
                # Using Picsum Photos with seed for consistent random images
                url = f"{self.PICSUM_BASE_URL}/seed/{seed}/1600/900"
                images.append({
                    "url": url,
                    "description": f"{query} image {i+1}",
                    "source": "picsum"
                })
            
            logger.info(f"✅ Generated {len(images)} images for query: {query}")
            return images
            
        except Exception as e:
            logger.error(f"❌ Image search error: {str(e)}")
            # Return empty list on error - don't fail generation
            return []
    
    async def get_hero_image(self, keywords: List[str]) -> Optional[str]:
        """
        Get a hero image based on keywords
        Returns single high-quality image URL
        """
        try:
            # Use first keyword for hero
            main_keyword = keywords[0] if keywords else "modern"
            
            # Generate seed from keyword for consistent hero image
            seed = self._get_seed_from_keyword(main_keyword, 99)  # Use 99 for hero to differ from section images
            
            # Get high-res image from Picsum Photos
            url = f"{self.PICSUM_BASE_URL}/seed/{seed}/1920/1080"
            
            logger.info(f"✅ Generated hero image for: {main_keyword} (seed: {seed})")
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
