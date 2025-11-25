"""
COMPREHENSIVE WEBSITE TYPES - 100+ Categories
Each type has keywords for detection and 5 unique template variations
"""

WEBSITE_TYPES = {
    # Business & Professional Services
    "saas": {
        "keywords": ["saas", "software as a service", "cloud software", "subscription software", "platform"],
        "templates": ["modern_dashboard", "minimalist_tech", "gradient_hero", "dark_mode_pro", "glassmorphism_app"]
    },
    "agency": {
        "keywords": ["agency", "digital agency", "marketing agency", "creative agency", "design studio"],
        "templates": ["portfolio_grid", "full_screen_showcase", "split_screen_bold", "masonry_projects", "timeline_work"]
    },
    "consulting": {
        "keywords": ["consulting", "consultant", "advisory", "business consulting", "strategy"],
        "templates": ["professional_corporate", "executive_minimal", "trust_builder", "expertise_showcase", "sidebar_services"]
    },
    "law_firm": {
        "keywords": ["law", "lawyer", "attorney", "legal", "law firm", "legal services"],
        "templates": ["professional_trust", "dark_authority", "columned_classic", "modern_legal", "sidebar_practice_areas"]
    },
    "accounting": {
        "keywords": ["accounting", "accountant", "bookkeeping", "tax", "cpa", "financial services"],
        "templates": ["clean_professional", "trust_numbers", "sidebar_services", "calculator_featured", "corporate_blue"]
    },
    
    # Real Estate & Construction
    "real_estate": {
        "keywords": ["real estate", "property", "realtor", "homes", "listings", "housing"],
        "templates": ["property_showcase", "map_integrated", "luxury_properties", "search_focused", "agent_profiles"]
    },
    "renovation": {
        "keywords": ["renovation", "remodeling", "home improvement", "contractor", "construction"],
        "templates": ["before_after_gallery", "project_showcase", "service_cards", "testimonial_heavy", "sidebar_services"]
    },
    "flooring": {
        "keywords": ["flooring", "floors", "hardwood", "carpet", "tile", "laminate"],
        "templates": ["material_showcase", "room_visualizer", "comparison_grid", "texture_focused", "portfolio_masonry"]
    },
    "roofing": {
        "keywords": ["roofing", "roof", "roofer", "roof repair", "roof replacement"],
        "templates": ["trust_badges", "emergency_cta", "warranty_featured", "project_gallery", "service_areas"]
    },
    "landscaping": {
        "keywords": ["landscaping", "landscape", "lawn care", "gardening", "outdoor"],
        "templates": ["seasonal_showcase", "before_after", "service_packages", "green_nature", "portfolio_grid"]
    },
    "interior_design": {
        "keywords": ["interior design", "interior designer", "home design", "decoration"],
        "templates": ["portfolio_luxury", "mood_board", "room_by_room", "designer_profile", "full_screen_gallery"]
    },
    
    # Health & Wellness
    "medical_clinic": {
        "keywords": ["medical", "clinic", "doctor", "healthcare", "physician", "medical practice"],
        "templates": ["appointment_focused", "trust_professional", "doctor_profiles", "services_detailed", "patient_portal"]
    },
    "dental": {
        "keywords": ["dental", "dentist", "orthodontics", "teeth", "dental care"],
        "templates": ["smile_gallery", "appointment_booking", "services_visual", "family_friendly", "modern_clean"]
    },
    "gym": {
        "keywords": ["gym", "fitness", "health club", "workout", "training center"],
        "templates": ["membership_plans", "class_schedule", "trainer_profiles", "transformation_gallery", "dark_energetic"]
    },
    "yoga_studio": {
        "keywords": ["yoga", "yoga studio", "meditation", "wellness center"],
        "templates": ["calming_minimal", "class_schedule", "instructor_profiles", "serene_imagery", "booking_integrated"]
    },
    "spa": {
        "keywords": ["spa", "massage", "beauty", "salon", "wellness spa"],
        "templates": ["luxurious_calm", "service_menu", "booking_system", "tranquil_colors", "package_deals"]
    },
    "chiropractor": {
        "keywords": ["chiropractor", "chiropractic", "spine", "back pain"],
        "templates": ["pain_relief_focused", "appointment_priority", "conditions_treated", "trust_medical", "testimonial_based"]
    },
    "pharmacy": {
        "keywords": ["pharmacy", "drugstore", "prescriptions", "medications"],
        "templates": ["prescription_transfer", "service_focused", "trust_healthcare", "clean_professional", "online_refill"]
    },
    
    # Food & Hospitality
    "restaurant": {
        "keywords": ["restaurant", "dining", "eatery", "bistro", "cafe", "diner"],
        "templates": ["menu_showcase", "reservation_system", "food_gallery", "chef_story", "dark_elegant"]
    },
    "cafe": {
        "keywords": ["cafe", "coffee shop", "coffee house", "espresso bar"],
        "templates": ["cozy_minimal", "menu_board", "instagram_feed", "location_focused", "order_online"]
    },
    "bar": {
        "keywords": ["bar", "pub", "cocktail bar", "lounge", "nightclub"],
        "templates": ["dark_atmospheric", "drinks_menu", "events_calendar", "vip_reservation", "gallery_nightlife"]
    },
    "bakery": {
        "keywords": ["bakery", "pastry", "bread", "baked goods"],
        "templates": ["product_showcase", "daily_specials", "order_online", "warm_inviting", "gallery_delicious"]
    },
    "food_truck": {
        "keywords": ["food truck", "mobile food", "street food"],
        "templates": ["location_tracker", "menu_simple", "social_focused", "colorful_fun", "event_booking"]
    },
    "hotel": {
        "keywords": ["hotel", "resort", "accommodation", "lodging", "inn"],
        "templates": ["booking_system", "room_showcase", "amenities_featured", "luxury_imagery", "virtual_tour"]
    },
    "catering": {
        "keywords": ["catering", "event catering", "food service"],
        "templates": ["package_showcase", "event_types", "menu_options", "gallery_events", "quote_request"]
    },
    
    # E-commerce & Retail
    "ecommerce": {
        "keywords": ["shop", "store", "ecommerce", "online store", "buy", "sell"],
        "templates": ["product_grid", "featured_collections", "cart_prominent", "search_filter", "minimal_shop"]
    },
    "fashion": {
        "keywords": ["fashion", "clothing", "apparel", "boutique", "wear"],
        "templates": ["lookbook_style", "collection_showcase", "editorial_layout", "model_focused", "minimalist_luxury"]
    },
    "jewelry": {
        "keywords": ["jewelry", "jeweler", "diamonds", "rings", "necklaces"],
        "templates": ["luxury_showcase", "product_zoom", "collection_elegant", "dark_premium", "detail_focused"]
    },
    "furniture": {
        "keywords": ["furniture", "home furnishings", "decor"],
        "templates": ["room_sets", "product_360", "style_guide", "catalog_grid", "inspiration_board"]
    },
    "electronics": {
        "keywords": ["electronics", "gadgets", "tech store", "devices"],
        "templates": ["product_specs", "comparison_tool", "dark_tech", "feature_highlight", "reviews_prominent"]
    },
    
    # Education & Training
    "online_course": {
        "keywords": ["course", "online learning", "education", "training", "class"],
        "templates": ["course_catalog", "instructor_led", "progress_dashboard", "video_focused", "certification_path"]
    },
    "tutoring": {
        "keywords": ["tutoring", "tutor", "private lessons", "academic help"],
        "templates": ["subject_showcase", "tutor_profiles", "booking_sessions", "testimonial_based", "results_focused"]
    },
    "school": {
        "keywords": ["school", "academy", "college", "university", "educational institution"],
        "templates": ["program_showcase", "admissions_focused", "campus_tour", "faculty_directory", "student_portal"]
    },
    "driving_school": {
        "keywords": ["driving school", "drivers ed", "driving lessons"],
        "templates": ["package_options", "instructor_profiles", "booking_system", "trust_safety", "testimonials"]
    },
    
    # Creative & Media
    "photography": {
        "keywords": ["photography", "photographer", "photo", "portrait", "wedding photography"],
        "templates": ["full_screen_gallery", "portfolio_masonry", "package_pricing", "about_artist", "booking_inquiry"]
    },
    "videography": {
        "keywords": ["videography", "video production", "filmmaker", "video"],
        "templates": ["video_showcase", "reel_featured", "services_packages", "client_portfolio", "cinematic_dark"]
    },
    "music": {
        "keywords": ["music", "musician", "band", "artist", "singer"],
        "templates": ["audio_player", "tour_dates", "discography", "media_kit", "dark_stage"]
    },
    "art_gallery": {
        "keywords": ["art", "gallery", "artist", "paintings", "sculpture"],
        "templates": ["exhibition_showcase", "artist_statement", "collection_grid", "virtual_gallery", "minimal_white"]
    },
    "podcast": {
        "keywords": ["podcast", "podcasting", "show", "episodes"],
        "templates": ["episode_player", "guest_showcase", "subscribe_focused", "transcript_readable", "dark_audio"]
    },
    
    # Technology & IT
    "software_company": {
        "keywords": ["software company", "software development", "tech company"],
        "templates": ["product_showcase", "case_studies", "team_technical", "dark_code", "integration_focus"]
    },
    "app": {
        "keywords": ["app", "mobile app", "application", "software"],
        "templates": ["app_showcase", "feature_screens", "download_cta", "testimonial_ratings", "video_demo"]
    },
    "web_design": {
        "keywords": ["web design", "website design", "web development"],
        "templates": ["portfolio_websites", "process_timeline", "package_pricing", "client_showcase", "modern_creative"]
    },
    "it_services": {
        "keywords": ["it services", "it support", "managed services", "network"],
        "templates": ["service_packages", "response_time", "trust_security", "business_focused", "support_portal"]
    },
    "cybersecurity": {
        "keywords": ["cybersecurity", "security", "data protection", "cyber"],
        "templates": ["threat_focus", "protection_services", "dark_secure", "compliance_badges", "audit_services"]
    },
    
    # Home Services
    "plumbing": {
        "keywords": ["plumbing", "plumber", "pipe", "drain"],
        "templates": ["emergency_24_7", "service_areas", "common_problems", "trust_licensed", "booking_system"]
    },
    "electrical": {
        "keywords": ["electrical", "electrician", "wiring", "electric"],
        "templates": ["service_showcase", "emergency_available", "residential_commercial", "trust_certified", "safety_focused"]
    },
    "hvac": {
        "keywords": ["hvac", "heating", "cooling", "air conditioning", "furnace"],
        "templates": ["seasonal_services", "maintenance_plans", "emergency_repair", "energy_efficiency", "financing_options"]
    },
    "cleaning": {
        "keywords": ["cleaning", "maid service", "housekeeping", "janitorial"],
        "templates": ["service_packages", "booking_online", "recurring_plans", "satisfaction_guarantee", "before_after"]
    },
    "pest_control": {
        "keywords": ["pest control", "exterminator", "pest removal"],
        "templates": ["pest_types", "treatment_methods", "emergency_service", "prevention_tips", "guarantee_featured"]
    },
    "locksmith": {
        "keywords": ["locksmith", "lock service", "keys"],
        "templates": ["emergency_24_7", "services_residential", "automotive_locks", "trust_security", "quick_response"]
    },
    "moving": {
        "keywords": ["moving", "movers", "relocation", "moving company"],
        "templates": ["quote_calculator", "service_areas", "packing_services", "testimonials_trust", "booking_date"]
    },
    "painting": {
        "keywords": ["painting", "painter", "paint contractor"],
        "templates": ["color_consultation", "project_gallery", "interior_exterior", "before_after", "quote_request"]
    },
    
    # Automotive
    "auto_repair": {
        "keywords": ["auto repair", "mechanic", "car repair", "automotive"],
        "templates": ["services_list", "appointment_booking", "trust_certified", "warranty_guarantee", "location_map"]
    },
    "car_dealership": {
        "keywords": ["car dealership", "auto sales", "used cars", "new cars"],
        "templates": ["inventory_grid", "search_filters", "financing_options", "trade_in_value", "virtual_tour"]
    },
    "car_wash": {
        "keywords": ["car wash", "auto detailing", "car cleaning"],
        "templates": ["package_options", "membership_plans", "location_hours", "before_after", "colorful_clean"]
    },
    "towing": {
        "keywords": ["towing", "tow truck", "roadside assistance"],
        "templates": ["emergency_call", "service_areas", "24_7_available", "pricing_transparent", "quick_response"]
    },
    
    # Personal Services
    "barber": {
        "keywords": ["barber", "barbershop", "haircut", "men's grooming"],
        "templates": ["services_menu", "booking_online", "barber_profiles", "gallery_styles", "vintage_modern"]
    },
    "salon": {
        "keywords": ["salon", "hair salon", "beauty salon"],
        "templates": ["services_menu", "stylist_profiles", "booking_system", "gallery_transformations", "elegant_feminine"]
    },
    "tattoo": {
        "keywords": ["tattoo", "tattoo shop", "tattoo artist"],
        "templates": ["artist_portfolio", "style_showcase", "booking_consultation", "dark_artistic", "gallery_full"]
    },
    "pet_grooming": {
        "keywords": ["pet grooming", "dog grooming", "pet care"],
        "templates": ["service_packages", "before_after", "booking_online", "cute_friendly", "testimonials_pets"]
    },
    "life_coach": {
        "keywords": ["life coach", "coaching", "personal development"],
        "templates": ["about_approach", "testimonials_transformation", "booking_session", "minimal_inspiring", "video_intro"]
    },
    
    # Professional Services
    "insurance": {
        "keywords": ["insurance", "insurance agency", "coverage"],
        "templates": ["coverage_types", "quote_request", "trust_protected", "claims_process", "agent_profiles"]
    },
    "mortgage": {
        "keywords": ["mortgage", "home loan", "mortgage broker"],
        "templates": ["calculator_featured", "loan_types", "application_process", "rates_comparison", "trust_licensed"]
    },
    "financial_advisor": {
        "keywords": ["financial advisor", "wealth management", "investment"],
        "templates": ["services_comprehensive", "about_advisor", "client_results", "trust_certified", "consultation_booking"]
    },
    "tax_preparation": {
        "keywords": ["tax preparation", "tax service", "tax filing"],
        "templates": ["services_individual", "deadline_focused", "deductions_tips", "secure_upload", "pricing_packages"]
    },
    
    # Entertainment & Events
    "event_planning": {
        "keywords": ["event planning", "event planner", "party planning"],
        "templates": ["portfolio_events", "services_types", "vendor_network", "testimonials_celebrations", "inquiry_form"]
    },
    "wedding": {
        "keywords": ["wedding", "wedding planner", "bridal"],
        "templates": ["package_options", "vendor_directory", "gallery_romantic", "planning_timeline", "elegant_luxe"]
    },
    "dj": {
        "keywords": ["dj", "disc jockey", "entertainment"],
        "templates": ["music_genres", "event_types", "equipment_list", "booking_inquiry", "dark_energetic"]
    },
    "venue": {
        "keywords": ["venue", "event space", "banquet hall"],
        "templates": ["space_showcase", "capacity_details", "amenities_list", "virtual_tour", "booking_calendar"]
    },
    
    # Non-Profit & Community
    "nonprofit": {
        "keywords": ["nonprofit", "charity", "foundation", "organization"],
        "templates": ["mission_focused", "donation_prominent", "impact_stories", "volunteer_signup", "transparent_minimal"]
    },
    "church": {
        "keywords": ["church", "ministry", "congregation", "faith"],
        "templates": ["service_times", "sermon_archive", "events_calendar", "community_groups", "donation_tithe"]
    },
    
    # Blog & Content
    "blog": {
        "keywords": ["blog", "blogger", "articles", "posts"],
        "templates": ["post_grid", "featured_article", "sidebar_categories", "author_bio", "readable_typography"]
    },
    "news": {
        "keywords": ["news", "magazine", "journalism", "publication"],
        "templates": ["headline_focused", "category_sections", "breaking_news", "article_dense", "newspaper_layout"]
    },
    "portfolio": {
        "keywords": ["portfolio", "showcase", "work", "projects"],
        "templates": ["grid_masonry", "full_screen_slides", "case_studies", "about_creative", "minimal_modern"]
    },
    
    # Travel & Tourism
    "travel_agency": {
        "keywords": ["travel", "travel agency", "tour", "vacation"],
        "templates": ["destination_showcase", "package_deals", "booking_system", "testimonials_trips", "inspiring_imagery"]
    },
    "tour_guide": {
        "keywords": ["tour guide", "tours", "sightseeing"],
        "templates": ["tour_options", "itinerary_detailed", "booking_calendar", "reviews_prominent", "local_expertise"]
    },
    
    # Sports & Recreation
    "sports_team": {
        "keywords": ["sports team", "team", "league", "club"],
        "templates": ["schedule_prominent", "roster_players", "stats_dashboard", "tickets_merch", "team_colors"]
    },
    "recreation_center": {
        "keywords": ["recreation", "community center", "activities"],
        "templates": ["facility_showcase", "programs_classes", "membership_info", "calendar_events", "family_friendly"]
    }
}

def detect_website_type(prompt: str) -> str:
    """Detect website type from user prompt using keyword matching"""
    prompt_lower = prompt.lower()
    
    # Score each type based on keyword matches
    scores = {}
    for type_name, type_data in WEBSITE_TYPES.items():
        score = 0
        for keyword in type_data["keywords"]:
            if keyword in prompt_lower:
                # Longer keywords get higher score (more specific)
                score += len(keyword.split())
        
        if score > 0:
            scores[type_name] = score
    
    # Return type with highest score
    if scores:
        best_type = max(scores.items(), key=lambda x: x[1])[0]
        return best_type
    
    # Default fallback
    return "saas"

def get_templates_for_type(website_type: str) -> list:
    """Get available template variations for a website type"""
    type_data = WEBSITE_TYPES.get(website_type, WEBSITE_TYPES["saas"])
    return type_data["templates"]
