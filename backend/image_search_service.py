"""
AI-Powered Image Generation Service using OpenAI DALL-E
Automatically generates contextual, high-quality images for websites
"""
import os
import base64
import logging
from typing import List, Dict, Optional
import asyncio
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

logger = logging.getLogger(__name__)

class ImageSearchService:
    """Service to generate AI images using OpenAI's image generation API"""
    
    def __init__(self):
        self.api_key = os.getenv('EMERGENT_LLM_KEY')
        if not self.api_key:
            logger.warning("⚠️ EMERGENT_LLM_KEY not found in environment")
        
    def _create_image_prompt(self, context: str, image_type: str = "general") -> str:
        """Create a detailed prompt for image generation"""
        if image_type == "hero":
            return f"Professional, high-quality hero image for {context}. Modern, vibrant, eye-catching design suitable for a website header. Photorealistic style."
        elif image_type == "section":
            return f"Professional stock photo representing {context}. Clean, modern, suitable for website content section. High quality, photorealistic."
        else:
            return f"Professional image for {context} website. Modern, clean, photorealistic."
    
    async def _generate_single_image(self, prompt: str) -> Optional[str]:
        """Generate a single image and return as base64 data URL"""
        try:
            from emergentintegrations.llm.openai.image_generation import OpenAIImageGeneration
            
            if not self.api_key:
                logger.error("❌ Cannot generate image: EMERGENT_LLM_KEY not configured")
                return None
            
            # Initialize image generator
            image_gen = OpenAIImageGeneration(api_key=self.api_key)
            
            # Generate image (this may take 30-60 seconds)
            logger.info(f"🎨 Generating AI image: {prompt[:60]}...")
            images = await image_gen.generate_images(
                prompt=prompt,
                model="gpt-image-1",  # Latest model
                number_of_images=1
            )
            
            if images and len(images) > 0:
                # Convert to base64 data URL
                image_base64 = base64.b64encode(images[0]).decode('utf-8')
                data_url = f"data:image/png;base64,{image_base64}"
                logger.info(f"✅ Image generated successfully ({len(images[0])} bytes)")
                return data_url
            else:
                logger.error("❌ No image was generated")
                return None
                
        except ImportError:
            logger.error("❌ emergentintegrations not installed. Run: pip install emergentintegrations --extra-index-url https://d33sy5i8bnduwe.cloudfront.net/simple/")
            return None
        except Exception as e:
            logger.error(f"❌ Image generation error: {str(e)}")
            return None
    
    async def search_images(self, query: str, count: int = 4) -> List[Dict[str, str]]:
        """
        Generate AI images based on query
        Returns list of images with base64 data URLs
        Note: This generates real AI images, so it may take 1-2 minutes
        """
        try:
            images = []
            
            # Clean query
            clean_query = query.replace('+', ' ').replace('_', ' ').strip()
            
            logger.info(f"🎨 Generating {count} AI images for: {clean_query}")
            
            # Generate images concurrently for speed
            tasks = []
            for i in range(count):
                prompt = self._create_image_prompt(clean_query, "section")
                # Add variety to each image
                if i == 0:
                    prompt += " Close-up view."
                elif i == 1:
                    prompt += " Wide angle view."
                elif i == 2:
                    prompt += " Detail shot."
                else:
                    prompt += " Overview perspective."
                
                tasks.append(self._generate_single_image(prompt))
            
            # Wait for all images to generate
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            # Collect successful results
            for i, result in enumerate(results):
                if isinstance(result, str) and result:
                    images.append({
                        "url": result,  # Base64 data URL
                        "description": f"{clean_query} image {i+1}",
                        "source": "ai-generated",
                        "type": "base64"
                    })
                elif isinstance(result, Exception):
                    logger.error(f"Failed to generate image {i+1}: {str(result)}")
            
            logger.info(f"✅ Successfully generated {len(images)}/{count} AI images")
            return images
            
        except Exception as e:
            logger.error(f"❌ Image search error: {str(e)}")
            return []
    
    async def get_hero_image(self, keywords: List[str]) -> Optional[str]:
        """
        Generate a hero image based on keywords
        Returns base64 data URL for high-quality hero image
        """
        try:
            # Use first keyword or combination
            main_keyword = keywords[0] if keywords else "modern business"
            
            # Create compelling hero prompt
            prompt = self._create_image_prompt(main_keyword, "hero")
            
            logger.info(f"🎨 Generating hero image for: {main_keyword}")
            
            # Generate hero image
            hero_url = await self._generate_single_image(prompt)
            
            if hero_url:
                logger.info(f"✅ Hero image generated successfully")
            else:
                logger.error(f"❌ Failed to generate hero image")
            
            return hero_url
            
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
