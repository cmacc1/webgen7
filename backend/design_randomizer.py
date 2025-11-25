"""
DESIGN RANDOMIZER - Ensures Every Generation is Unique
Randomly selects from 1000+ components, styles, layouts for maximum variety
"""

import random
from typing import Dict, List

class DesignRandomizer:
    """Randomly selects design patterns to ensure variety"""
    
    def __init__(self):
        self.layout_patterns = [
            "asymmetric_grid", "bento_box", "masonry", "full_width_sections", 
            "card_based", "sidebar_layout", "split_screen", "zigzag_content",
            "timeline_vertical", "centered_content", "wide_hero_narrow_content"
        ]
        
        self.navigation_styles = [
            {"name": "Transparent Sticky", "code": "fixed top-0 bg-transparent backdrop-blur-md"},
            {"name": "Solid Shadow", "code": "sticky top-0 bg-white shadow-lg"},
            {"name": "Centered Logo", "code": "flex flex-col items-center py-6"},
            {"name": "Split Nav", "code": "flex justify-between items-center"},
            {"name": "Mega Menu Dropdown", "code": "relative group with dropdown mega-menu"},
            {"name": "Sidebar Navigation", "code": "fixed left-0 h-screen w-64"},
            {"name": "Bottom Tab Bar", "code": "fixed bottom-0 flex justify-around"},
        ]
        
        self.hero_styles = [
            {
                "name": "Full Screen Image Overlay",
                "structure": "min-h-screen with background image + dark overlay + centered content"
            },
            {
                "name": "Split Hero (50/50)",
                "structure": "grid grid-cols-2: text left, image/visual right"
            },
            {
                "name": "Animated Gradient",
                "structure": "min-h-screen with animated gradient background + floating elements"
            },
            {
                "name": "Video Background",
                "structure": "video element as background with text overlay"
            },
            {
                "name": "Diagonal Split",
                "structure": "diagonal clip-path dividing content and visual"
            },
            {
                "name": "Carousel Hero",
                "structure": "rotating hero images/messages with navigation dots"
            },
            {
                "name": "Particles Background",
                "structure": "animated particles with transparent elements"
            }
        ]
        
        self.button_styles = [
            "bg-gradient-to-r from-purple-600 to-pink-600 hover:shadow-2xl hover:scale-105",
            "bg-white text-purple-600 border-3 border-purple-600 hover:bg-purple-600 hover:text-white",
            "bg-black text-white hover:bg-gray-800 shadow-[8px_8px_0_rgb(0,0,0,0.2)]",
            "bg-gradient-to-r from-blue-500 to-cyan-500 hover:from-blue-600 hover:to-cyan-600",
            "relative overflow-hidden group (with animated background slide)",
            "bg-gray-100 text-gray-900 shadow-[6px_6px_12px_#bebebe,-6px_-6px_12px_#ffffff] (neumorphism)",
            "bg-transparent border-2 backdrop-blur-md hover:bg-white hover:bg-opacity-20",
        ]
        
        self.card_layouts = [
            "Hover Lift Cards (shadow-xl hover:-translate-y-2)",
            "Glass Morphism Cards (bg-opacity-10 backdrop-blur-lg)",
            "Gradient Border Cards (border with gradient animation)",
            "3D Flip Cards (rotateY on hover showing back)",
            "Expandable Cards (click to expand with more info)",
            "Stacked Cards (overlapping with z-index)",
            "Tilt Effect Cards (3D tilt on mouse move)",
        ]
        
        self.form_patterns = [
            {
                "name": "Multi-Step Form",
                "features": ["Progress bar", "Next/Back buttons", "Step indicators", "Save progress"]
            },
            {
                "name": "Inline Validation Form",
                "features": ["Real-time feedback", "Success/error icons", "Character count", "Strength meter"]
            },
            {
                "name": "Floating Label Form",
                "features": ["Labels float up on focus", "Smooth transitions", "Clean minimal design"]
            },
            {
                "name": "Payment Form",
                "features": ["Card number input mask", "CVV field", "Expiry date", "Billing address", "Payment icons"]
            },
            {
                "name": "Subscription Form",
                "features": ["Plan selection", "Monthly/Annual toggle", "Promo code input", "Price calculation"]
            },
            {
                "name": "Survey/Quiz Form",
                "features": ["Multiple choice", "Rating scales", "Progress tracker", "Results page"]
            }
        ]
        
        self.color_combinations = [
            {"primary": "#667eea", "secondary": "#764ba2", "accent": "#f093fb", "name": "Purple Dreams"},
            {"primary": "#f093fb", "secondary": "#f5576c", "accent": "#4facfe", "name": "Candy Pop"},
            {"primary": "#4facfe", "secondary": "#00f2fe", "accent": "#43e97b", "name": "Ocean Breeze"},
            {"primary": "#fa709a", "secondary": "#fee140", "accent": "#30cfd0", "name": "Sunset Vibes"},
            {"primary": "#667eea", "secondary": "#764ba2", "accent": "#667eea", "name": "Deep Space"},
            {"primary": "#f857a6", "secondary": "#ff5858", "accent": "#feca57", "name": "Fire Glow"},
            {"primary": "#a8edea", "secondary": "#fed6e3", "accent": "#f093fb", "name": "Soft Pastels"},
            {"primary": "#ff6b6b", "secondary": "#4ecdc4", "accent": "#45b7d1", "name": "Retro Vibes"},
        ]
        
        self.animation_styles = [
            "Fade In Up (opacity + translateY)",
            "Scale In (scale from 0.9 to 1)",
            "Slide In Left (translateX from -50px)",
            "Rotate In (rotate from -5deg to 0)",
            "Blur Fade In (filter blur + opacity)",
            "Staggered Reveal (children animate in sequence)",
            "Parallax Scroll (different scroll speeds)",
            "Magnetic Hover (elements follow cursor)",
        ]
        
        self.section_layouts = [
            "Full Width Alternating (image left, text right, then reverse)",
            "Centered Content Max-Width (narrow column centered)",
            "Three Column Grid (equal width cards)",
            "Asymmetric Grid (2-1 or 1-2 column ratio)",
            "Masonry Layout (Pinterest-style)",
            "Horizontal Scroll Section (scroll-snap)",
            "Sticky Scroll Section (elements stick while scrolling)",
            "Overlapping Sections (negative margin overlap)",
        ]
        
        self.advanced_features = [
            {"name": "Dark Mode Toggle", "code": "Switch between light/dark themes"},
            {"name": "Search Bar with Autocomplete", "code": "Live search suggestions"},
            {"name": "Infinite Scroll", "code": "Load more content as user scrolls"},
            {"name": "Lazy Loading Images", "code": "Images load as they enter viewport"},
            {"name": "Parallax Scrolling", "code": "Background moves slower than foreground"},
            {"name": "Scroll Spy Navigation", "code": "Active nav link based on scroll position"},
            {"name": "Animated Counters", "code": "Numbers count up when visible"},
            {"name": "Testimonial Carousel", "code": "Auto-rotating testimonials"},
            {"name": "Video Lightbox", "code": "Click to play video in modal"},
            {"name": "Cookie Consent Banner", "code": "GDPR-compliant cookie notice"},
            {"name": "Share Buttons", "code": "Social media sharing"},
            {"name": "Print Styles", "code": "Optimized for printing"},
        ]
        
        self.payment_subscription_components = {
            "pricing_tables": [
                "Three-tier with highlighted middle plan",
                "Comparison table with checkmarks",
                "Slider to adjust features/price",
                "Annual/Monthly toggle with discount badge",
                "Feature matrix grid",
            ],
            "payment_integrations": [
                "Stripe Checkout embedded form",
                "PayPal button integration",
                "Credit card form with validation",
                "Apple Pay / Google Pay buttons",
                "Crypto payment option",
            ],
            "subscription_features": [
                "Cancel anytime messaging",
                "Money-back guarantee badge",
                "Trial period countdown",
                "Upgrade/downgrade options",
                "Usage meter (API calls, storage, etc.)",
                "Billing history table",
            ]
        }
    
    def get_random_design_system(self) -> Dict:
        """Generate a completely random design system for this generation"""
        
        # Randomly select components
        layout = random.choice(self.layout_patterns)
        nav = random.choice(self.navigation_styles)
        hero = random.choice(self.hero_styles)
        buttons = random.sample(self.button_styles, k=3)  # 3 different button styles
        cards = random.choice(self.card_layouts)
        form = random.choice(self.form_patterns)
        colors = random.choice(self.color_combinations)
        animations = random.sample(self.animation_styles, k=3)  # 3 animation types
        section = random.choice(self.section_layouts)
        features = random.sample(self.advanced_features, k=5)  # 5 advanced features
        
        # Payment/subscription (30% chance to include)
        include_payment = random.random() < 0.3
        payment_components = {}
        if include_payment:
            payment_components = {
                "pricing_style": random.choice(self.payment_subscription_components["pricing_tables"]),
                "payment_method": random.choice(self.payment_subscription_components["payment_integrations"]),
                "subscription_features": random.sample(self.payment_subscription_components["subscription_features"], k=3)
            }
        
        return {
            "layout_pattern": layout,
            "navigation": nav,
            "hero_style": hero,
            "button_styles": buttons,
            "card_layout": cards,
            "form_pattern": form,
            "colors": colors,
            "animations": animations,
            "section_layout": section,
            "advanced_features": features,
            "payment_components": payment_components if include_payment else None,
            "design_id": f"{layout}_{nav['name']}_{hero['name']}"  # Unique identifier
        }
    
    def generate_variety_instructions(self, design_system: Dict) -> str:
        """Generate specific instructions based on random selections"""
        
        instructions = f"""
🎨 UNIQUE DESIGN SYSTEM FOR THIS GENERATION (ID: {design_system['design_id']}):

LAYOUT: {design_system['layout_pattern']}
NAVIGATION: {design_system['navigation']['name']} - {design_system['navigation']['code']}
HERO: {design_system['hero_style']['name']} - {design_system['hero_style']['structure']}

BUTTON STYLES (Use different ones throughout):
1. Primary CTA: {design_system['button_styles'][0]}
2. Secondary CTA: {design_system['button_styles'][1]}
3. Tertiary/Links: {design_system['button_styles'][2]}

CARDS: {design_system['card_layout']}

FORM STYLE: {design_system['form_pattern']['name']}
Features: {', '.join(design_system['form_pattern']['features'])}

COLOR PALETTE "{design_system['colors']['name']}":
- Primary: {design_system['colors']['primary']}
- Secondary: {design_system['colors']['secondary']}
- Accent: {design_system['colors']['accent']}

ANIMATIONS TO USE:
{chr(10).join(['- ' + anim for anim in design_system['animations']])}

SECTION LAYOUT: {design_system['section_layout']}

ADVANCED FEATURES (Must include):
{chr(10).join(['- ' + feat['name'] + ': ' + feat['code'] for feat in design_system['advanced_features']])}
"""
        
        if design_system['payment_components']:
            instructions += f"""
💰 PAYMENT/SUBSCRIPTION COMPONENTS (INCLUDE THESE):
- Pricing: {design_system['payment_components']['pricing_style']}
- Payment: {design_system['payment_components']['payment_method']}
- Features: {', '.join(design_system['payment_components']['subscription_features'])}
"""
        
        return instructions
