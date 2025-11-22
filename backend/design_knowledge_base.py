"""
Comprehensive Design Knowledge Base for AI Website Generation
Contains best practices, patterns, and implementation guidelines
"""

# ==============================================================================
# MODERN FRAMEWORKS & LIBRARIES (CDN Links)
# ==============================================================================

FRAMEWORKS = {
    "ui_frameworks": {
        "react": {
            "cdn": ["https://unpkg.com/react@18/umd/react.production.min.js",
                   "https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"],
            "usage": "Full React applications with components",
            "when": "Complex interactive UIs, SPAs"
        },
        "vue": {
            "cdn": ["https://unpkg.com/vue@3/dist/vue.global.js"],
            "usage": "Progressive framework for building UIs",
            "when": "Data-driven interfaces, reactive apps"
        },
        "alpine": {
            "cdn": ["https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"],
            "usage": "Lightweight reactive framework",
            "when": "Simple interactions without heavy framework"
        },
        "htmx": {
            "cdn": ["https://unpkg.com/htmx.org@1.9.10"],
            "usage": "Modern interactions with HTML attributes",
            "when": "Server-side rendered with dynamic updates"
        }
    },
    
    "css_frameworks": {
        "tailwind": {
            "cdn": ["https://cdn.tailwindcss.com"],
            "usage": "Utility-first CSS framework",
            "when": "Rapid prototyping, custom designs"
        },
        "bootstrap": {
            "cdn": ["https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css",
                   "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"],
            "usage": "Component library with pre-built elements",
            "when": "Quick professional layouts"
        },
        "bulma": {
            "cdn": ["https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css"],
            "usage": "Modern CSS framework based on Flexbox",
            "when": "Clean, minimalist designs"
        }
    },
    
    "animation_libraries": {
        "gsap": {
            "cdn": ["https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.4/gsap.min.js",
                   "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.4/ScrollTrigger.min.js"],
            "usage": "Professional-grade animations",
            "when": "Complex animations, timeline-based"
        },
        "anime": {
            "cdn": ["https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"],
            "usage": "Lightweight animation library",
            "when": "SVG, DOM, CSS animations"
        },
        "motion_one": {
            "cdn": ["https://cdn.jsdelivr.net/npm/motion@10.16.2/dist/motion.js"],
            "usage": "Modern animation library",
            "when": "Web Animations API based effects"
        },
        "typed_js": {
            "cdn": ["https://cdn.jsdelivr.net/npm/typed.js@2.0.16"],
            "usage": "Typing animation",
            "when": "Hero sections, dynamic text"
        }
    },
    
    "3d_graphics": {
        "threejs": {
            "cdn": ["https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js"],
            "usage": "3D graphics and WebGL",
            "when": "3D visualizations, immersive experiences"
        },
        "p5": {
            "cdn": ["https://cdn.jsdelivr.net/npm/p5@1.7.0/lib/p5.min.js"],
            "usage": "Creative coding and generative art",
            "when": "Visual effects, interactive art"
        }
    },
    
    "charts_data_viz": {
        "chartjs": {
            "cdn": ["https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.js"],
            "usage": "Simple, flexible charts",
            "when": "Dashboards, analytics"
        },
        "apexcharts": {
            "cdn": ["https://cdn.jsdelivr.net/npm/apexcharts"],
            "usage": "Modern charting library",
            "when": "Interactive charts, real-time data"
        },
        "d3": {
            "cdn": ["https://d3js.org/d3.v7.min.js"],
            "usage": "Data-driven documents",
            "when": "Custom visualizations, complex data"
        },
        "echarts": {
            "cdn": ["https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js"],
            "usage": "Powerful charting library",
            "when": "Enterprise dashboards"
        }
    },
    
    "interaction_libraries": {
        "swiper": {
            "cdn": ["https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css",
                   "https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"],
            "usage": "Touch-enabled sliders/carousels",
            "when": "Image galleries, testimonials"
        },
        "flickity": {
            "cdn": ["https://unpkg.com/flickity@2/dist/flickity.min.css",
                   "https://unpkg.com/flickity@2/dist/flickity.pkgd.min.js"],
            "usage": "Touch carousels",
            "when": "Product showcases"
        },
        "dragula": {
            "cdn": ["https://cdn.jsdelivr.net/npm/dragula@3.7.3/dist/dragula.min.js"],
            "usage": "Drag and drop",
            "when": "Kanban boards, sortable lists"
        },
        "sortable": {
            "cdn": ["https://cdn.jsdelivr.net/npm/sortablejs@latest/Sortable.min.js"],
            "usage": "Reorderable drag-drop lists",
            "when": "List management, prioritization"
        }
    },
    
    "forms_validation": {
        "cleave": {
            "cdn": ["https://cdn.jsdelivr.net/npm/cleave.js@1.6.0/dist/cleave.min.js"],
            "usage": "Input formatting",
            "when": "Credit cards, phone numbers, dates"
        },
        "choices": {
            "cdn": ["https://cdn.jsdelivr.net/npm/choices.js/public/assets/styles/choices.min.css",
                   "https://cdn.jsdelivr.net/npm/choices.js/public/assets/scripts/choices.min.js"],
            "usage": "Select dropdowns",
            "when": "Enhanced select boxes"
        },
        "flatpickr": {
            "cdn": ["https://cdn.jsdelivr.net/npm/flatpickr/dist/flatpickr.min.css",
                   "https://cdn.jsdelivr.net/npm/flatpickr"],
            "usage": "Date/time picker",
            "when": "Date inputs, scheduling"
        }
    },
    
    "utilities": {
        "axios": {
            "cdn": ["https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"],
            "usage": "HTTP requests",
            "when": "API calls, data fetching"
        },
        "lodash": {
            "cdn": ["https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"],
            "usage": "Utility functions",
            "when": "Data manipulation, helpers"
        },
        "dayjs": {
            "cdn": ["https://cdn.jsdelivr.net/npm/dayjs@1/dayjs.min.js"],
            "usage": "Date manipulation",
            "when": "Date formatting, calculations"
        },
        "luxon": {
            "cdn": ["https://cdn.jsdelivr.net/npm/luxon@3.4.4/build/global/luxon.min.js"],
            "usage": "DateTime library",
            "when": "Complex date operations"
        }
    },
    
    "notifications_modals": {
        "sweetalert2": {
            "cdn": ["https://cdn.jsdelivr.net/npm/sweetalert2@11"],
            "usage": "Beautiful popups/alerts",
            "when": "Confirmations, notifications"
        },
        "toastify": {
            "cdn": ["https://cdn.jsdelivr.net/npm/toastify-js/src/toastify.min.css",
                   "https://cdn.jsdelivr.net/npm/toastify-js"],
            "usage": "Toast notifications",
            "when": "Non-intrusive alerts"
        },
        "tippy": {
            "cdn": ["https://unpkg.com/@popperjs/core@2",
                   "https://unpkg.com/tippy.js@6"],
            "usage": "Tooltips and popovers",
            "when": "Contextual help, hints"
        }
    }
}

# ==============================================================================
# DESIGN KNOWLEDGE BASE
# ==============================================================================

DESIGN_PRINCIPLES = {
    "color_theory": {
        "color_schemes": {
            "complementary": "Colors opposite on color wheel (high contrast)",
            "analogous": "Adjacent colors (harmonious)",
            "triadic": "Three evenly spaced colors (vibrant)",
            "monochromatic": "Variations of single hue (elegant)"
        },
        "best_practices": [
            "60-30-10 rule: 60% dominant, 30% secondary, 10% accent",
            "Use color psychology: Blue=trust, Red=urgency, Green=success",
            "Ensure WCAG AA contrast ratio (4.5:1 for text)",
            "Limit to 3-5 colors in palette",
            "Use HSL for easier color manipulation"
        ],
        "popular_palettes": {
            "tech": ["#2563eb", "#8b5cf6", "#ec4899", "#f59e0b"],
            "corporate": ["#1e40af", "#059669", "#374151", "#f3f4f6"],
            "creative": ["#ec4899", "#8b5cf6", "#06b6d4", "#f59e0b"],
            "minimal": ["#000000", "#ffffff", "#6b7280", "#f3f4f6"],
            "warm": ["#dc2626", "#f59e0b", "#fbbf24", "#fef3c7"],
            "cool": ["#0ea5e9", "#06b6d4", "#8b5cf6", "#e0e7ff"]
        }
    },
    
    "typography": {
        "font_pairings": {
            "classic": "Playfair Display + Source Sans Pro",
            "modern": "Inter + Space Grotesk",
            "elegant": "Cormorant + Lato",
            "tech": "Roboto Mono + Roboto",
            "creative": "Abril Fatface + Poppins"
        },
        "best_practices": [
            "Use 2-3 fonts maximum",
            "Heading: 2.5-4rem on desktop, 1.5-2.5rem mobile",
            "Body text: 16-18px (1rem-1.125rem)",
            "Line height: 1.5-1.8 for body, 1.2-1.4 for headings",
            "Letter spacing: -0.02em for large headings, normal for body",
            "Use font-weight variations instead of multiple fonts"
        ],
        "google_fonts": [
            "Inter", "Roboto", "Poppins", "Montserrat", "Open Sans",
            "Lato", "Playfair Display", "Space Grotesk", "Work Sans",
            "DM Sans", "Plus Jakarta Sans", "Outfit"
        ]
    },
    
    "spacing_layout": {
        "spacing_scale": {
            "xs": "4px",
            "sm": "8px",
            "md": "16px",
            "lg": "24px",
            "xl": "32px",
            "2xl": "48px",
            "3xl": "64px",
            "4xl": "96px"
        },
        "best_practices": [
            "Use 8px grid system for consistency",
            "Section padding: 80-120px vertical on desktop",
            "Container max-width: 1280px for readability",
            "Card padding: 24-40px internal",
            "Button padding: 12-16px vertical, 24-48px horizontal",
            "Whitespace is design - be generous!"
        ],
        "responsive_breakpoints": {
            "mobile": "< 640px",
            "tablet": "640px - 1024px",
            "desktop": "1024px - 1280px",
            "xl": "> 1280px"
        }
    }
}

# ==============================================================================
# COMPONENT DESIGN PATTERNS
# ==============================================================================

COMPONENT_PATTERNS = {
    "buttons": {
        "primary_button": {
            "design": "Bold, high contrast, main call-to-action",
            "css": """
.btn-primary {
    padding: 14px 32px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
}
.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(102, 126, 234, 0.5);
}
.btn-primary:active {
    transform: translateY(0);
}
            """,
            "variations": ["gradient", "solid", "outline", "ghost"]
        },
        "icon_button": {
            "design": "Circular, minimal, for single actions",
            "css": """
.btn-icon {
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    background: rgba(255,255,255,0.1);
    border: none;
    cursor: pointer;
    transition: all 0.3s;
}
.btn-icon:hover {
    background: rgba(255,255,255,0.2);
    transform: scale(1.1);
}
            """
        }
    },
    
    "cards": {
        "elevated_card": {
            "design": "Subtle shadow, hover lift effect",
            "css": """
.card {
    background: white;
    border-radius: 16px;
    padding: 32px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.07), 0 1px 3px rgba(0,0,0,0.06);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 24px rgba(0,0,0,0.12), 0 4px 8px rgba(0,0,0,0.08);
}
            """
        },
        "glass_card": {
            "design": "Glassmorphism effect, modern look",
            "css": """
.glass-card {
    background: rgba(255,255,255,0.1);
    backdrop-filter: blur(10px) saturate(180%);
    border: 1px solid rgba(255,255,255,0.18);
    border-radius: 20px;
    padding: 32px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
}
            """
        }
    },
    
    "navigation": {
        "sticky_nav": {
            "design": "Fixed position, blur background on scroll",
            "css": """
.nav {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 70px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 48px;
    background: rgba(255,255,255,0.8);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid rgba(0,0,0,0.1);
    z-index: 1000;
    transition: all 0.3s;
}
.nav.scrolled {
    height: 60px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
            """
        },
        "sidebar_nav": {
            "design": "Fixed sidebar, smooth slide animations",
            "css": """
.sidebar {
    position: fixed;
    left: 0;
    top: 0;
    width: 260px;
    height: 100vh;
    background: #1a1a1a;
    padding: 24px;
    overflow-y: auto;
    transition: transform 0.3s ease;
}
.sidebar-item {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px 16px;
    border-radius: 8px;
    color: #a0a0a0;
    transition: all 0.2s;
}
.sidebar-item:hover {
    background: rgba(255,255,255,0.05);
    color: white;
}
.sidebar-item.active {
    background: #2563eb;
    color: white;
}
            """
        }
    },
    
    "forms": {
        "modern_input": {
            "design": "Clean, large, clear focus states",
            "css": """
.input {
    width: 100%;
    padding: 14px 16px;
    font-size: 16px;
    border: 2px solid #e5e7eb;
    border-radius: 8px;
    background: white;
    transition: all 0.3s;
}
.input:focus {
    outline: none;
    border-color: #2563eb;
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}
.input::placeholder {
    color: #9ca3af;
}
            """
        },
        "floating_label": {
            "design": "Label animates on focus",
            "html_css": """
<div class="input-group">
    <input type="text" id="email" required>
    <label for="email">Email Address</label>
</div>

<style>
.input-group {
    position: relative;
}
.input-group input {
    width: 100%;
    padding: 16px;
    border: 2px solid #e5e7eb;
    border-radius: 8px;
}
.input-group label {
    position: absolute;
    left: 16px;
    top: 16px;
    color: #9ca3af;
    transition: all 0.3s;
    pointer-events: none;
}
.input-group input:focus + label,
.input-group input:valid + label {
    top: -8px;
    left: 12px;
    font-size: 12px;
    background: white;
    padding: 0 4px;
    color: #2563eb;
}
</style>
            """
        }
    },
    
    "hero_sections": {
        "centered_hero": {
            "design": "Full height, centered content, gradient background",
            "html_structure": """
<section class="hero">
    <div class="hero-content">
        <h1 class="hero-title">Your Amazing Product</h1>
        <p class="hero-subtitle">Build better experiences faster</p>
        <div class="hero-cta">
            <button class="btn-primary">Get Started</button>
            <button class="btn-secondary">Learn More</button>
        </div>
    </div>
</section>
            """,
            "css": """
.hero {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 80px 24px;
    text-align: center;
}
.hero-title {
    font-size: clamp(2.5rem, 6vw, 5rem);
    font-weight: 800;
    color: white;
    margin-bottom: 24px;
    line-height: 1.1;
}
.hero-subtitle {
    font-size: clamp(1.125rem, 2vw, 1.5rem);
    color: rgba(255,255,255,0.9);
    margin-bottom: 40px;
}
            """
        }
    }
}

# ==============================================================================
# ANIMATION PATTERNS
# ==============================================================================

ANIMATION_PATTERNS = {
    "micro_interactions": {
        "button_ripple": {
            "description": "Material Design ripple effect on click",
            "code": """
button.addEventListener('click', function(e) {
    const ripple = document.createElement('span');
    const rect = this.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    
    ripple.style.left = x + 'px';
    ripple.style.top = y + 'px';
    ripple.classList.add('ripple');
    this.appendChild(ripple);
    
    setTimeout(() => ripple.remove(), 600);
});

/* CSS */
.ripple {
    position: absolute;
    border-radius: 50%;
    background: rgba(255,255,255,0.6);
    transform: scale(0);
    animation: ripple-effect 0.6s ease-out;
}
@keyframes ripple-effect {
    to {
        transform: scale(4);
        opacity: 0;
    }
}
            """
        },
        "smooth_scroll": {
            "description": "Smooth scrolling to anchors",
            "code": """
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        target.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    });
});
            """
        }
    },
    
    "entrance_animations": {
        "fade_in_up": {
            "css": """
.fade-in-up {
    opacity: 0;
    transform: translateY(30px);
    animation: fadeInUp 0.8s ease forwards;
}
@keyframes fadeInUp {
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
            """
        },
        "stagger_animation": {
            "description": "Sequential animation for list items",
            "code": """
.stagger-item {
    opacity: 0;
    transform: translateY(20px);
}
.stagger-item:nth-child(1) { animation: fadeInUp 0.6s ease 0.1s forwards; }
.stagger-item:nth-child(2) { animation: fadeInUp 0.6s ease 0.2s forwards; }
.stagger-item:nth-child(3) { animation: fadeInUp 0.6s ease 0.3s forwards; }
            """
        }
    }
}

# ==============================================================================
# BEST PRACTICES BY WEBSITE TYPE
# ==============================================================================

WEBSITE_PATTERNS = {
    "landing_page": {
        "structure": ["Hero", "Features", "Testimonials", "Pricing", "CTA", "Footer"],
        "design_tips": [
            "Clear value proposition in hero (5 seconds rule)",
            "Use social proof (logos, testimonials)",
            "Single, clear call-to-action",
            "Feature benefits, not just features",
            "Mobile-first responsive design"
        ],
        "color_scheme": "Bold primary with white space"
    },
    
    "dashboard": {
        "structure": ["Sidebar Nav", "Top Bar", "Stat Cards", "Charts", "Tables"],
        "design_tips": [
            "Use data visualization libraries (Chart.js, ApexCharts)",
            "Clear hierarchy with card-based layout",
            "Consistent spacing and alignment",
            "Real-time updates with animations",
            "Color-code data (green=good, red=alert)"
        ],
        "color_scheme": "Neutral background with accent highlights"
    },
    
    "ecommerce": {
        "structure": ["Nav", "Hero Banner", "Product Grid", "Filters", "Cart"],
        "design_tips": [
            "Large, high-quality product images",
            "Clear pricing and CTAs",
            "Easy-to-use filters and search",
            "Trust signals (reviews, ratings)",
            "Smooth cart experience"
        ],
        "color_scheme": "Brand colors with clear CTAs"
    },
    
    "portfolio": {
        "structure": ["Hero", "About", "Projects Grid", "Skills", "Contact"],
        "design_tips": [
            "Showcase best work prominently",
            "Use high-quality project images",
            "Clear project descriptions",
            "Easy navigation between projects",
            "Personal branding consistency"
        ],
        "color_scheme": "Sophisticated, brand-aligned"
    },
    
    "blog": {
        "structure": ["Header", "Featured Post", "Post Grid", "Sidebar", "Footer"],
        "design_tips": [
            "Readable typography (18px, 1.6 line-height)",
            "Clear visual hierarchy",
            "Featured images for posts",
            "Easy-to-scan layout",
            "Related posts section"
        ],
        "color_scheme": "Clean, reading-focused"
    }
}
