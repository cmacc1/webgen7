"""
BUSINESS IMAGE MAPPER - Hyper-Specific Image Search Queries
Maps business types to highly relevant image search terms
"""

BUSINESS_IMAGE_QUERIES = {
    # Home Services - VERY SPECIFIC
    "flooring": ["hardwood flooring installation", "luxury floor living room", "tile flooring modern home", "laminate wood floor"],
    "renovation": ["home renovation before after", "modern kitchen remodel", "bathroom renovation luxury", "house renovation interior"],
    "roofing": ["roof installation professional", "new roof shingles house", "roofing contractor work", "modern roof architecture"],
    "landscaping": ["professional landscaping design", "luxury garden landscape", "outdoor landscaping project", "landscape design modern"],
    "interior_design": ["luxury interior design living room", "modern interior designer project", "elegant home interior", "interior design showcase"],
    "plumbing": ["professional plumber work", "modern plumbing installation", "plumbing service clean", "bathroom plumbing luxury"],
    "electrical": ["electrician professional work", "electrical panel modern", "lighting installation luxury", "electrical service"],
    "hvac": ["hvac system installation", "modern air conditioning unit", "heating cooling professional", "hvac technician work"],
    "cleaning": ["professional cleaning service", "spotless clean home interior", "cleaning company work", "pristine clean house"],
    "pest_control": ["professional pest control service", "home protection pest", "pest control technician", "clean safe home"],
    "painting": ["interior painting professional", "fresh painted wall living room", "house painting service", "paint color consultation"],
    "locksmith": ["professional locksmith service", "modern door lock security", "locksmith key cutting", "secure home locks"],
    "moving": ["professional moving company", "movers loading truck", "relocation service", "moving boxes organized"],
    
    # Real Estate
    "real_estate": ["luxury home for sale", "modern house real estate", "real estate property showcase", "beautiful home interior"],
    
    # Food & Hospitality - SPECIFIC INTERIOR SHOTS
    "restaurant": ["elegant restaurant interior dining", "fine dining restaurant ambiance", "modern restaurant design", "restaurant food plating"],
    "cafe": ["cozy coffee shop interior", "modern cafe design", "latte art coffee shop", "cafe workspace aesthetic"],
    "bar": ["upscale bar interior", "craft cocktails bar", "modern lounge bar design", "bartender mixing drinks"],
    "bakery": ["artisan bakery display", "fresh baked goods showcase", "bakery interior cozy", "bread pastry display"],
    "hotel": ["luxury hotel lobby", "elegant hotel room interior", "five star hotel suite", "hotel hospitality service"],
    
    # Health & Wellness - PROFESSIONAL SETTINGS
    "medical_clinic": ["modern medical clinic interior", "doctor consultation room", "clean medical office", "healthcare facility professional"],
    "dental": ["modern dental office", "dentist chair clinic", "dental practice interior clean", "dentist examination room"],
    "gym": ["modern gym equipment", "fitness center interior", "gym workout training", "state of art fitness facility"],
    "yoga_studio": ["peaceful yoga studio interior", "yoga class meditation", "zen yoga space", "wellness studio serene"],
    "spa": ["luxury spa interior", "massage therapy room", "spa relaxation wellness", "elegant spa treatment room"],
    "chiropractor": ["chiropractic office modern", "chiropractor treatment room", "spine health clinic", "chiropractic care professional"],
    "pharmacy": ["modern pharmacy interior", "pharmacy counter professional", "medication pharmacy clean", "pharmacy service"],
    
    # Business & Professional - OFFICE SETTINGS
    "saas": ["modern tech office workspace", "software development team", "saas dashboard analytics", "tech startup office"],
    "agency": ["creative agency office", "design team collaboration", "modern agency workspace", "digital agency professionals"],
    "consulting": ["professional business meeting", "consultant office modern", "business strategy session", "executive consulting"],
    "law_firm": ["professional law office", "attorney office elegant", "legal consultation room", "law library modern"],
    "accounting": ["accountant office professional", "financial planning desk", "accounting firm modern", "tax preparation office"],
    "financial_advisor": ["financial advisor consultation", "wealth management office", "investment planning professional", "financial planning meeting"],
    
    # Automotive
    "auto_repair": ["auto mechanic shop", "car repair garage professional", "automotive service bay", "mechanic working car"],
    "car_dealership": ["car showroom luxury", "new car dealership floor", "automobile showroom modern", "car sales display"],
    "car_wash": ["professional car wash", "car detailing service", "clean shiny car", "auto wash facility"],
    
    # Creative - SHOWCASE WORK
    "photography": ["professional photography studio", "photographer camera gear", "photo session shoot", "photography portfolio"],
    "videography": ["video production studio", "filmmaker camera equipment", "video shoot professional", "cinematography setup"],
    "art_gallery": ["modern art gallery interior", "art exhibition space", "gallery wall paintings", "contemporary art display"],
    "music": ["recording studio professional", "musician performance stage", "music production studio", "concert stage lighting"],
    
    # E-commerce - PRODUCT FOCUSED
    "ecommerce": ["online shopping product display", "ecommerce warehouse", "product photography studio", "shopping cart checkout"],
    "fashion": ["fashion boutique interior", "clothing store display", "fashion runway model", "designer clothing rack"],
    "jewelry": ["luxury jewelry display case", "diamond jewelry showcase", "jewelry store elegant", "fine jewelry close up"],
    "furniture": ["modern furniture showroom", "elegant furniture display", "interior design furniture", "contemporary furniture store"],
    
    # Education
    "online_course": ["online learning student laptop", "elearning classroom virtual", "online education workspace", "student studying computer"],
    "school": ["modern classroom interior", "students learning education", "school campus building", "education facility"],
    
    # Personal Services
    "barber": ["barbershop interior modern", "barber cutting hair", "mens grooming salon", "barber chair vintage"],
    "salon": ["hair salon interior elegant", "beauty salon styling", "salon chair modern", "hair stylist work"],
    "tattoo": ["tattoo studio interior", "tattoo artist working", "tattoo parlor design", "tattoo shop modern"],
    "pet_grooming": ["pet grooming salon", "dog grooming professional", "pet spa interior", "groomer working dog"],
    
    # Tech
    "software_company": ["tech office modern workspace", "software engineers coding", "tech company office", "development team"],
    "app": ["mobile app development", "app interface design", "smartphone app screen", "mobile application"],
    "web_design": ["web designer workspace", "website design mockup", "web development office", "ui ux design"],
    "it_services": ["it support technician", "server room data center", "it professional computer", "network operations center"],
    "cybersecurity": ["cybersecurity operations center", "security analyst working", "data protection encryption", "cyber security professional"],
    
    # Events
    "event_planning": ["elegant event venue setup", "event planning coordination", "wedding reception decorated", "event decor professional"],
    "wedding": ["wedding ceremony venue", "wedding reception elegant", "bridal party celebration", "wedding venue decorated"],
    "venue": ["event venue interior spacious", "banquet hall elegant", "wedding venue decorated", "event space modern"],
    
    # Default fallback
    "default": ["modern professional business", "elegant workspace interior", "professional service office", "contemporary business setting"]
}

def get_hero_image_query(website_type: str, prompt: str) -> str:
    """
    Get highly specific image search query for business type
    Returns professional, relevant search term
    """
    
    # Get business-specific queries
    queries = BUSINESS_IMAGE_QUERIES.get(website_type, BUSINESS_IMAGE_QUERIES["default"])
    
    # Use first query as primary (most specific)
    primary_query = queries[0]
    
    # Extract business name if present
    import re
    business_name_match = re.search(r'(?:for|called|named)\s+["\']?([A-Z][a-zA-Z\s]+)["\']?', prompt)
    if business_name_match:
        business_name = business_name_match.group(1).strip()
        # Don't include business name in search (too specific, won't find results)
        # Just use business type query
    
    # Check for specific mentions in prompt
    prompt_lower = prompt.lower()
    
    # Flooring specific
    if website_type == "flooring":
        if "hardwood" in prompt_lower:
            return "luxury hardwood flooring living room"
        elif "tile" in prompt_lower:
            return "modern tile flooring kitchen"
        elif "carpet" in prompt_lower:
            return "carpet flooring bedroom interior"
        elif "laminate" in prompt_lower:
            return "laminate wood flooring modern home"
    
    # Restaurant specific
    if website_type == "restaurant":
        if "italian" in prompt_lower:
            return "elegant italian restaurant interior dining"
        elif "pizza" in prompt_lower:
            return "pizzeria restaurant interior"
        elif "sushi" in prompt_lower:
            return "modern sushi restaurant interior"
        elif "fine dining" in prompt_lower:
            return "luxury fine dining restaurant"
    
    # Gym specific
    if website_type == "gym":
        if "crossfit" in prompt_lower:
            return "crossfit gym equipment interior"
        elif "yoga" in prompt_lower:
            return "yoga studio peaceful interior"
        elif "boxing" in prompt_lower:
            return "boxing gym training interior"
    
    # Real estate specific
    if website_type == "real_estate":
        if "luxury" in prompt_lower:
            return "luxury mansion real estate interior"
        elif "commercial" in prompt_lower:
            return "commercial property office building"
        elif "apartment" in prompt_lower:
            return "modern apartment interior real estate"
    
    return primary_query

def get_alternative_queries(website_type: str) -> list:
    """Get alternative search queries for fallback"""
    queries = BUSINESS_IMAGE_QUERIES.get(website_type, BUSINESS_IMAGE_QUERIES["default"])
    return queries[1:4]  # Return next 3 alternatives
