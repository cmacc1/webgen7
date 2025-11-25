"""
TEMPLATE DEFINITIONS - 5 Unique Variations Per Website Type
Each template has specific layout, features, and characteristics
"""

TEMPLATE_DEFINITIONS = {
    # Universal Templates (can be used for any type)
    "modern_dashboard": {
        "name": "Modern Dashboard",
        "layout": "Sidebar navigation with main content area",
        "navigation": "Fixed left sidebar (240px) with logo, menu items, user profile at bottom",
        "hero": "Dashboard header with stats cards and welcome message",
        "features": ["Collapsible sidebar", "Dark/light mode toggle", "Stat cards", "Charts/graphs", "Data tables"],
        "colors": "Professional blues and grays with accent colors",
        "best_for": "SaaS, Analytics, Admin panels, Business tools"
    },
    
    "minimalist_tech": {
        "name": "Minimalist Tech",
        "layout": "Top navigation with centered content, max-width container",
        "navigation": "Minimal top bar with logo left, 3-4 links right",
        "hero": "Large typography hero with gradient background",
        "features": ["Whitespace-heavy", "Sans-serif typography", "Micro-interactions", "Smooth scrolling"],
        "colors": "Monochrome with one accent color",
        "best_for": "Tech startups, SaaS, Modern businesses"
    },
    
    "gradient_hero": {
        "name": "Gradient Hero",
        "layout": "Full-width sections with alternating backgrounds",
        "navigation": "Transparent nav that becomes solid on scroll",
        "hero": "Full-screen animated gradient with centered content",
        "features": ["Animated gradients", "Glass-morphism cards", "Floating elements", "Particle effects"],
        "colors": "Vibrant gradients (purple/pink, blue/cyan)",
        "best_for": "Creative agencies, SaaS, Modern products"
    },
    
    "dark_mode_pro": {
        "name": "Dark Mode Professional",
        "layout": "Dark theme with high contrast elements",
        "navigation": "Dark top bar with subtle borders",
        "hero": "Dark background with neon accent colors",
        "features": ["Dark backgrounds", "Neon accents", "Code-like aesthetic", "Terminal-style elements"],
        "colors": "Dark grays/blacks with bright accents",
        "best_for": "Tech products, Developer tools, Gaming, Modern brands"
    },
    
    "glassmorphism_app": {
        "name": "Glassmorphism App",
        "layout": "Overlapping glass-effect cards on colorful background",
        "navigation": "Glass nav bar with backdrop-blur",
        "hero": "Large glass card with blur effect",
        "features": ["Backdrop-blur effects", "Semi-transparent elements", "Soft shadows", "Layered design"],
        "colors": "Soft pastels with transparency",
        "best_for": "Modern apps, Creative products, Design-forward brands"
    },
    
    # Portfolio/Creative Templates
    "portfolio_grid": {
        "name": "Portfolio Grid",
        "layout": "3-column grid of project cards",
        "navigation": "Minimal top nav or sidebar filter",
        "hero": "Featured project full-width with overlay text",
        "features": ["Filterable grid", "Hover effects", "Lightbox gallery", "Project details"],
        "colors": "Depends on projects, neutral background",
        "best_for": "Designers, Photographers, Creative agencies"
    },
    
    "full_screen_showcase": {
        "name": "Full Screen Showcase",
        "layout": "One project per screen, scroll to see next",
        "navigation": "Minimal dots navigation on side",
        "hero": "First project fills entire viewport",
        "features": ["Snap scrolling", "Full-screen images", "Minimal text", "Case study detail pages"],
        "colors": "High contrast, bold",
        "best_for": "High-end agencies, Luxury brands, Photography"
    },
    
    "split_screen_bold": {
        "name": "Split Screen Bold",
        "layout": "50/50 split - image left, content right (or vice versa)",
        "navigation": "Integrated into split or minimal top",
        "hero": "Full-height split with large image and bold text",
        "features": ["Fixed split", "Parallax on image side", "Bold typography", "Color blocks"],
        "colors": "Bold, contrasting colors",
        "best_for": "Creative agencies, Portfolios, Product launches"
    },
    
    "masonry_projects": {
        "name": "Masonry Projects",
        "layout": "Pinterest-style masonry grid with varying heights",
        "navigation": "Sticky top bar",
        "hero": "Large hero image with overlay",
        "features": ["Masonry layout", "Infinite scroll", "Quick view", "Category filters"],
        "colors": "Neutral with colorful projects",
        "best_for": "Photographers, Design studios, Creative portfolios"
    },
    
    "timeline_work": {
        "name": "Timeline Work",
        "layout": "Vertical timeline with projects alternating left/right",
        "navigation": "Fixed top or sidebar",
        "hero": "Timeline starts with introduction",
        "features": ["Visual timeline", "Chronological", "Scroll animations", "Milestone highlights"],
        "colors": "Professional with timeline accent",
        "best_for": "Agencies, Consultants, Experience showcase"
    },
    
    # Professional/Corporate Templates
    "professional_corporate": {
        "name": "Professional Corporate",
        "layout": "Traditional layout with header, content, sidebar, footer",
        "navigation": "Top bar with dropdown menus",
        "hero": "Banner with professional image and tagline",
        "features": ["Dropdown menus", "Breadcrumbs", "Sidebar widgets", "Professional imagery"],
        "colors": "Blues, grays, corporate colors",
        "best_for": "Law firms, Accounting, Consulting, B2B"
    },
    
    "executive_minimal": {
        "name": "Executive Minimal",
        "layout": "Clean, spacious layout with max-width content",
        "navigation": "Simple top nav with logo and 4-5 links",
        "hero": "Large image with subtle overlay and centered text",
        "features": ["Whitespace", "Professional fonts", "Subtle animations", "Trust signals"],
        "colors": "Navy, gray, gold accents",
        "best_for": "Executive coaching, High-end consulting, Professional services"
    },
    
    "trust_builder": {
        "name": "Trust Builder",
        "layout": "Traditional with prominent trust signals",
        "navigation": "Top bar with phone number and CTAs",
        "hero": "Professional team photo with credentials",
        "features": ["Certifications", "Testimonials", "Team bios", "Awards", "Case studies"],
        "colors": "Professional blues and whites",
        "best_for": "Legal, Medical, Financial, Professional services"
    },
    
    "expertise_showcase": {
        "name": "Expertise Showcase",
        "layout": "Content-heavy with sidebars for navigation",
        "navigation": "Top bar plus left sidebar for deep navigation",
        "hero": "Expertise statement with background image",
        "features": ["Resource library", "Blog integration", "Deep navigation", "Author profiles"],
        "colors": "Professional with readable contrast",
        "best_for": "Consulting, Education, Thought leadership"
    },
    
    "sidebar_services": {
        "name": "Sidebar Services",
        "layout": "Left sidebar with service categories, main content area",
        "navigation": "Sidebar navigation (expandable/collapsible sections)",
        "hero": "Banner with breadcrumb navigation",
        "features": ["Expandable sidebar", "Service pages", "Contact forms", "Resource downloads"],
        "colors": "Professional, trust-building",
        "best_for": "Service businesses, B2B, Professional firms"
    },
    
    # E-commerce Templates
    "product_grid": {
        "name": "Product Grid",
        "layout": "Header with search, product grid, filters sidebar",
        "navigation": "Top bar with cart icon, search bar",
        "hero": "Banner with current promotion or featured collection",
        "features": ["Product grid", "Quick view", "Cart sidebar", "Filters", "Sort options"],
        "colors": "Clean, product-focused",
        "best_for": "E-commerce, Online stores, Product catalogs"
    },
    
    "featured_collections": {
        "name": "Featured Collections",
        "layout": "Large featured product sections with lifestyle imagery",
        "navigation": "Top bar with mega menu",
        "hero": "Full-width lifestyle image with product",
        "features": ["Collection showcases", "Lifestyle imagery", "Product carousels", "Editorial content"],
        "colors": "Brand-specific, high-end",
        "best_for": "Fashion, Lifestyle brands, Premium products"
    },
    
    # Booking/Service Templates
    "appointment_focused": {
        "name": "Appointment Focused",
        "layout": "Prominent booking widget with service info",
        "navigation": "Simple top bar",
        "hero": "Large CTA for booking with available times",
        "features": ["Booking calendar", "Time slots", "Service selection", "Provider profiles"],
        "colors": "Trust-building blues and greens",
        "best_for": "Medical, Dental, Services, Consultations"
    },
    
    "booking_system": {
        "name": "Booking System",
        "layout": "Calendar/availability front and center",
        "navigation": "Minimal top nav",
        "hero": "Date picker and service selector",
        "features": ["Real-time availability", "Multiple services", "Add-ons", "Customer accounts"],
        "colors": "Professional and trustworthy",
        "best_for": "Salons, Spas, Services, Appointments"
    },
    
    # Real Estate Templates
    "property_showcase": {
        "name": "Property Showcase",
        "layout": "Large property images with details sidebar",
        "navigation": "Top bar with search",
        "hero": "Featured property with key details",
        "features": ["Image galleries", "Property details", "Map integration", "Virtual tours", "Inquiry forms"],
        "colors": "Premium, professional",
        "best_for": "Real estate, Property management"
    },
    
    "map_integrated": {
        "name": "Map Integrated",
        "layout": "Split view - map on left, listings on right",
        "navigation": "Top bar with filters",
        "hero": "Map and listings split view",
        "features": ["Interactive map", "Map markers", "List/map toggle", "Filters", "Save favorites"],
        "colors": "Clean, map-focused",
        "best_for": "Real estate, Location-based services"
    },
    
    # Restaurant/Food Templates
    "menu_showcase": {
        "name": "Menu Showcase",
        "layout": "Menu sections with food imagery",
        "navigation": "Top bar with menu categories",
        "hero": "Food photography hero with tagline",
        "features": ["Menu sections", "Food photos", "Prices", "Dietary icons", "Order online"],
        "colors": "Warm, appetizing",
        "best_for": "Restaurants, Cafes, Food services"
    },
    
    "reservation_system": {
        "name": "Reservation System",
        "layout": "Booking widget prominent with restaurant info",
        "navigation": "Simple top nav",
        "hero": "Restaurant ambiance photo with reservation widget",
        "features": ["Table booking", "Party size", "Time selection", "Special requests"],
        "colors": "Elegant, sophisticated",
        "best_for": "Fine dining, Restaurants, Events"
    },
    
    # Membership/Plans Templates
    "membership_plans": {
        "name": "Membership Plans",
        "layout": "Pricing tiers front and center",
        "navigation": "Simple top bar",
        "hero": "Plan comparison with sign-up CTAs",
        "features": ["Plan comparison", "Feature checkmarks", "Pricing toggle", "Sign-up flow"],
        "colors": "Clear, professional",
        "best_for": "Gyms, SaaS, Membership sites, Subscriptions"
    },
    
    # Gallery Templates
    "before_after_gallery": {
        "name": "Before/After Gallery",
        "layout": "Before/after slider showcase",
        "navigation": "Top bar",
        "hero": "Featured before/after with slider",
        "features": ["Image comparison slider", "Gallery grid", "Project details", "Testimonials"],
        "colors": "Professional, trustworthy",
        "best_for": "Renovations, Transformations, Services"
    },
    
    # Profile/Authentication Templates
    "profile_dashboard": {
        "name": "Profile Dashboard",
        "layout": "User dashboard with sidebar navigation",
        "navigation": "Sidebar with user profile section",
        "hero": "Welcome header with user name and avatar",
        "features": ["User profile", "Settings", "Activity feed", "Notifications", "Preferences"],
        "colors": "Clean, modern",
        "best_for": "SaaS, Membership sites, User portals"
    },
    
    "auth_focused": {
        "name": "Auth Focused",
        "layout": "Split screen - form on left, imagery/benefits on right",
        "navigation": "Minimal logo and help link",
        "hero": "Sign-up/login form with benefits list",
        "features": ["Email/password", "Social login", "Remember me", "Password reset", "Email verification"],
        "colors": "Brand colors with trust signals",
        "best_for": "SaaS, Apps, Membership sites"
    }
}

def get_template_definition(template_key: str) -> dict:
    """Get detailed template definition"""
    return TEMPLATE_DEFINITIONS.get(template_key, TEMPLATE_DEFINITIONS["modern_dashboard"])

def select_best_template(website_type: str, prompt: str, available_templates: list) -> str:
    """Select best template based on prompt analysis"""
    prompt_lower = prompt.lower()
    
    # Keyword-based template selection
    if any(word in prompt_lower for word in ["booking", "appointment", "schedule", "reservation"]):
        if "appointment_focused" in available_templates:
            return "appointment_focused"
        if "booking_system" in available_templates:
            return "booking_system"
    
    if any(word in prompt_lower for word in ["portfolio", "work", "projects", "showcase"]):
        if "portfolio_grid" in available_templates:
            return "portfolio_grid"
        if "masonry_projects" in available_templates:
            return "masonry_projects"
    
    if any(word in prompt_lower for word in ["shop", "store", "buy", "products", "sell"]):
        if "product_grid" in available_templates:
            return "product_grid"
    
    if any(word in prompt_lower for word in ["menu", "food", "restaurant", "dining"]):
        if "menu_showcase" in available_templates:
            return "menu_showcase"
    
    if any(word in prompt_lower for word in ["membership", "plans", "pricing", "tiers", "subscription"]):
        if "membership_plans" in available_templates:
            return "membership_plans"
    
    if any(word in prompt_lower for word in ["modern", "minimal", "clean"]):
        if "minimalist_tech" in available_templates:
            return "minimalist_tech"
    
    if any(word in prompt_lower for word in ["dark", "gaming", "tech"]):
        if "dark_mode_pro" in available_templates:
            return "dark_mode_pro"
    
    if any(word in prompt_lower for word in ["property", "real estate", "homes", "listings"]):
        if "property_showcase" in available_templates:
            return "property_showcase"
    
    if any(word in prompt_lower for word in ["before after", "transformation", "renovation"]):
        if "before_after_gallery" in available_templates:
            return "before_after_gallery"
    
    # Default to first available template
    return available_templates[0] if available_templates else "modern_dashboard"
