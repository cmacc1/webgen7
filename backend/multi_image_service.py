"""
MULTI-SOURCE IMAGE SERVICE - High-Quality Free Images
Supports: Unsplash, Pixabay, Pexels with intelligent fallbacks
All APIs are 100% FREE
"""

import os
import httpx
import logging
from typing import Optional, List, Dict

logger = logging.getLogger(__name__)

class MultiImageService:
    """
    Multi-source image provider with quality prioritization
    Priority: Unsplash > Pixabay > Pexels
    """
    
    def __init__(self):
        # API Keys from environment
        self.unsplash_key = os.environ.get('UNSPLASH_ACCESS_KEY', '')
        self.pixabay_key = os.environ.get('PIXABAY_API_KEY', '')
        self.pexels_key = os.environ.get('PEXELS_API_KEY', '')
        
        # Track which services are available
        self.unsplash_available = bool(self.unsplash_key)
        self.pixabay_available = bool(self.pixabay_key)
        self.pexels_available = bool(self.pexels_key)
        
        logger.info(f"🖼️ Image sources available: Unsplash={self.unsplash_available}, Pixabay={self.pixabay_available}, Pexels={self.pexels_available}")
    
    async def get_hero_image(self, query: str, orientation: str = "landscape") -> Optional[Dict]:
        """
        Get high-quality hero image from best available source
        Returns: {"url": "...", "photographer": "...", "source": "unsplash/pixabay/pexels"}
        """
        logger.info(f"🔍 Searching for hero image: '{query}'")
        
        # Try Unsplash first (highest quality)
        if self.unsplash_available:
            result = await self._search_unsplash(query, orientation, count=1)
            if result:
                logger.info(f"✅ Found hero image on Unsplash")
                return result[0]
        
        # Fallback to Pixabay
        if self.pixabay_available:
            result = await self._search_pixabay(query, count=1)
            if result:
                logger.info(f"✅ Found hero image on Pixabay")
                return result[0]
        
        # Fallback to Pexels
        if self.pexels_available:
            result = await self._search_pexels(query, orientation, count=1)
            if result:
                logger.info(f"✅ Found hero image on Pexels")
                return result[0]
        
        logger.warning(f"❌ No hero image found for '{query}'")
        return None
    
    async def _search_unsplash(self, query: str, orientation: str = "landscape", count: int = 1) -> List[Dict]:
        """
        Search Unsplash API
        Rate limit: 50 requests/hour (free tier)
        """
        if not self.unsplash_key:
            return []
        
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(
                    "https://api.unsplash.com/search/photos",
                    params={
                        "query": query,
                        "orientation": orientation,
                        "per_page": count,
                        "client_id": self.unsplash_key
                    }
                )
                
                if response.status_code == 200:
                    data = response.json()
                    results = data.get("results", [])
                    
                    images = []
                    for photo in results[:count]:
                        images.append({
                            "url": photo["urls"]["regular"],  # High quality (1080px)
                            "url_full": photo["urls"]["full"],  # Highest quality
                            "url_thumb": photo["urls"]["thumb"],  # Thumbnail
                            "photographer": photo["user"]["name"],
                            "photographer_url": photo["user"]["links"]["html"],
                            "source": "unsplash",
                            "alt": photo.get("alt_description", query),
                            "width": photo["width"],
                            "height": photo["height"]
                        })
                    
                    logger.info(f"🌄 Unsplash: Found {len(images)} images for '{query}'")
                    return images
                else:
                    logger.warning(f"⚠️ Unsplash API error: {response.status_code}")
                    return []
                    
        except Exception as e:
            logger.error(f"❌ Unsplash error: {str(e)}")
            return []
    
    async def _search_pixabay(self, query: str, count: int = 1) -> List[Dict]:
        """
        Search Pixabay API
        No rate limit, unlimited free access
        """
        if not self.pixabay_key:
            return []
        
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(
                    "https://pixabay.com/api/",
                    params={
                        "key": self.pixabay_key,
                        "q": query,
                        "image_type": "photo",
                        "orientation": "horizontal",
                        "per_page": count,
                        "safesearch": "true"
                    }
                )
                
                if response.status_code == 200:
                    data = response.json()
                    hits = data.get("hits", [])
                    
                    images = []
                    for photo in hits[:count]:
                        images.append({
                            "url": photo["largeImageURL"],  # High quality
                            "url_full": photo["largeImageURL"],
                            "url_thumb": photo["previewURL"],
                            "photographer": photo["user"],
                            "photographer_url": f"https://pixabay.com/users/{photo['user']}-{photo['user_id']}/",
                            "source": "pixabay",
                            "alt": photo.get("tags", query),
                            "width": photo["imageWidth"],
                            "height": photo["imageHeight"]
                        })
                    
                    logger.info(f"🎨 Pixabay: Found {len(images)} images for '{query}'")
                    return images
                else:
                    logger.warning(f"⚠️ Pixabay API error: {response.status_code}")
                    return []
                    
        except Exception as e:
            logger.error(f"❌ Pixabay error: {str(e)}")
            return []
    
    async def _search_pexels(self, query: str, orientation: str = "landscape", count: int = 1) -> List[Dict]:
        """
        Search Pexels API (existing)
        Rate limit: 200 requests/hour
        """
        if not self.pexels_key:
            return []
        
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(
                    "https://api.pexels.com/v1/search",
                    headers={"Authorization": self.pexels_key},
                    params={
                        "query": query,
                        "orientation": orientation,
                        "per_page": count
                    }
                )
                
                if response.status_code == 200:
                    data = response.json()
                    photos = data.get("photos", [])
                    
                    images = []
                    for photo in photos[:count]:
                        images.append({
                            "url": photo["src"]["large"],  # High quality
                            "url_full": photo["src"]["original"],
                            "url_thumb": photo["src"]["medium"],
                            "photographer": photo["photographer"],
                            "photographer_url": photo["photographer_url"],
                            "source": "pexels",
                            "alt": photo.get("alt", query),
                            "width": photo["width"],
                            "height": photo["height"]
                        })
                    
                    logger.info(f"📸 Pexels: Found {len(images)} images for '{query}'")
                    return images
                else:
                    logger.warning(f"⚠️ Pexels API error: {response.status_code}")
                    return []
                    
        except Exception as e:
            logger.error(f"❌ Pexels error: {str(e)}")
            return []
    
    async def get_multiple_images(self, queries: List[str], count_per_query: int = 1) -> List[Dict]:
        """
        Get multiple images for different queries
        Distributes across all available sources for variety
        """
        all_images = []
        sources = []
        
        # Build available sources list
        if self.unsplash_available:
            sources.append("unsplash")
        if self.pixabay_available:
            sources.append("pixabay")
        if self.pexels_available:
            sources.append("pexels")
        
        if not sources:
            logger.error("❌ No image sources available")
            return []
        
        # Rotate through sources for variety
        source_index = 0
        for query in queries:
            source = sources[source_index % len(sources)]
            
            if source == "unsplash":
                results = await self._search_unsplash(query, count=count_per_query)
            elif source == "pixabay":
                results = await self._search_pixabay(query, count=count_per_query)
            else:  # pexels
                results = await self._search_pexels(query, count=count_per_query)
            
            all_images.extend(results)
            source_index += 1
        
        logger.info(f"✅ Retrieved {len(all_images)} total images from {len(sources)} sources")
        return all_images
    
    def get_attribution_html(self, image: Dict) -> str:
        """
        Generate proper attribution HTML for an image
        Required by all three services
        """
        source = image.get("source", "unknown")
        photographer = image.get("photographer", "Unknown")
        photographer_url = image.get("photographer_url", "#")
        
        if source == "unsplash":
            return f'Photo by <a href="{photographer_url}?utm_source=your_app&utm_medium=referral">{photographer}</a> on <a href="https://unsplash.com?utm_source=your_app&utm_medium=referral">Unsplash</a>'
        elif source == "pixabay":
            return f'Image by <a href="{photographer_url}">{photographer}</a> from <a href="https://pixabay.com">Pixabay</a>'
        elif source == "pexels":
            return f'Photo by <a href="{photographer_url}">{photographer}</a> on <a href="https://www.pexels.com">Pexels</a>'
        else:
            return f'Photo by {photographer}'
    
    async def search_with_fallback(self, query: str, orientation: str = "landscape") -> Optional[Dict]:
        """
        Search all sources with intelligent fallback
        Returns first successful result
        """
        # Try all sources in priority order
        sources = [
            ("Unsplash", self._search_unsplash),
            ("Pixabay", self._search_pixabay),
            ("Pexels", self._search_pexels)
        ]
        
        for source_name, search_func in sources:
            try:
                results = await search_func(query, orientation=orientation if source_name != "Pixabay" else None, count=1)
                if results:
                    logger.info(f"✅ Found image on {source_name}")
                    return results[0]
            except Exception as e:
                logger.warning(f"⚠️ {source_name} search failed: {str(e)}")
                continue
        
        return None

# Test function
async def test_multi_image_service():
    """Test all three image sources"""
    service = MultiImageService()
    
    print("\n🧪 Testing Multi-Image Service\n")
    
    # Test hero image
    hero = await service.get_hero_image("modern office workspace")
    if hero:
        print(f"✅ Hero Image: {hero['source']} - {hero['url'][:50]}...")
        print(f"   Photographer: {hero['photographer']}")
    
    # Test multiple queries
    queries = ["coffee cup", "laptop", "notebook"]
    images = await service.get_multiple_images(queries)
    print(f"\n✅ Multiple Images: {len(images)} found")
    for img in images:
        print(f"   - {img['source']}: {img['alt']}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_multi_image_service())
