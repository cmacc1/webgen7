"""
PEXELS IMAGE SERVICE - Real, Contextual Photos
Fetches actual relevant photos from Pexels API based on website type and prompt
"""

import httpx
import asyncio
import logging
from typing import List, Dict, Optional

logger = logging.getLogger(__name__)

class PexelsImageService:
    """Service to fetch real, contextual images from Pexels API"""
    
    def __init__(self):
        self.api_key = "nz7oJbq5rzpacGTjQrbs4SOvDbTPHX9G8kgGtHsMNOljerMbmT8a9RRD"
        self.base_url = "https://api.pexels.com/v1"
        self.headers = {"Authorization": self.api_key}
        
        # Search queries mapped to website types
        self.search_queries = {
            "law_firm": ["law office", "courthouse", "legal documents", "business meeting"],
            "consultant_coaching": ["business coaching", "professional meeting", "mentor", "consultation"],
            "gym": ["gym workout", "fitness training", "weight lifting", "exercise"],
            "restaurant": ["restaurant interior", "food plating", "dining", "chef cooking"],
            "renovation": ["home renovation", "construction", "interior design", "building"],
            "tech": ["technology", "coding", "startup office", "computer work"],
            "saas": ["software development", "team collaboration", "modern office"],
            "medical_clinic": ["medical office", "doctor patient", "healthcare", "clinic"],
            "dental": ["dental office", "dentist", "dental care"],
            "hotel": ["hotel lobby", "hotel room", "hospitality"],
            "real_estate": ["modern home", "house exterior", "property", "real estate"],
            "landscaping": ["landscaping", "garden design", "outdoor spaces"],
            "ecommerce": ["online shopping", "product display", "retail"],
            "spa": ["spa treatment", "massage", "wellness", "relaxation"],
            "barber": ["barber shop", "haircut", "salon"],
            "auto_repair": ["mechanic", "car repair", "auto service"],
            "photography": ["photographer", "camera", "photography studio"],
            "default": ["professional business", "modern office", "teamwork"]
        }
    
    async def search_images(self, query: str, per_page: int = 15) -> List[Dict]:
        """Search Pexels for images matching query"""
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(
                    f"{self.base_url}/search",
                    headers=self.headers,
                    params={
                        "query": query,
                        "per_page": per_page,
                        "orientation": "landscape"
                    }
                )
                
                if response.status_code == 200:
                    data = response.json()
                    photos = data.get("photos", [])
                    
                    images = []
                    for photo in photos:
                        images.append({
                            "url": photo["src"]["large2x"],  # High quality
                            "medium": photo["src"]["large"],
                            "small": photo["src"]["medium"],
                            "photographer": photo["photographer"],
                            "alt": photo.get("alt", query)
                        })
                    
                    logger.info(f"✅ Pexels: Found {len(images)} images for '{query}'")
                    return images
                else:
                    logger.error(f"❌ Pexels API error: {response.status_code}")
                    return []
                    
        except Exception as e:
            logger.error(f"❌ Pexels search error: {str(e)}")
            return []
    
    async def get_hero_image(self, website_type: str, prompt: str) -> Optional[str]:
        """Get a relevant hero image"""
        # Get search queries for this type
        queries = self.search_queries.get(website_type, self.search_queries["default"])
        
        # Try first query
        images = await self.search_images(queries[0], per_page=5)
        
        if images:
            return images[0]["url"]  # Return highest quality
        
        return None
    
    async def get_section_images(self, website_type: str, count: int = 4) -> List[str]:
        """Get multiple relevant section images"""
        queries = self.search_queries.get(website_type, self.search_queries["default"])
        
        all_images = []
        
        # Search with different queries for variety
        for i, query in enumerate(queries[:count]):
            images = await self.search_images(query, per_page=3)
            if images:
                all_images.append(images[0]["url"])
            
            if len(all_images) >= count:
                break
        
        # Fill remaining with first query if needed
        while len(all_images) < count:
            images = await self.search_images(queries[0], per_page=10)
            for img in images:
                if img["url"] not in all_images:
                    all_images.append(img["url"])
                    if len(all_images) >= count:
                        break
        
        logger.info(f"✅ Retrieved {len(all_images)} section images from Pexels")
        return all_images[:count]
    
    async def get_gallery_images(self, website_type: str, count: int = 6) -> List[Dict[str, str]]:
        """Get gallery images with multiple sizes"""
        queries = self.search_queries.get(website_type, self.search_queries["default"])
        
        # Get variety by using multiple queries
        all_images = []
        images = await self.search_images(queries[0], per_page=count)
        
        for img in images[:count]:
            all_images.append({
                "large": img["url"],
                "medium": img["medium"],
                "thumbnail": img["small"],
                "alt": img["alt"],
                "photographer": img["photographer"]
            })
        
        logger.info(f"✅ Retrieved {len(all_images)} gallery images from Pexels")
        return all_images
    
    def get_fallback_gradient(self, website_type: str) -> str:
        """Get fallback gradient if Pexels fails"""
        gradients = {
            "law_firm": "linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%)",
            "gym": "linear-gradient(135deg, #dc2626 0%, #ef4444 100%)",
            "restaurant": "linear-gradient(135deg, #92400e 0%, #d97706 100%)",
            "renovation": "linear-gradient(135deg, #854d0e 0%, #ca8a04 100%)",
            "default": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
        }
        return gradients.get(website_type, gradients["default"])
