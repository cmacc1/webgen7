"""
TEMPLATE LIBRARY - 20+ Completely Different Website Architectures
Each template has UNIQUE layout, navigation, hero style, and structure
"""

import random

TEMPLATES = [
    {
        "name": "Sidebar Navigation",
        "id": "sidebar_nav",
        "structure": "Fixed left sidebar with scrollable content area",
        "navigation": "Vertical sidebar (fixed left, always visible, logo at top, links below)",
        "hero": "Split screen - text left, visual right (or full-width gradient)",
        "sections": "Full-width content area with right margin for sidebar",
        "unique_elements": ["Fixed left navigation", "Scrollspy highlighting", "Smooth horizontal transitions"]
    },
    {
        "name": "Top Bar Sticky",
        "id": "topbar_sticky",
        "structure": "Sticky top navigation with dropdown menus",
        "navigation": "Horizontal top bar (sticky on scroll, centered logo or left-aligned)",
        "hero": "Full-screen background with centered content or diagonal split",
        "sections": "Traditional stacked sections with alternating backgrounds",
        "unique_elements": ["Mega dropdown menus", "Search bar in nav", "Progress indicator on scroll"]
    },
    {
        "name": "Hamburger Mobile-First",
        "id": "hamburger_mobile",
        "structure": "Hidden menu with hamburger icon, slides in from left",
        "navigation": "Hamburger icon top-right, slides in full-screen menu overlay",
        "hero": "Vertical stacked hero with prominent CTA",
        "sections": "Card-based mobile-first design, stacks vertically",
        "unique_elements": ["Animated hamburger icon", "Full-screen menu overlay", "Bottom tab bar"]
    },
    {
        "name": "Split Screen Dual",
        "id": "split_dual",
        "structure": "Permanent 50/50 split - left for navigation, right for content",
        "navigation": "Left half: vertical nav + branding, Right half: scrollable content",
        "hero": "Integrated into split (left: text, right: visual)",
        "sections": "Right panel scrolls while left stays fixed",
        "unique_elements": ["Permanent split layout", "Left panel fixed", "Parallax on right"]
    },
    {
        "name": "Centered Minimal",
        "id": "centered_minimal",
        "structure": "Narrow centered column (max-w-3xl), lots of whitespace",
        "navigation": "Centered logo + centered horizontal nav links",
        "hero": "Minimal centered text with subtle background",
        "sections": "All content in narrow column, generous padding",
        "unique_elements": ["Minimalist design", "Typography-focused", "Subtle animations"]
    },
    {
        "name": "Grid Dashboard",
        "id": "grid_dashboard",
        "structure": "Bento box grid layout with cards",
        "navigation": "Top bar with logo left, menu icons right",
        "hero": "Large grid card spanning 2x2 or full-width",
        "sections": "CSS Grid with varying card sizes (1x1, 2x1, 1x2)",
        "unique_elements": ["Bento box layout", "Interactive cards", "Hover state changes"]
    },
    {
        "name": "Timeline Vertical",
        "id": "timeline_vertical",
        "structure": "Vertical timeline down the center with content alternating left/right",
        "navigation": "Fixed top bar with transparent background",
        "hero": "Centered title with timeline starting below",
        "sections": "Timeline with dots, lines connecting content cards left and right",
        "unique_elements": ["Visual timeline", "Alternating content", "Scroll-triggered animations"]
    },
    {
        "name": "Horizontal Scroll",
        "id": "horizontal_scroll",
        "structure": "Sections scroll horizontally with snap points",
        "navigation": "Fixed top bar with section indicators",
        "hero": "First horizontal panel",
        "sections": "Each section is a full-viewport horizontal panel",
        "unique_elements": ["Horizontal scroll", "Snap scrolling", "Dot navigation"]
    },
    {
        "name": "Card Masonry",
        "id": "card_masonry",
        "structure": "Pinterest-style masonry layout with varying card heights",
        "navigation": "Floating pill-shaped nav at top",
        "hero": "Large featured card at top left",
        "sections": "Masonry grid with cards of different heights",
        "unique_elements": ["Masonry layout", "Hover zoom", "Lightbox gallery"]
    },
    {
        "name": "Asymmetric Brutalist",
        "id": "asymmetric_brutal",
        "structure": "Bold asymmetric layout with overlapping elements",
        "navigation": "Large text links, unconventional placement (top-left vertical or bottom)",
        "hero": "Overlapping text and shapes, diagonal elements",
        "sections": "Sections overlap, rotated elements, bold typography",
        "unique_elements": ["Brutalist design", "Overlapping sections", "Bold colors and shapes"]
    },
    {
        "name": "Tabbed Interface",
        "id": "tabbed_interface",
        "structure": "Main content area with tab navigation",
        "navigation": "Top bar with prominent tab navigation below",
        "hero": "Full-width banner above tabs",
        "sections": "Each tab loads different content (about, services, pricing, contact)",
        "unique_elements": ["Tab navigation", "Content switching", "Active state indicators"]
    },
    {
        "name": "Parallax Storytelling",
        "id": "parallax_story",
        "structure": "Full-screen sections with parallax backgrounds",
        "navigation": "Fixed transparent nav with section dots on right",
        "hero": "First full-screen parallax section",
        "sections": "Each section is full-screen with different parallax speeds",
        "unique_elements": ["Parallax scrolling", "Section dots navigation", "Opacity transitions"]
    },
    {
        "name": "Accordion Expansion",
        "id": "accordion_expand",
        "structure": "Vertical accordion sections that expand on click",
        "navigation": "Minimal top bar",
        "hero": "First expanded accordion",
        "sections": "Clickable headers expand to reveal content, others collapse",
        "unique_elements": ["Accordion sections", "Smooth expand/collapse", "Icon rotation"]
    },
    {
        "name": "Floating Sidebar",
        "id": "floating_sidebar",
        "structure": "Content in center, floating sidebar appears on right on scroll",
        "navigation": "Top horizontal bar",
        "hero": "Full-width hero",
        "sections": "As you scroll, floating sidebar appears with quick links/CTA",
        "unique_elements": ["Floating sidebar on scroll", "Quick action bar", "Sticky CTA"]
    },
    {
        "name": "Magazine Layout",
        "id": "magazine_layout",
        "structure": "Multi-column layout like a magazine/newspaper",
        "navigation": "Top masthead with horizontal nav",
        "hero": "Large featured story with image left, headline right",
        "sections": "2-3 column article layout with images and text",
        "unique_elements": ["Multi-column text", "Drop caps", "Pull quotes"]
    },
    {
        "name": "Bottom Navigation",
        "id": "bottom_nav",
        "structure": "Navigation fixed at bottom like mobile app",
        "navigation": "Fixed bottom bar with icon + label navigation",
        "hero": "Full-screen with content starting just below top",
        "sections": "Swipeable sections with bottom nav tabs",
        "unique_elements": ["Bottom tab bar", "Mobile app style", "Swipe gestures"]
    },
    {
        "name": "Diagonal Sections",
        "id": "diagonal_sections",
        "structure": "Sections separated by diagonal dividers",
        "navigation": "Top bar",
        "hero": "Hero with diagonal bottom edge",
        "sections": "Each section has diagonal top/bottom edges using clip-path",
        "unique_elements": ["Diagonal dividers", "Clip-path shapes", "Overlapping colors"]
    },
    {
        "name": "Circles and Curves",
        "id": "circles_curves",
        "structure": "Circular elements, curved sections, organic shapes",
        "navigation": "Circular logo, curved nav bar",
        "hero": "Circular hero with curved bottom edge",
        "sections": "Sections with border-radius, circular image frames, wave dividers",
        "unique_elements": ["Circular design", "Wave dividers", "Organic shapes"]
    },
    {
        "name": "Neumorphism Style",
        "id": "neumorphism",
        "structure": "Soft UI with subtle shadows and highlights",
        "navigation": "Neumorphic top bar with soft shadows",
        "hero": "Neumorphic cards with inner/outer shadows",
        "sections": "Soft, tactile design with light gray backgrounds",
        "unique_elements": ["Neumorphic shadows", "Soft tactile design", "Subtle depth"]
    },
    {
        "name": "Glassmorphism Modern",
        "id": "glassmorphism",
        "structure": "Glass effect with backdrop blur and transparency",
        "navigation": "Transparent nav with backdrop-blur",
        "hero": "Glass cards floating over background",
        "sections": "Semi-transparent sections with blur effects",
        "unique_elements": ["Backdrop blur", "Glass transparency", "Floating elements"]
    }
]

COLOR_SCHEMES = [
    {"name": "Midnight Purple", "primary": "#7C3AED", "secondary": "#DB2777", "accent": "#F59E0B", "bg": "#0F172A"},
    {"name": "Ocean Blue", "primary": "#0EA5E9", "secondary": "#06B6D4", "accent": "#10B981", "bg": "#F0F9FF"},
    {"name": "Forest Green", "primary": "#059669", "secondary": "#10B981", "accent": "#F59E0B", "bg": "#F0FDF4"},
    {"name": "Sunset Orange", "primary": "#F97316", "secondary": "#FB923C", "accent": "#FDE047", "bg": "#FFF7ED"},
    {"name": "Rose Pink", "primary": "#EC4899", "secondary": "#F472B6", "accent": "#FDE047", "bg": "#FFF1F2"},
    {"name": "Slate Gray", "primary": "#64748B", "secondary": "#94A3B8", "accent": "#0EA5E9", "bg": "#F8FAFC"},
    {"name": "Emerald Teal", "primary": "#14B8A6", "secondary": "#2DD4BF", "accent": "#FCD34D", "bg": "#F0FDFA"},
    {"name": "Violet Dream", "primary": "#8B5CF6", "secondary": "#A78BFA", "accent": "#F472B6", "bg": "#FAF5FF"},
    {"name": "Crimson Red", "primary": "#DC2626", "secondary": "#EF4444", "accent": "#FCD34D", "bg": "#FEF2F2"},
    {"name": "Indigo Night", "primary": "#4F46E5", "secondary": "#6366F1", "accent": "#34D399", "bg": "#EEF2FF"}
]

TYPOGRAPHY_STYLES = [
    {"name": "Modern Sans", "heading": "font-family: 'Inter', sans-serif", "body": "font-family: 'Inter', sans-serif"},
    {"name": "Classic Serif", "heading": "font-family: 'Playfair Display', serif", "body": "font-family: 'Source Sans Pro', sans-serif"},
    {"name": "Tech Mono", "heading": "font-family: 'Space Grotesk', sans-serif", "body": "font-family: 'JetBrains Mono', monospace"},
    {"name": "Elegant Script", "heading": "font-family: 'Cormorant Garamond', serif", "body": "font-family: 'Lato', sans-serif"},
    {"name": "Bold Display", "heading": "font-family: 'Bebas Neue', sans-serif", "body": "font-family: 'Roboto', sans-serif"}
]

def get_random_template():
    """Get a completely random template configuration"""
    template = random.choice(TEMPLATES)
    colors = random.choice(COLOR_SCHEMES)
    typography = random.choice(TYPOGRAPHY_STYLES)
    
    return {
        "template": template,
        "colors": colors,
        "typography": typography,
        "template_id": f"{template['id']}_{colors['name'].replace(' ', '_').lower()}_{random.randint(1000, 9999)}"
    }

def get_template_specific_instructions(template_config):
    """Generate specific CSS/HTML instructions for this template"""
    template = template_config["template"]
    colors = template_config["colors"]
    
    instructions = f"""
🎨 TEMPLATE ARCHITECTURE: {template['name'].upper()}
ID: {template_config['template_id']}

📐 STRUCTURE REQUIREMENTS:
{template['structure']}

🧭 NAVIGATION STYLE:
{template['navigation']}

🎭 HERO STYLE:
{template['hero']}

📄 SECTION LAYOUT:
{template['sections']}

✨ UNIQUE ELEMENTS TO IMPLEMENT:
{chr(10).join(['- ' + elem for elem in template['unique_elements']])}

🎨 COLOR SCHEME: {colors['name']}
- Primary: {colors['primary']}
- Secondary: {colors['secondary']}
- Accent: {colors['accent']}
- Background: {colors['bg']}

CRITICAL: This template structure is MANDATORY. Do NOT create a generic top-nav website.
Follow the navigation style, hero style, and section layout EXACTLY as specified above.
"""
    
    return instructions

def validate_template_variety(generated_html, template_config):
    """Validate that generated HTML matches the template structure"""
    template = template_config["template"]
    template_id = template["id"]
    
    checks = {
        "has_unique_structure": False,
        "matches_template": False,
        "template_id": template_id
    }
    
    # Check for template-specific markers
    if template_id == "sidebar_nav":
        checks["has_unique_structure"] = "fixed" in generated_html.lower() and "sidebar" in generated_html.lower()
    elif template_id == "split_dual":
        checks["has_unique_structure"] = "grid-cols-2" in generated_html or "w-1/2" in generated_html
    elif template_id == "horizontal_scroll":
        checks["has_unique_structure"] = "overflow-x" in generated_html or "snap-x" in generated_html
    elif template_id == "timeline_vertical":
        checks["has_unique_structure"] = "timeline" in generated_html.lower()
    
    return checks
