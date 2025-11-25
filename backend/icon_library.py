"""
ICON LIBRARY - High-Quality Icons for Every Feature Type
Maps common features/services to Font Awesome icons for clean, professional design
"""

# Feature/Service to Icon Mapping
FEATURE_ICONS = {
    # Fitness & Gym
    "personal training": "fa-dumbbell",
    "group classes": "fa-users",
    "cardio": "fa-heart-pulse",
    "strength training": "fa-dumbbell",
    "yoga": "fa-spa",
    "pilates": "fa-person-walking",
    "crossfit": "fa-dumbbell",
    "swimming": "fa-person-swimming",
    "nutrition": "fa-apple-whole",
    "weight loss": "fa-weight-scale",
    
    # Restaurant & Food
    "menu": "fa-utensils",
    "delivery": "fa-truck-fast",
    "takeout": "fa-bag-shopping",
    "catering": "fa-cake-candles",
    "reservation": "fa-calendar-check",
    "chef": "fa-hat-chef",
    "dining": "fa-plate-utensils",
    "bar": "fa-martini-glass",
    "breakfast": "fa-mug-hot",
    "lunch": "fa-burger",
    "dinner": "fa-pizza-slice",
    
    # Renovation & Construction
    "kitchen remodel": "fa-kitchen-set",
    "bathroom": "fa-shower",
    "flooring": "fa-layer-group",
    "painting": "fa-paint-roller",
    "roofing": "fa-house",
    "deck": "fa-tree",
    "landscaping": "fa-seedling",
    "plumbing": "fa-pipe",
    "electrical": "fa-bolt",
    "hvac": "fa-fan",
    "windows": "fa-window-maximize",
    
    # Tech & SaaS
    "cloud": "fa-cloud",
    "api": "fa-code",
    "analytics": "fa-chart-line",
    "security": "fa-shield-halved",
    "database": "fa-database",
    "integration": "fa-plug",
    "automation": "fa-robot",
    "ai": "fa-brain",
    "mobile": "fa-mobile-screen",
    "support": "fa-headset",
    
    # Business & Professional
    "consulting": "fa-handshake",
    "strategy": "fa-chess",
    "planning": "fa-clipboard-list",
    "management": "fa-briefcase",
    "finance": "fa-chart-pie",
    "legal": "fa-gavel",
    "accounting": "fa-calculator",
    "marketing": "fa-bullhorn",
    "sales": "fa-chart-simple",
    "hr": "fa-people-group",
    
    # Medical & Health
    "appointment": "fa-calendar-days",
    "doctor": "fa-user-doctor",
    "nurse": "fa-user-nurse",
    "pharmacy": "fa-pills",
    "surgery": "fa-syringe",
    "emergency": "fa-ambulance",
    "xray": "fa-x-ray",
    "lab": "fa-flask",
    "therapy": "fa-heart",
    "dental": "fa-tooth",
    
    # Real Estate
    "buy": "fa-house-circle-check",
    "sell": "fa-hand-holding-dollar",
    "rent": "fa-key",
    "commercial": "fa-building",
    "residential": "fa-house",
    "property": "fa-map-location-dot",
    "mortgage": "fa-file-contract",
    "inspection": "fa-magnifying-glass",
    
    # Education
    "course": "fa-book-open",
    "certificate": "fa-certificate",
    "tutorial": "fa-graduation-cap",
    "workshop": "fa-chalkboard-user",
    "exam": "fa-file-pen",
    "library": "fa-book",
    "research": "fa-microscope",
    
    # E-commerce
    "shop": "fa-cart-shopping",
    "products": "fa-box",
    "payment": "fa-credit-card",
    "shipping": "fa-truck",
    "returns": "fa-rotate-left",
    "wishlist": "fa-heart",
    "reviews": "fa-star",
    "discount": "fa-tag",
    
    # Common Features
    "contact": "fa-envelope",
    "location": "fa-location-dot",
    "phone": "fa-phone",
    "email": "fa-at",
    "chat": "fa-comment",
    "faq": "fa-circle-question",
    "pricing": "fa-dollar-sign",
    "testimonials": "fa-quote-left",
    "gallery": "fa-images",
    "video": "fa-video",
    "download": "fa-download",
    "upload": "fa-upload",
    "search": "fa-magnifying-glass",
    "filter": "fa-filter",
    "settings": "fa-gear",
    "profile": "fa-user",
    "team": "fa-users",
    "about": "fa-circle-info",
    "blog": "fa-newspaper",
    "social": "fa-share-nodes",
}

# Category-based icon sets for when specific match isn't found
CATEGORY_ICONS = {
    "fitness": ["fa-dumbbell", "fa-heart-pulse", "fa-person-running", "fa-trophy", "fa-medal"],
    "restaurant": ["fa-utensils", "fa-burger", "fa-pizza-slice", "fa-martini-glass", "fa-mug-hot"],
    "renovation": ["fa-hammer", "fa-screwdriver-wrench", "fa-paint-roller", "fa-house", "fa-ruler"],
    "tech": ["fa-laptop-code", "fa-server", "fa-cloud", "fa-microchip", "fa-code"],
    "business": ["fa-briefcase", "fa-chart-line", "fa-handshake", "fa-building", "fa-user-tie"],
    "medical": ["fa-stethoscope", "fa-heart-pulse", "fa-pills", "fa-syringe", "fa-user-doctor"],
    "education": ["fa-graduation-cap", "fa-book", "fa-chalkboard-user", "fa-pencil", "fa-lightbulb"],
    "ecommerce": ["fa-cart-shopping", "fa-bag-shopping", "fa-credit-card", "fa-box", "fa-truck"],
    "default": ["fa-check", "fa-star", "fa-heart", "fa-bolt", "fa-circle-check"]
}

def get_icon_for_feature(feature_text: str, category: str = "default") -> str:
    """
    Get the best icon for a feature based on text matching
    Returns Font Awesome icon class
    """
    feature_lower = feature_text.lower()
    
    # Try direct match first
    for keyword, icon in FEATURE_ICONS.items():
        if keyword in feature_lower:
            return icon
    
    # Fall back to category icons
    icons = CATEGORY_ICONS.get(category, CATEGORY_ICONS["default"])
    
    # Return first icon from category (can be randomized if needed)
    return icons[0]

def get_multiple_icons(features: list, category: str = "default") -> list:
    """
    Get icons for multiple features, ensuring variety
    """
    icons = []
    used_icons = set()
    
    for feature in features:
        icon = get_icon_for_feature(feature, category)
        
        # Ensure variety - don't reuse icons if possible
        if icon in used_icons and len(icons) < len(CATEGORY_ICONS.get(category, [])):
            # Try to get a different icon from category
            category_icons = CATEGORY_ICONS.get(category, CATEGORY_ICONS["default"])
            for alt_icon in category_icons:
                if alt_icon not in used_icons:
                    icon = alt_icon
                    break
        
        icons.append(icon)
        used_icons.add(icon)
    
    return icons

# Pricing/Plan Icons
PRICING_ICONS = {
    "basic": "fa-cube",
    "starter": "fa-seedling",
    "free": "fa-gift",
    "pro": "fa-rocket",
    "professional": "fa-crown",
    "premium": "fa-gem",
    "enterprise": "fa-building",
    "business": "fa-briefcase",
    "team": "fa-users",
    "unlimited": "fa-infinity"
}

# Social Media Icons
SOCIAL_ICONS = {
    "facebook": "fa-brands fa-facebook",
    "twitter": "fa-brands fa-twitter",
    "instagram": "fa-brands fa-instagram",
    "linkedin": "fa-brands fa-linkedin",
    "youtube": "fa-brands fa-youtube",
    "tiktok": "fa-brands fa-tiktok",
    "github": "fa-brands fa-github",
    "discord": "fa-brands fa-discord"
}

# Process/Step Icons
PROCESS_ICONS = [
    "fa-1", "fa-2", "fa-3", "fa-4", "fa-5", "fa-6",
    "fa-calendar-check", "fa-clipboard-list", "fa-paper-plane", 
    "fa-check-double", "fa-flag-checkered"
]

def generate_icon_html(icon_class: str, size: str = "2xl", color: str = "primary") -> str:
    """Generate HTML for a Font Awesome icon with styling"""
    return f'<i class="fa-solid {icon_class} fa-{size} text-{color}"></i>'

def generate_feature_card_with_icon(title: str, description: str, category: str = "default") -> str:
    """Generate a complete feature card with icon"""
    icon = get_icon_for_feature(title, category)
    
    return f"""
    <div class="feature-card p-6 bg-white rounded-xl shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-2">
        <div class="icon-container w-16 h-16 bg-gradient-to-br from-blue-500 to-purple-600 rounded-full flex items-center justify-center mb-4">
            <i class="fa-solid {icon} fa-2xl text-white"></i>
        </div>
        <h3 class="text-xl font-bold mb-2">{title}</h3>
        <p class="text-gray-600">{description}</p>
    </div>
    """
