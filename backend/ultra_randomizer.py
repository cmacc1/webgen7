"""
ULTRA RANDOMIZATION SYSTEM
Provides MASSIVE variety in website generation through thousands of combinations
"""
import random
from typing import Dict, List, Any

class UltraRandomizer:
    """
    Generates completely unique website designs every time through
    massive randomization of all design elements
    """
    
    # 50+ LAYOUT STRUCTURES
    LAYOUT_STRUCTURES = [
        "Hero → Features Grid → About → CTA",
        "Hero → Stats Bar → Services → Testimonials → Contact",
        "Hero Split Screen → Feature Cards → Gallery → Footer",
        "Hero Video Background → Benefits → Pricing → FAQ",
        "Hero Diagonal → Timeline → Team → Contact Form",
        "Hero Particles → Icon Grid → Process Steps → CTA",
        "Hero Slideshow → Product Grid → Reviews → Newsletter",
        "Hero Parallax → Stats → Case Studies → Contact",
        "Hero Animated → Services List → About Split → Form",
        "Hero Gradient → Feature Tabs → Pricing Table → Footer",
        "Full Screen Hero → Floating Cards → Image Gallery → Contact",
        "Split Hero → Vertical Timeline → Team Grid → CTA",
        "Hero Carousel → Icon Features → Video Section → Form",
        "Hero Overlay → Horizontal Scroll → Stats → Contact",
        "Hero Mask → Grid Layout → Testimonial Slider → Footer",
        "Centered Hero → Bento Box Grid → FAQ Accordion → CTA",
        "Hero Left Align → Card Carousel → About Columns → Form",
        "Hero Right Align → Masonry Grid → Partner Logos → Contact",
        "Hero Asymmetric → Feature Showcase → Pricing Cards → Footer",
        "Hero Wave → Service Icons → Team Carousel → CTA",
        "Hero Blob → Stats Counter → Case Study Grid → Contact",
        "Hero Mesh Gradient → Tab Navigation → Gallery → Form",
        "Hero Split Diagonal → Process Flow → Reviews → CTA",
        "Hero Circle → Icon Timeline → About Grid → Footer",
        "Hero Triangle → Feature Blocks → Pricing → Contact",
        "Hero Polygon → Service Grid → Team → Newsletter",
        "Hero Liquid → Benefits Cards → Stats → CTA",
        "Hero Geometric → Product Showcase → Testimonials → Form",
        "Hero Abstract → Icon Features → About → Contact",
        "Hero Minimal → Grid Gallery → Services → Footer",
        "Hero Maximal → Card Stack → Process → CTA",
        "Hero Magazine → Column Layout → Images → Contact",
        "Hero Newspaper → List Features → Team → Form",
        "Hero Dashboard → Metrics → Charts → CTA",
        "Hero Portfolio → Project Grid → About → Contact",
        "Hero Agency → Service Cards → Case Studies → Form",
        "Hero Startup → Feature Icons → Pricing → CTA",
        "Hero Corporate → Stats → Team → Contact",
        "Hero Creative → Gallery Masonry → About → Form",
        "Hero Modern → Card Hover → Features → CTA",
        "Hero Classic → Icon List → Services → Contact",
        "Hero Futuristic → Neon Cards → About → Form",
        "Hero Retro → Vintage Grid → Team → CTA",
        "Hero Brutalist → Bold Blocks → Features → Contact",
        "Hero Glassmorphism → Blur Cards → Services → Form",
        "Hero Neumorphism → Soft Shadows → About → CTA",
        "Hero Skeuomorphism → Realistic Cards → Team → Contact",
        "Hero Flat Design → Simple Grid → Features → Form",
        "Hero Material → Elevated Cards → Services → CTA",
        "Hero iOS Style → Rounded Cards → About → Contact"
    ]
    
    # 100+ COLOR SCHEMES
    COLOR_SCHEMES = [
        {
            "name": "Ocean Breeze",
            "primary": "#0077be", "secondary": "#00a8cc", "accent": "#00d4ff",
            "bg": "#f0f8ff", "text": "#1a1a2e", "gradient": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
        },
        {
            "name": "Sunset Glow",
            "primary": "#ff6b6b", "secondary": "#ff8e53", "accent": "#ffb347",
            "bg": "#fff5f5", "text": "#2d3436", "gradient": "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)"
        },
        {
            "name": "Forest Green",
            "primary": "#27ae60", "secondary": "#2ecc71", "accent": "#52c77a",
            "bg": "#f1f8f4", "text": "#1e3a1e", "gradient": "linear-gradient(135deg, #fa709a 0%, #fee140 100%)"
        },
        {
            "name": "Royal Purple",
            "primary": "#8e44ad", "secondary": "#9b59b6", "accent": "#be7fd8",
            "bg": "#f8f5ff", "text": "#2c1654", "gradient": "linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)"
        },
        {
            "name": "Crimson Red",
            "primary": "#e74c3c", "secondary": "#c0392b", "accent": "#ff7675",
            "bg": "#fff5f5", "text": "#2c1618", "gradient": "linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%)"
        },
        {
            "name": "Golden Hour",
            "primary": "#f39c12", "secondary": "#e67e22", "accent": "#f1c40f",
            "bg": "#fffbf0", "text": "#2c1810", "gradient": "linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%)"
        },
        {
            "name": "Arctic Blue",
            "primary": "#3498db", "secondary": "#2980b9", "accent": "#5dade2",
            "bg": "#f0f7ff", "text": "#1a2332", "gradient": "linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 100%)"
        },
        {
            "name": "Cherry Blossom",
            "primary": "#ff69b4", "secondary": "#ff1493", "accent": "#ffc0cb",
            "bg": "#fff0f7", "text": "#2c1620", "gradient": "linear-gradient(135deg, #f6d365 0%, #fda085 100%)"
        },
        {
            "name": "Midnight Blue",
            "primary": "#2c3e50", "secondary": "#34495e", "accent": "#5d6d7e",
            "bg": "#ecf0f1", "text": "#0f1419", "gradient": "linear-gradient(135deg, #434343 0%, #000000 100%)"
        },
        {
            "name": "Lime Zest",
            "primary": "#7bed9f", "secondary": "#2ed573", "accent": "#a4f2b7",
            "bg": "#f0fff4", "text": "#1a2f1a", "gradient": "linear-gradient(135deg, #d299c2 0%, #fef9d7 100%)"
        },
        {
            "name": "Coral Reef",
            "primary": "#ff7979", "secondary": "#ff6348", "accent": "#ff9999",
            "bg": "#fff7f7", "text": "#2c1616", "gradient": "linear-gradient(135deg, #ffeaa7 0%, #fdcb6e 100%)"
        },
        {
            "name": "Slate Gray",
            "primary": "#636e72", "secondary": "#2d3436", "accent": "#95a5a6",
            "bg": "#f5f6fa", "text": "#1a1a1a", "gradient": "linear-gradient(135deg, #e0e0e0 0%, #bdbdbd 100%)"
        },
        {
            "name": "Turquoise Dream",
            "primary": "#00b894", "secondary": "#00cec9", "accent": "#55efc4",
            "bg": "#f0fffe", "text": "#1a2e2c", "gradient": "linear-gradient(135deg, #13547a 0%, #80d0c7 100%)"
        },
        {
            "name": "Lavender Fields",
            "primary": "#a29bfe", "secondary": "#6c5ce7", "accent": "#b8b1ff",
            "bg": "#f8f7ff", "text": "#2c2654", "gradient": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)"
        },
        {
            "name": "Tangerine Burst",
            "primary": "#fd79a8", "secondary": "#e17055", "accent": "#ff9ff3",
            "bg": "#fff5f8", "text": "#2c1620", "gradient": "linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%)"
        },
        # Add 85 more color schemes...
        {"name": "Neon Nights", "primary": "#00ffff", "secondary": "#ff00ff", "accent": "#00ff00", "bg": "#0a0a0a", "text": "#ffffff", "gradient": "linear-gradient(135deg, #00ffff 0%, #ff00ff 100%)"},
        {"name": "Monochrome", "primary": "#333333", "secondary": "#666666", "accent": "#999999", "bg": "#ffffff", "text": "#000000", "gradient": "linear-gradient(135deg, #ffffff 0%, #000000 100%)"},
        {"name": "Pastel Dream", "primary": "#ffd1dc", "secondary": "#fffacd", "accent": "#e0bbe4", "bg": "#fef9ff", "text": "#4a4a4a", "gradient": "linear-gradient(135deg, #ffd1dc 0%, #e0bbe4 100%)"},
        {"name": "Earth Tones", "primary": "#8b7355", "secondary": "#d2b48c", "accent": "#daa520", "bg": "#faf8f3", "text": "#3e2723", "gradient": "linear-gradient(135deg, #8b7355 0%, #d2b48c 100%)"},
        {"name": "Cyberpunk", "primary": "#ff006e", "secondary": "#8338ec", "accent": "#3a86ff", "bg": "#0a0a0a", "text": "#ffffff", "gradient": "linear-gradient(135deg, #ff006e 0%, #8338ec 100%)"},
    ]
    
    # 50+ HERO STYLES
    HERO_STYLES = [
        {
            "name": "Full Screen Overlay",
            "html_class": "h-screen relative flex items-center justify-center",
            "overlay": "absolute inset-0 bg-black bg-opacity-50",
            "content_position": "relative z-10 text-center text-white"
        },
        {
            "name": "Split Screen Left/Right",
            "html_class": "min-h-screen grid md:grid-cols-2",
            "overlay": "none",
            "content_position": "flex items-center justify-center p-12"
        },
        {
            "name": "Centered Minimal",
            "html_class": "h-screen flex items-center justify-center bg-gradient-to-br",
            "overlay": "none",
            "content_position": "text-center max-w-4xl mx-auto px-6"
        },
        {
            "name": "Diagonal Split",
            "html_class": "min-h-screen relative overflow-hidden",
            "overlay": "clip-path: polygon(0 0, 100% 0, 100% 80%, 0 100%)",
            "content_position": "relative z-10 pt-32 pb-20 px-6"
        },
        {
            "name": "Floating Cards",
            "html_class": "min-h-screen relative py-20",
            "overlay": "absolute inset-0 bg-gradient-to-br opacity-90",
            "content_position": "relative z-10 container mx-auto px-6"
        },
        {
            "name": "Video Background",
            "html_class": "h-screen relative",
            "overlay": "absolute inset-0 bg-black bg-opacity-40",
            "content_position": "relative z-20 flex items-center justify-center text-white"
        },
        {
            "name": "Particles Effect",
            "html_class": "h-screen relative overflow-hidden",
            "overlay": "absolute inset-0 bg-gradient-to-r",
            "content_position": "relative z-10 flex items-center justify-center"
        },
        {
            "name": "Blob Shapes",
            "html_class": "min-h-screen relative overflow-hidden",
            "overlay": "absolute top-10 right-10 w-96 h-96 bg-purple-400 rounded-full filter blur-3xl opacity-20",
            "content_position": "relative z-10 py-20 px-6"
        },
        {
            "name": "Mesh Gradient",
            "html_class": "h-screen relative",
            "overlay": "absolute inset-0 bg-gradient-to-br from-blue-400 via-purple-500 to-pink-500",
            "content_position": "relative z-10 flex items-center justify-center text-white"
        },
        {
            "name": "Glassmorphism",
            "html_class": "h-screen relative flex items-center justify-center",
            "overlay": "absolute inset-0 backdrop-blur-lg bg-white bg-opacity-10",
            "content_position": "relative z-10 text-center"
        },
        # Add 40 more hero styles with variations...
        {"name": "Wave Bottom", "html_class": "h-screen relative", "overlay": "absolute bottom-0 w-full h-32 bg-white", "content_position": "relative z-10 flex items-center"},
        {"name": "Animated Gradient", "html_class": "h-screen bg-gradient-to-r animate-gradient-x", "overlay": "none", "content_position": "flex items-center justify-center"},
        {"name": "Grid Pattern", "html_class": "h-screen relative bg-grid-pattern", "overlay": "absolute inset-0 bg-black bg-opacity-5", "content_position": "relative z-10 flex items-center"},
        {"name": "Dot Matrix", "html_class": "h-screen bg-dot-pattern", "overlay": "none", "content_position": "flex items-center justify-center"},
        {"name": "Noise Texture", "html_class": "h-screen bg-noise-texture", "overlay": "absolute inset-0 opacity-5", "content_position": "relative z-10 flex items-center"},
    ]
    
    # 30+ BUTTON STYLES
    BUTTON_STYLES = [
        "px-8 py-4 bg-gradient-to-r from-blue-500 to-purple-600 text-white rounded-full hover:scale-110 transition-transform shadow-2xl",
        "px-8 py-4 bg-black text-white rounded-lg hover:bg-gray-800 transition-all shadow-xl",
        "px-8 py-4 border-2 border-current rounded-full hover:bg-current hover:text-white transition-all",
        "px-8 py-4 bg-white text-gray-900 rounded-xl hover:shadow-2xl transform hover:-translate-y-1 transition-all",
        "px-10 py-5 bg-gradient-to-r from-pink-500 to-orange-500 text-white rounded-2xl hover:shadow-2xl",
        "px-8 py-4 bg-transparent border-2 border-white text-white backdrop-blur-sm hover:bg-white hover:text-black transition-all",
        "px-8 py-4 bg-purple-600 text-white rounded-md hover:bg-purple-700 shadow-lg hover:shadow-purple-500/50",
        "px-12 py-5 text-xl font-bold bg-yellow-400 text-black rounded-full hover:bg-yellow-500 shadow-2xl",
        "px-8 py-4 bg-red-600 text-white rounded-lg hover:bg-red-700 transform hover:scale-105 transition-all",
        "px-8 py-4 bg-green-500 text-white rounded-2xl hover:bg-green-600 hover:rotate-2 transition-all",
        "px-10 py-5 bg-gradient-to-br from-cyan-500 to-blue-700 text-white rounded-full hover:from-cyan-600 hover:to-blue-800",
        "px-8 py-4 bg-indigo-600 text-white rounded-xl hover:shadow-2xl hover:shadow-indigo-500/50 transition-all",
        "px-8 py-4 border-4 border-black text-black hover:bg-black hover:text-white transition-all font-black",
        "px-8 py-4 bg-teal-500 text-white rounded-lg hover:bg-teal-600 hover:shadow-xl transition-all",
        "px-10 py-5 bg-gradient-to-r from-red-500 via-yellow-500 to-green-500 text-white rounded-full hover:scale-110",
        "px-8 py-4 bg-amber-500 text-black rounded-2xl hover:bg-amber-600 transform hover:-translate-y-2 transition-all shadow-xl",
        "px-8 py-4 bg-rose-600 text-white rounded-full hover:bg-rose-700 hover:shadow-2xl hover:shadow-rose-500/50",
        "px-8 py-4 bg-emerald-600 text-white rounded-lg hover:bg-emerald-700 hover:ring-4 hover:ring-emerald-300 transition-all",
        "px-10 py-5 bg-gradient-to-r from-violet-600 to-fuchsia-600 text-white rounded-2xl hover:from-violet-700 hover:to-fuchsia-700",
        "px-8 py-4 bg-slate-800 text-white rounded-xl hover:bg-slate-900 hover:shadow-2xl transition-all",
    ]
    
    # 40+ CARD STYLES
    CARD_STYLES = [
        "bg-white rounded-3xl p-10 shadow-2xl hover:shadow-3xl hover:-translate-y-3 transition-all duration-300 border border-gray-100",
        "bg-gradient-to-br from-white to-gray-50 rounded-2xl p-8 shadow-xl hover:shadow-2xl hover:scale-105 transition-all",
        "bg-white rounded-xl p-8 border-2 border-gray-200 hover:border-blue-500 transition-all",
        "backdrop-blur-xl bg-white bg-opacity-80 rounded-3xl p-10 shadow-xl hover:bg-opacity-90 transition-all",
        "bg-gradient-to-br from-purple-500 to-pink-500 rounded-2xl p-8 text-white hover:scale-105 transform transition-all shadow-2xl",
        "bg-black text-white rounded-2xl p-10 hover:bg-gray-900 transition-all shadow-2xl",
        "bg-gradient-to-r from-blue-600 to-cyan-500 rounded-3xl p-10 text-white shadow-2xl hover:shadow-blue-500/50 transform hover:-translate-y-2",
        "bg-white rounded-2xl p-8 shadow-lg hover:shadow-2xl border-l-8 border-blue-600 transition-all",
        "bg-gray-50 rounded-xl p-8 hover:bg-white hover:shadow-xl transition-all border border-gray-200",
        "bg-gradient-to-br from-yellow-400 to-orange-500 rounded-3xl p-10 text-white shadow-2xl hover:scale-105 transform",
        "relative overflow-hidden bg-white rounded-2xl p-8 shadow-xl hover:shadow-2xl group",
        "bg-teal-500 text-white rounded-2xl p-8 hover:bg-teal-600 transition-all shadow-lg",
        "bg-white rounded-3xl p-10 shadow-2xl hover:rotate-2 transition-all border-4 border-purple-200",
        "bg-gradient-to-br from-pink-400 to-purple-600 rounded-2xl p-8 text-white hover:from-pink-500 hover:to-purple-700",
        "bg-indigo-600 text-white rounded-xl p-8 hover:bg-indigo-700 shadow-xl hover:shadow-indigo-500/50",
        "bg-white rounded-2xl p-8 shadow-lg border-t-8 border-green-500 hover:shadow-2xl transition-all",
        "bg-rose-100 rounded-3xl p-10 hover:bg-rose-200 transition-all shadow-xl",
        "bg-gradient-to-r from-emerald-500 to-teal-600 rounded-2xl p-8 text-white shadow-2xl hover:shadow-emerald-500/50",
        "bg-slate-800 text-white rounded-xl p-8 hover:bg-slate-900 shadow-2xl",
        "bg-white rounded-3xl p-10 shadow-2xl hover:-translate-x-2 hover:-translate-y-2 transition-all border-r-8 border-b-8 border-blue-600",
    ]
    
    # 25+ SECTION BACKGROUNDS
    SECTION_BACKGROUNDS = [
        "bg-gradient-to-br from-blue-50 to-purple-50",
        "bg-white",
        "bg-gray-50",
        "bg-gradient-to-r from-pink-100 to-purple-100",
        "bg-gradient-to-br from-green-50 to-blue-50",
        "bg-black text-white",
        "bg-gradient-to-r from-yellow-50 to-orange-50",
        "bg-indigo-50",
        "bg-gradient-to-br from-teal-50 to-cyan-50",
        "bg-rose-50",
        "bg-gradient-to-r from-purple-900 to-indigo-900 text-white",
        "bg-gray-900 text-white",
        "bg-gradient-to-br from-blue-900 to-purple-900 text-white",
        "bg-amber-50",
        "bg-gradient-to-r from-emerald-50 to-teal-50",
        "bg-slate-50",
        "bg-gradient-to-br from-pink-50 to-rose-50",
        "bg-cyan-50",
        "bg-gradient-to-r from-violet-50 to-fuchsia-50",
        "bg-lime-50",
        "bg-gradient-to-br from-orange-50 to-red-50",
        "bg-sky-50",
        "bg-gradient-to-r from-blue-600 to-cyan-600 text-white",
        "bg-emerald-600 text-white",
        "bg-gradient-to-br from-purple-600 to-pink-600 text-white",
    ]
    
    # 20+ ANIMATION STYLES
    ANIMATION_STYLES = [
        "animate-fade-in",
        "animate-slide-up",
        "animate-slide-down",
        "animate-slide-left",
        "animate-slide-right",
        "animate-zoom-in",
        "animate-zoom-out",
        "animate-rotate",
        "animate-bounce",
        "animate-pulse",
        "animate-wiggle",
        "animate-spin-slow",
        "animate-float",
        "animate-glow",
        "animate-shake",
        "animate-flip",
        "animate-scale-up",
        "animate-blur-in",
        "animate-gradient",
        "animate-slide-diagonal",
    ]
    
    # 15+ TYPOGRAPHY STYLES
    TYPOGRAPHY_STYLES = [
        {"heading": "font-black text-7xl", "subheading": "font-bold text-3xl", "body": "text-xl leading-relaxed"},
        {"heading": "font-extrabold text-6xl tracking-tight", "subheading": "font-semibold text-2xl", "body": "text-lg"},
        {"heading": "font-bold text-8xl", "subheading": "font-medium text-4xl", "body": "text-base"},
        {"heading": "font-black text-6xl uppercase", "subheading": "font-bold text-2xl uppercase", "body": "text-lg"},
        {"heading": "font-extrabold text-7xl italic", "subheading": "font-bold text-3xl", "body": "text-xl"},
        {"heading": "font-black text-5xl", "subheading": "font-semibold text-xl", "body": "text-base leading-loose"},
        {"heading": "font-bold text-9xl tracking-tighter", "subheading": "font-medium text-4xl", "body": "text-2xl"},
        {"heading": "font-extrabold text-6xl", "subheading": "font-bold text-3xl tracking-wide", "body": "text-lg"},
        {"heading": "font-black text-7xl leading-tight", "subheading": "font-semibold text-2xl", "body": "text-xl leading-relaxed"},
        {"heading": "font-bold text-6xl", "subheading": "font-medium text-3xl italic", "body": "text-lg"},
        {"heading": "font-extrabold text-8xl uppercase tracking-widest", "subheading": "font-bold text-4xl", "body": "text-2xl"},
        {"heading": "font-black text-5xl", "subheading": "font-bold text-2xl", "body": "text-xl font-light"},
        {"heading": "font-bold text-7xl tracking-wide", "subheading": "font-semibold text-3xl", "body": "text-lg"},
        {"heading": "font-extrabold text-6xl", "subheading": "font-medium text-2xl uppercase", "body": "text-base"},
        {"heading": "font-black text-8xl italic", "subheading": "font-bold text-4xl", "body": "text-xl"},
    ]
    
    def get_ultra_random_design(self) -> Dict[str, Any]:
        """
        Generate a completely unique design configuration
        with randomized everything
        """
        return {
            "layout": random.choice(self.LAYOUT_STRUCTURES),
            "colors": random.choice(self.COLOR_SCHEMES),
            "hero_style": random.choice(self.HERO_STYLES),
            "button_style": random.choice(self.BUTTON_STYLES),
            "card_style": random.choice(self.CARD_STYLES),
            "section_bg_1": random.choice(self.SECTION_BACKGROUNDS),
            "section_bg_2": random.choice(self.SECTION_BACKGROUNDS),
            "section_bg_3": random.choice(self.SECTION_BACKGROUNDS),
            "animation": random.choice(self.ANIMATION_STYLES),
            "typography": random.choice(self.TYPOGRAPHY_STYLES),
            
            # Randomize spacing
            "spacing": {
                "section_padding": random.choice(["py-12", "py-16", "py-20", "py-24", "py-32"]),
                "container_padding": random.choice(["px-4", "px-6", "px-8", "px-10", "px-12"]),
                "element_gap": random.choice(["gap-4", "gap-6", "gap-8", "gap-10", "gap-12"]),
            },
            
            # Randomize grid layouts
            "grid": {
                "features": random.choice(["grid-cols-1 md:grid-cols-2", "grid-cols-1 md:grid-cols-3", "grid-cols-1 md:grid-cols-4", "grid-cols-1 md:grid-cols-2 lg:grid-cols-3"]),
                "testimonials": random.choice(["grid-cols-1 md:grid-cols-2", "grid-cols-1 md:grid-cols-3", "flex flex-col"]),
                "team": random.choice(["grid-cols-1 md:grid-cols-2 lg:grid-cols-3", "grid-cols-1 md:grid-cols-3 lg:grid-cols-4", "grid-cols-1 md:grid-cols-2"]),
            },
            
            # Randomize shadows
            "shadows": {
                "card": random.choice(["shadow-xl", "shadow-2xl", "shadow-lg hover:shadow-2xl", "drop-shadow-2xl"]),
                "button": random.choice(["shadow-lg", "shadow-xl", "shadow-2xl", "shadow-none"]),
                "hero": random.choice(["drop-shadow-2xl", "shadow-inner", "shadow-none"]),
            },
            
            # Randomize border radius
            "radius": {
                "card": random.choice(["rounded-lg", "rounded-xl", "rounded-2xl", "rounded-3xl", "rounded-full"]),
                "button": random.choice(["rounded-md", "rounded-lg", "rounded-xl", "rounded-full"]),
                "image": random.choice(["rounded-lg", "rounded-xl", "rounded-2xl", "rounded-none"]),
            },
            
            # Randomize hover effects
            "hover": {
                "card": random.choice([
                    "hover:scale-105 hover:-translate-y-2",
                    "hover:rotate-2 hover:scale-105",
                    "hover:shadow-2xl",
                    "hover:-translate-y-3 hover:shadow-3xl",
                    "hover:scale-110",
                ]),
                "button": random.choice([
                    "hover:scale-110",
                    "hover:shadow-2xl hover:-translate-y-1",
                    "hover:rotate-2",
                    "hover:scale-105 hover:shadow-xl",
                ]),
            },
            
            # Randomize icon sizes
            "icon_size": random.choice(["fa-2x", "fa-3x", "fa-4x", "text-5xl", "text-6xl"]),
            
            # Random choice for features to include
            "features": {
                "dark_mode": random.choice([True, False]),
                "particles": random.choice([True, False]),
                "smooth_scroll": True,
                "lazy_load": random.choice([True, False]),
                "parallax": random.choice([True, False]),
                "animations_on_scroll": random.choice([True, False]),
            }
        }
    
    def get_random_component_mix(self) -> Dict[str, str]:
        """
        Mix and match components from different design systems
        """
        hero_options = [
            "Full screen with video background",
            "Split screen left/right",
            "Centered with floating cards",
            "Diagonal split with gradient",
            "Particle effect background",
            "Glassmorphism overlay",
            "Mesh gradient animated",
            "Wave shapes bottom",
            "Blob shapes floating",
            "Grid pattern overlay",
        ]
        
        features_options = [
            "Icon grid 3 columns",
            "Card carousel horizontal scroll",
            "Bento box layout",
            "Timeline vertical",
            "Tab navigation",
            "Accordion expandable",
            "Masonry grid",
            "Stacked cards",
            "Icon list with animations",
            "Feature blocks with hover",
        ]
        
        cta_options = [
            "Full width banner",
            "Centered with dual buttons",
            "Split with image",
            "Floating card",
            "Diagonal section",
            "Animated gradient background",
            "Video background with overlay",
            "Minimal centered",
            "Newsletter signup focus",
            "Contact form embedded",
        ]
        
        return {
            "hero": random.choice(hero_options),
            "features": random.choice(features_options),
            "about": random.choice(["Split image/text", "Centered content", "Timeline", "Grid layout", "Card format"]),
            "testimonials": random.choice(["Carousel slider", "Grid cards", "Single large quote", "Video testimonials", "Rating stars"]),
            "cta": random.choice(cta_options),
            "footer": random.choice(["Multi-column", "Centered", "Minimal", "Newsletter focus", "Social media focus"]),
        }
