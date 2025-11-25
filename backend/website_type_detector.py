"""
WEBSITE TYPE DETECTION ENGINE
Analyzes user prompts to identify website type and select appropriate design patterns
"""

import re
from typing import Dict, List, Tuple

class WebsiteTypeDetector:
    """Intelligent website type detection from user prompts"""
    
    def __init__(self):
        # Comprehensive keyword mappings for all website types
        self.type_keywords = {
            "law_firm": ["law", "legal", "attorney", "lawyer", "firm", "justice", "court", "litigation"],
            "consultant_coaching": ["consultant", "coaching", "coach", "advisor", "consulting", "mentorship", "training", "consulting firm"],
            "financial_advisor": ["financial", "wealth", "investment", "portfolio", "finance", "money management", "wealth management"],
            "accounting": ["accounting", "bookkeeping", "cpa", "tax", "payroll", "audit"],
            "recruitment": ["recruitment", "staffing", "hiring", "job", "career", "employment agency"],
            
            # Trades & Home Services
            "hvac": ["hvac", "heating", "cooling", "air conditioning", "furnace", "ac repair"],
            "plumbing": ["plumbing", "plumber", "pipe", "drain", "water heater"],
            "electrical": ["electrical", "electrician", "wiring", "circuit"],
            "renovation": ["renovation", "remodeling", "construction", "contractor", "building"],
            "landscaping": ["landscaping", "lawn care", "gardening", "yard", "outdoor"],
            "roofing": ["roofing", "roof", "siding", "gutter"],
            "flooring": ["flooring", "floors", "hardwood", "tile", "carpet"],
            "pest_control": ["pest", "exterminator", "bug", "termite", "rodent"],
            "cleaning": ["cleaning", "maid", "janitorial", "housekeeping"],
            
            # Health, Wellness & Fitness
            "gym": ["gym", "fitness", "workout", "training", "exercise", "health club"],
            "medical_clinic": ["medical", "clinic", "doctor", "healthcare", "hospital", "practice"],
            "dental": ["dental", "dentist", "orthodontist", "teeth"],
            "chiropractor": ["chiropractor", "chiropractic", "spine", "adjustment"],
            "physical_therapy": ["physical therapy", "physiotherapy", "rehabilitation", "pt"],
            "yoga_studio": ["yoga", "pilates", "meditation", "wellness studio"],
            "spa": ["spa", "massage", "aesthetics", "medspa", "beauty"],
            
            # Hospitality & Events
            "hotel": ["hotel", "motel", "inn", "lodging", "accommodation"],
            "restaurant": ["restaurant", "cafe", "bistro", "diner", "eatery", "food", "dining"],
            "travel_agency": ["travel", "tour", "vacation", "trip", "destination"],
            "event_venue": ["venue", "event space", "hall", "ballroom"],
            "conference": ["conference", "convention", "summit", "expo"],
            
            # Automotive & Real Estate
            "car_dealership": ["car", "auto", "dealership", "vehicle", "automotive"],
            "real_estate": ["real estate", "realtor", "property", "homes", "housing"],
            "property_management": ["property management", "landlord", "rental"],
            
            # Digital, Media & Creator
            "agency": ["agency", "marketing", "advertising", "creative", "digital agency"],
            "artist": ["artist", "musician", "painter", "creative", "art"],
            "podcaster": ["podcast", "streamer", "content creator", "influencer"],
            "crypto": ["crypto", "cryptocurrency", "memecoin", "token", "blockchain"],
            "saas": ["saas", "software", "platform", "crm", "tool", "app", "cloud software"],
            "marketplace": ["marketplace", "ecommerce", "shop", "store", "buy", "sell"],
            "blog": ["blog", "news", "magazine", "journal", "publication"],
            "portal": ["portal", "dashboard", "login", "member area"],
            "membership": ["membership", "subscription", "course", "online learning"],
            
            # B2B Services
            "msp": ["msp", "managed services", "it support", "tech support"],
            "industrial": ["industrial", "equipment", "machinery", "manufacturing"],
            "api_service": ["api", "developer", "platform", "integration"],
            "logistics": ["logistics", "freight", "shipping", "transportation"],
            "data_analytics": ["analytics", "data", "insights", "reporting"],
            
            # Niche Retail
            "vintage_store": ["vintage", "thrift", "antique", "secondhand"],
            "collectibles": ["collectible", "coin", "stamp", "memorabilia"],
            "nursery": ["nursery", "plants", "garden", "greenhouse"],
            "hobby_shop": ["hobby", "model", "rc", "toys"],
            "art_prints": ["art print", "poster", "digital download", "wall art"],
            
            # Specialized Healthcare
            "veterinary": ["veterinary", "vet", "animal", "pet clinic"],
            "tattoo": ["tattoo", "piercing", "ink", "body art"],
            "dental_specialist": ["implant", "cosmetic dentistry", "dental specialist"],
            "teletherapy": ["therapy", "counseling", "mental health", "teletherapy"],
            
            # Creative Services
            "voiceover": ["voiceover", "voice actor", "narrator"],
            "copywriter": ["copywriter", "content writer", "writer"],
            "photographer": ["photographer", "photography", "wedding photographer"],
            "architect": ["architecture", "architect", "design"],
            "stylist": ["stylist", "fashion", "wardrobe"],
            
            # Food & Beverage
            "brewery": ["brewery", "distillery", "craft beer", "spirits"],
            "food_truck": ["food truck", "mobile food", "pop-up"],
            "coffee_roaster": ["coffee", "roaster", "cafe"],
            "catering": ["catering", "event catering", "meal prep"],
            
            # Local Services
            "pizzeria": ["pizza", "pizzeria", "takeout"],
            "barber": ["barber", "salon", "hair", "hairstylist"],
            "daycare": ["daycare", "preschool", "childcare"],
            "auto_repair": ["auto repair", "mechanic", "car repair"],
            "pharmacy": ["pharmacy", "drugstore", "prescriptions"],
            "locksmith": ["locksmith", "keys", "locks"],
            "junk_removal": ["junk removal", "hauling", "waste"],
            "window_cleaner": ["window cleaning", "pressure washing"],
            "storage": ["storage", "self-storage", "warehouse"],
            
            # Professional Services
            "insurance": ["insurance", "insurance agency", "coverage"],
            "tax_prep": ["tax", "tax preparation", "tax service"],
            "massage": ["massage", "massage therapy", "bodywork"],
            "personal_trainer": ["personal trainer", "fitness coach"],
            "financial_planner": ["financial planner", "retirement", "investment advisor"],
            "notary": ["notary", "notarization", "documents"],
            "tutor": ["tutor", "tutoring", "education"],
            
            # Retail
            "boutique": ["boutique", "apparel", "fashion", "clothing"],
            "pet_store": ["pet store", "pet supply", "pet shop"],
            "wholesale": ["wholesale", "distributor", "b2b"],
            "art_gallery": ["gallery", "art gallery", "exhibition"],
            "jewelry": ["jewelry", "jeweler", "diamonds"]
        }
        
        # Industry-specific features
        self.type_features = {
            "law_firm": ["practice_areas", "attorney_bios", "case_results", "trust_badges", "consultation_form"],
            "consultant_coaching": ["methodology", "testimonials", "booking_calendar", "packages", "lead_magnet"],
            "gym": ["class_schedule", "membership_pricing", "trainer_profiles", "facility_tour"],
            "restaurant": ["menu", "reservation_system", "online_ordering", "location"],
            "saas": ["pricing_tiers", "features_comparison", "demo_video", "api_docs", "signup_flow"],
            "ecommerce": ["product_grid", "shopping_cart", "checkout", "reviews"],
            "medical_clinic": ["services", "doctor_profiles", "appointment_booking", "patient_forms"],
            "real_estate": ["property_search", "agent_profiles", "mortgage_calculator"],
        }
    
    def detect_type(self, prompt: str) -> Tuple[str, float]:
        """Detect website type from prompt with confidence score"""
        prompt_lower = prompt.lower()
        
        scores = {}
        for website_type, keywords in self.type_keywords.items():
            score = 0
            for keyword in keywords:
                if keyword in prompt_lower:
                    # Weight longer, more specific keywords higher
                    score += len(keyword.split()) * 2
            
            if score > 0:
                scores[website_type] = score
        
        if scores:
            best_match = max(scores.items(), key=lambda x: x[1])
            confidence = min(best_match[1] / 10.0, 1.0)  # Normalize to 0-1
            return best_match[0], confidence
        
        # Default fallback
        return "business", 0.3
    
    def extract_business_details(self, prompt: str) -> Dict:
        """Extract business name, location, etc. from prompt"""
        details = {
            "name": None,
            "location": None,
            "specialty": None
        }
        
        # Try to find business name (often in quotes or after "for")
        name_patterns = [
            r'["']([^"']+)["']',
            r'(?:for|called|named)\s+([A-Z][A-Za-z0-9\s&]+)',
        ]
        
        for pattern in name_patterns:
            match = re.search(pattern, prompt)
            if match:
                details["name"] = match.group(1).strip()
                break
        
        # Location detection
        location_pattern = r'(?:in|at|based in)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?(?:,\s*[A-Z]{2})?)'
        loc_match = re.search(location_pattern, prompt)
        if loc_match:
            details["location"] = loc_match.group(1)
        
        return details
    
    def get_recommended_sections(self, website_type: str) -> List[str]:
        """Get recommended sections for website type"""
        return self.type_features.get(website_type, ["hero", "features", "about", "contact"])
