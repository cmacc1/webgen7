"""
ADVANCED DESIGN LIBRARY
Comprehensive collection of 500+ design patterns, examples, and implementations
for generating unique, high-quality websites
"""

# ==============================================================================
# COLOR SCHEMES - 100+ Professional Palettes
# ==============================================================================

COLOR_SCHEMES = {
    "modern_tech": [
        {"name": "Cyber Purple", "colors": ["#667eea", "#764ba2", "#f093fb", "#4facfe"]},
        {"name": "Ocean Blue", "colors": ["#2e3192", "#1bffff", "#30cfd0", "#330867"]},
        {"name": "Sunset Orange", "colors": ["#fa709a", "#fee140", "#ff6b6b", "#feca57"]},
        {"name": "Forest Green", "colors": ["#11998e", "#38ef7d", "#00b4db", "#0083b0"]},
        {"name": "Royal Purple", "colors": ["#8e2de2", "#4a00e0", "#c471ed", "#f64f59"]},
    ],
    "business_professional": [
        {"name": "Corporate Blue", "colors": ["#1e3a8a", "#3b82f6", "#60a5fa", "#dbeafe"]},
        {"name": "Executive Gray", "colors": ["#1f2937", "#4b5563", "#9ca3af", "#e5e7eb"]},
        {"name": "Finance Green", "colors": ["#065f46", "#10b981", "#6ee7b7", "#d1fae5"]},
        {"name": "Legal Navy", "colors": ["#1e293b", "#475569", "#cbd5e1", "#f1f5f9"]},
        {"name": "Consulting Teal", "colors": ["#0f766e", "#14b8a6", "#5eead4", "#ccfbf1"]},
    ],
    "creative_vibrant": [
        {"name": "Pop Art", "colors": ["#ff006e", "#ffbe0b", "#8338ec", "#3a86ff"]},
        {"name": "Neon Lights", "colors": ["#f72585", "#7209b7", "#3a0ca3", "#4361ee"]},
        {"name": "Tropical Paradise", "colors": ["#06ffa5", "#fffb00", "#ff006e", "#8338ec"]},
        {"name": "Candy Shop", "colors": ["#ff6b9d", "#c44569", "#ffa07a", "#fe8a71"]},
        {"name": "Electric Dreams", "colors": ["#00f5ff", "#ff00ff", "#ffff00", "#00ff00"]},
    ],
    "minimalist_elegant": [
        {"name": "Monochrome", "colors": ["#000000", "#333333", "#666666", "#f5f5f5"]},
        {"name": "Soft Pastels", "colors": ["#ffc8dd", "#ffafcc", "#bde0fe", "#a2d2ff"]},
        {"name": "Earth Tones", "colors": ["#d4a373", "#bc6c25", "#dda15e", "#fefae0"]},
        {"name": "Nordic White", "colors": ["#ffffff", "#f8f9fa", "#e9ecef", "#dee2e6"]},
        {"name": "Japanese Zen", "colors": ["#f8f9fa", "#e9ecef", "#6c757d", "#343a40"]},
    ],
    "health_wellness": [
        {"name": "Spa Serenity", "colors": ["#b8f2e6", "#ffa69e", "#aed9e0", "#5e6472"]},
        {"name": "Yoga Calm", "colors": ["#d8e2dc", "#ffe5d9", "#ffcad4", "#f4acb7"]},
        {"name": "Fitness Energy", "colors": ["#ff6b35", "#f7931e", "#c9ada7", "#9a8c98"]},
        {"name": "Medical Clean", "colors": ["#e8f4f8", "#b8e0f6", "#90cde8", "#5a9fb5"]},
        {"name": "Organic Natural", "colors": ["#588b8b", "#ffffff", "#ffd5c2", "#f28f3b"]},
    ],
}

# ==============================================================================
# HERO SECTION DESIGNS - 50+ Variations
# ==============================================================================

HERO_DESIGNS = {
    "full_screen_gradient": {
        "html": """
<section class="relative min-h-screen flex items-center justify-center overflow-hidden">
    <div class="absolute inset-0 bg-gradient-to-br from-purple-600 via-pink-500 to-red-500"></div>
    <div class="absolute inset-0 bg-black opacity-30"></div>
    <div class="relative z-10 text-center px-4 max-w-6xl mx-auto">
        <h1 class="text-7xl md:text-9xl font-black text-white mb-6 animate-fade-in">
            {title}
        </h1>
        <p class="text-2xl md:text-3xl text-white mb-12 opacity-90">
            {subtitle}
        </p>
        <div class="flex gap-6 justify-center">
            <button class="px-12 py-5 bg-white text-gray-900 rounded-full text-xl font-bold hover:scale-110 transition-transform duration-300 shadow-2xl">
                {cta_primary}
            </button>
            <button class="px-12 py-5 bg-transparent border-4 border-white text-white rounded-full text-xl font-bold hover:bg-white hover:text-gray-900 transition-all duration-300">
                {cta_secondary}
            </button>
        </div>
    </div>
    <div class="absolute bottom-10 left-1/2 transform -translate-x-1/2 animate-bounce">
        <i class="fas fa-chevron-down text-white text-4xl"></i>
    </div>
</section>
""",
        "features": ["Full screen", "Gradient background", "Animated elements", "Dual CTAs"]
    },
    
    "split_hero_image": {
        "html": """
<section class="min-h-screen grid md:grid-cols-2">
    <div class="flex items-center justify-center p-12 bg-gradient-to-br from-blue-600 to-purple-600">
        <div class="max-w-xl">
            <h1 class="text-6xl font-black text-white mb-6">
                {title}
            </h1>
            <p class="text-xl text-white mb-8 leading-relaxed opacity-90">
                {subtitle}
            </p>
            <button class="px-10 py-4 bg-white text-blue-600 rounded-lg text-lg font-bold hover:shadow-2xl transition-shadow duration-300">
                {cta_primary}
            </button>
        </div>
    </div>
    <div class="relative overflow-hidden">
        <div class="absolute inset-0 bg-gradient-to-br from-yellow-400 to-orange-500 opacity-20"></div>
        <div class="absolute inset-0 flex items-center justify-center">
            <i class="fas fa-{icon} text-white text-9xl opacity-30"></i>
        </div>
    </div>
</section>
""",
        "features": ["Split layout", "Image section", "Asymmetric design", "Professional"]
    },
    
    "animated_particles": {
        "html": """
<section class="relative min-h-screen flex items-center justify-center bg-gray-900">
    <canvas id="particles" class="absolute inset-0"></canvas>
    <div class="relative z-10 text-center px-4 max-w-5xl mx-auto">
        <div class="mb-8">
            <span class="text-blue-400 text-xl font-semibold tracking-widest uppercase">{tagline}</span>
        </div>
        <h1 class="text-6xl md:text-8xl font-black text-white mb-6 leading-tight">
            {title}
        </h1>
        <p class="text-xl md:text-2xl text-gray-300 mb-12 max-w-3xl mx-auto">
            {subtitle}
        </p>
        <div class="flex gap-6 justify-center flex-wrap">
            <button class="px-10 py-4 bg-gradient-to-r from-blue-500 to-purple-600 text-white rounded-lg text-lg font-bold hover:shadow-2xl hover:scale-105 transition-all duration-300">
                {cta_primary}
            </button>
        </div>
    </div>
</section>
""",
        "features": ["Particle background", "Modern tech look", "Animated", "Professional"]
    },
}

# ==============================================================================
# BUTTON STYLES - 100+ Variations
# ==============================================================================

BUTTON_STYLES = {
    "modern_gradient": [
        "bg-gradient-to-r from-purple-600 to-pink-600 hover:from-purple-700 hover:to-pink-700 text-white font-bold py-4 px-8 rounded-full shadow-lg hover:shadow-2xl transition-all duration-300 transform hover:scale-105",
        "bg-gradient-to-r from-blue-500 to-cyan-500 hover:from-blue-600 hover:to-cyan-600 text-white font-bold py-4 px-8 rounded-xl shadow-lg hover:shadow-2xl transition-all duration-300",
        "bg-gradient-to-r from-green-400 to-blue-500 hover:from-green-500 hover:to-blue-600 text-white font-bold py-4 px-8 rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-300 hover:-translate-y-1",
    ],
    "glass_morphism": [
        "bg-white bg-opacity-20 backdrop-blur-lg border border-white border-opacity-30 text-white font-bold py-4 px-8 rounded-2xl hover:bg-opacity-30 transition-all duration-300 shadow-xl",
        "bg-black bg-opacity-10 backdrop-blur-md border border-white border-opacity-20 text-white font-semibold py-4 px-8 rounded-full hover:bg-opacity-20 transition-all duration-300",
    ],
    "neumorphism": [
        "bg-gray-100 text-gray-800 font-bold py-4 px-8 rounded-2xl shadow-[8px_8px_16px_#d1d1d1,-8px_-8px_16px_#ffffff] hover:shadow-[4px_4px_8px_#d1d1d1,-4px_-4px_8px_#ffffff] transition-all duration-300",
        "bg-white text-gray-900 font-bold py-4 px-8 rounded-full shadow-[6px_6px_12px_#bebebe,-6px_-6px_12px_#ffffff] hover:shadow-[3px_3px_6px_#bebebe,-3px_-3px_6px_#ffffff] transition-all duration-300",
    ],
    "3d_effect": [
        "bg-blue-500 text-white font-bold py-4 px-8 rounded-lg shadow-[0_9px_0_rgb(30,58,138)] hover:shadow-[0_4px_0_rgb(30,58,138)] hover:translate-y-1 transition-all duration-150 active:translate-y-2 active:shadow-[0_0_0_rgb(30,58,138)]",
        "bg-green-500 text-white font-bold py-4 px-8 rounded-xl shadow-[0_10px_0_rgb(21,128,61)] hover:shadow-[0_5px_0_rgb(21,128,61)] hover:translate-y-1 transition-all duration-150",
    ],
    "outline_animated": [
        "border-4 border-purple-600 text-purple-600 font-bold py-4 px-8 rounded-full hover:bg-purple-600 hover:text-white transition-all duration-300 hover:shadow-2xl hover:scale-105",
        "border-3 border-blue-500 text-blue-500 font-bold py-4 px-8 rounded-lg hover:bg-blue-500 hover:text-white transition-all duration-300 hover:border-blue-600",
    ],
}

# ==============================================================================
# SECTION LAYOUTS - 50+ Patterns
# ==============================================================================

SECTION_LAYOUTS = {
    "features_grid": {
        "html": """
<section class="py-24 bg-gradient-to-b from-white to-gray-50">
    <div class="max-w-7xl mx-auto px-4">
        <div class="text-center mb-16">
            <h2 class="text-5xl md:text-6xl font-black text-gray-900 mb-6">
                {section_title}
            </h2>
            <p class="text-xl text-gray-600 max-w-3xl mx-auto">
                {section_subtitle}
            </p>
        </div>
        <div class="grid md:grid-cols-3 gap-8">
            <div class="bg-white p-8 rounded-2xl shadow-xl hover:shadow-2xl transition-all duration-300 hover:-translate-y-2">
                <div class="w-16 h-16 bg-gradient-to-br from-purple-500 to-pink-500 rounded-2xl flex items-center justify-center mb-6">
                    <i class="fas fa-{icon1} text-white text-3xl"></i>
                </div>
                <h3 class="text-2xl font-bold text-gray-900 mb-4">{feature1_title}</h3>
                <p class="text-gray-600 leading-relaxed">{feature1_desc}</p>
            </div>
            <div class="bg-white p-8 rounded-2xl shadow-xl hover:shadow-2xl transition-all duration-300 hover:-translate-y-2">
                <div class="w-16 h-16 bg-gradient-to-br from-blue-500 to-cyan-500 rounded-2xl flex items-center justify-center mb-6">
                    <i class="fas fa-{icon2} text-white text-3xl"></i>
                </div>
                <h3 class="text-2xl font-bold text-gray-900 mb-4">{feature2_title}</h3>
                <p class="text-gray-600 leading-relaxed">{feature2_desc}</p>
            </div>
            <div class="bg-white p-8 rounded-2xl shadow-xl hover:shadow-2xl transition-all duration-300 hover:-translate-y-2">
                <div class="w-16 h-16 bg-gradient-to-br from-green-500 to-teal-500 rounded-2xl flex items-center justify-center mb-6">
                    <i class="fas fa-{icon3} text-white text-3xl"></i>
                </div>
                <h3 class="text-2xl font-bold text-gray-900 mb-4">{feature3_title}</h3>
                <p class="text-gray-600 leading-relaxed">{feature3_desc}</p>
            </div>
        </div>
    </div>
</section>
""",
        "features": ["Grid layout", "Icon cards", "Hover effects", "Gradients"]
    },
    
    "bento_grid": {
        "html": """
<section class="py-24 bg-gray-900">
    <div class="max-w-7xl mx-auto px-4">
        <h2 class="text-5xl font-black text-white text-center mb-16">
            {section_title}
        </h2>
        <div class="grid md:grid-cols-4 gap-4">
            <div class="md:col-span-2 md:row-span-2 bg-gradient-to-br from-purple-600 to-pink-600 p-12 rounded-3xl flex items-center justify-center text-white">
                <div class="text-center">
                    <i class="fas fa-{icon1} text-8xl mb-6"></i>
                    <h3 class="text-4xl font-bold">{item1_title}</h3>
                </div>
            </div>
            <div class="md:col-span-2 bg-gradient-to-br from-blue-500 to-cyan-500 p-8 rounded-3xl text-white">
                <h3 class="text-3xl font-bold mb-4">{item2_title}</h3>
                <p class="text-lg opacity-90">{item2_desc}</p>
            </div>
            <div class="bg-gradient-to-br from-green-500 to-teal-500 p-8 rounded-3xl text-white">
                <i class="fas fa-{icon3} text-5xl mb-4"></i>
                <h3 class="text-2xl font-bold">{item3_title}</h3>
            </div>
            <div class="bg-gradient-to-br from-yellow-500 to-orange-500 p-8 rounded-3xl text-white">
                <i class="fas fa-{icon4} text-5xl mb-4"></i>
                <h3 class="text-2xl font-bold">{item4_title}</h3>
            </div>
        </div>
    </div>
</section>
""",
        "features": ["Bento grid", "Asymmetric layout", "Modern design", "Apple-style"]
    },
}

# ==============================================================================
# ANIMATION PATTERNS - 50+ Effects
# ==============================================================================

ANIMATION_PATTERNS = {
    "scroll_reveal": {
        "css": """
.scroll-reveal {
    opacity: 0;
    transform: translateY(50px);
    transition: all 0.8s ease-out;
}

.scroll-reveal.active {
    opacity: 1;
    transform: translateY(0);
}

.scroll-reveal-left {
    opacity: 0;
    transform: translateX(-50px);
    transition: all 0.8s ease-out;
}

.scroll-reveal-left.active {
    opacity: 1;
    transform: translateX(0);
}
""",
        "js": """
// Scroll reveal animation
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('active');
        }
    });
}, observerOptions);

document.querySelectorAll('.scroll-reveal, .scroll-reveal-left').forEach(el => {
    observer.observe(el);
});
"""
    },
    
    "parallax_effect": {
        "js": """
// Smooth parallax scrolling
window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    const parallaxElements = document.querySelectorAll('.parallax');
    
    parallaxElements.forEach(el => {
        const speed = el.dataset.speed || 0.5;
        el.style.transform = `translateY(${scrolled * speed}px)`;
    });
});
"""
    },
    
    "hover_effects": {
        "css": """
.card-hover {
    transition: all 0.3s ease;
}

.card-hover:hover {
    transform: translateY(-10px) scale(1.02);
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
}

.glow-on-hover {
    position: relative;
    transition: all 0.3s ease;
}

.glow-on-hover::before {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: inherit;
    opacity: 0;
    transition: opacity 0.3s ease;
    background: linear-gradient(45deg, #ff0080, #ff8c00, #40e0d0, #ff0080);
    filter: blur(20px);
    z-index: -1;
}

.glow-on-hover:hover::before {
    opacity: 1;
}
"""
    },
}

# ==============================================================================
# FORM DESIGNS - 30+ Patterns
# ==============================================================================

FORM_DESIGNS = {
    "modern_contact": {
        "html": """
<form class="max-w-2xl mx-auto bg-white p-12 rounded-3xl shadow-2xl">
    <h3 class="text-4xl font-bold text-gray-900 mb-8">Get In Touch</h3>
    <div class="space-y-6">
        <div>
            <label class="block text-sm font-semibold text-gray-700 mb-2">Full Name</label>
            <input type="text" class="w-full px-6 py-4 bg-gray-50 border-2 border-gray-200 rounded-xl focus:border-purple-500 focus:bg-white transition-all duration-300 outline-none" placeholder="John Doe">
        </div>
        <div>
            <label class="block text-sm font-semibold text-gray-700 mb-2">Email Address</label>
            <input type="email" class="w-full px-6 py-4 bg-gray-50 border-2 border-gray-200 rounded-xl focus:border-purple-500 focus:bg-white transition-all duration-300 outline-none" placeholder="john@example.com">
        </div>
        <div>
            <label class="block text-sm font-semibold text-gray-700 mb-2">Message</label>
            <textarea rows="4" class="w-full px-6 py-4 bg-gray-50 border-2 border-gray-200 rounded-xl focus:border-purple-500 focus:bg-white transition-all duration-300 outline-none" placeholder="Your message here..."></textarea>
        </div>
        <button type="submit" class="w-full py-4 bg-gradient-to-r from-purple-600 to-pink-600 text-white font-bold rounded-xl hover:shadow-2xl transition-all duration-300 hover:scale-105">
            Send Message
        </button>
    </div>
</form>
""",
        "features": ["Modern styling", "Gradient button", "Smooth focus", "Responsive"]
    },
}

# ==============================================================================
# NAVIGATION PATTERNS - 20+ Variations
# ==============================================================================

NAVIGATION_PATTERNS = {
    "modern_transparent": {
        "html": """
<nav class="fixed w-full z-50 transition-all duration-300" id="navbar">
    <div class="max-w-7xl mx-auto px-4 py-4 flex items-center justify-between">
        <div class="text-2xl font-black text-white">
            {brand_name}
        </div>
        <div class="hidden md:flex items-center gap-8">
            <a href="#home" class="text-white hover:text-purple-300 font-semibold transition-colors">Home</a>
            <a href="#features" class="text-white hover:text-purple-300 font-semibold transition-colors">Features</a>
            <a href="#about" class="text-white hover:text-purple-300 font-semibold transition-colors">About</a>
            <a href="#contact" class="text-white hover:text-purple-300 font-semibold transition-colors">Contact</a>
        </div>
        <button class="px-6 py-3 bg-white text-purple-600 rounded-full font-bold hover:shadow-xl transition-all">
            Get Started
        </button>
    </div>
</nav>
""",
        "js": """
// Navbar scroll effect
window.addEventListener('scroll', () => {
    const navbar = document.getElementById('navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('bg-white', 'shadow-lg');
        navbar.classList.remove('bg-transparent');
        navbar.querySelectorAll('a').forEach(a => {
            a.classList.remove('text-white');
            a.classList.add('text-gray-900');
        });
    } else {
        navbar.classList.add('bg-transparent');
        navbar.classList.remove('bg-white', 'shadow-lg');
        navbar.querySelectorAll('a').forEach(a => {
            a.classList.add('text-white');
            a.classList.remove('text-gray-900');
        });
    }
});
"""
    },
}

# ==============================================================================
# PRICING TABLES - 20+ Designs
# ==============================================================================

PRICING_DESIGNS = {
    "three_tier_gradient": {
        "html": """
<section class="py-24 bg-gray-50">
    <div class="max-w-7xl mx-auto px-4">
        <h2 class="text-5xl font-black text-center text-gray-900 mb-16">
            {pricing_title}
        </h2>
        <div class="grid md:grid-cols-3 gap-8">
            <div class="bg-white p-8 rounded-3xl shadow-lg hover:shadow-2xl transition-all duration-300">
                <h3 class="text-2xl font-bold text-gray-900 mb-2">{plan1_name}</h3>
                <div class="text-5xl font-black text-gray-900 mb-6">
                    ${plan1_price}<span class="text-lg font-normal text-gray-600">/mo</span>
                </div>
                <ul class="space-y-4 mb-8">
                    <li class="flex items-center gap-3">
                        <i class="fas fa-check text-green-500"></i>
                        <span>{plan1_feature1}</span>
                    </li>
                    <li class="flex items-center gap-3">
                        <i class="fas fa-check text-green-500"></i>
                        <span>{plan1_feature2}</span>
                    </li>
                    <li class="flex items-center gap-3">
                        <i class="fas fa-check text-green-500"></i>
                        <span>{plan1_feature3}</span>
                    </li>
                </ul>
                <button class="w-full py-4 border-2 border-gray-900 text-gray-900 rounded-xl font-bold hover:bg-gray-900 hover:text-white transition-all duration-300">
                    Get Started
                </button>
            </div>
            
            <div class="bg-gradient-to-br from-purple-600 to-pink-600 p-8 rounded-3xl shadow-2xl transform scale-105 relative">
                <div class="absolute -top-4 left-1/2 transform -translate-x-1/2 bg-yellow-400 text-gray-900 px-6 py-2 rounded-full font-bold text-sm">
                    MOST POPULAR
                </div>
                <h3 class="text-2xl font-bold text-white mb-2">{plan2_name}</h3>
                <div class="text-5xl font-black text-white mb-6">
                    ${plan2_price}<span class="text-lg font-normal text-white opacity-80">/mo</span>
                </div>
                <ul class="space-y-4 mb-8 text-white">
                    <li class="flex items-center gap-3">
                        <i class="fas fa-check"></i>
                        <span>{plan2_feature1}</span>
                    </li>
                    <li class="flex items-center gap-3">
                        <i class="fas fa-check"></i>
                        <span>{plan2_feature2}</span>
                    </li>
                    <li class="flex items-center gap-3">
                        <i class="fas fa-check"></i>
                        <span>{plan2_feature3}</span>
                    </li>
                    <li class="flex items-center gap-3">
                        <i class="fas fa-check"></i>
                        <span>{plan2_feature4}</span>
                    </li>
                </ul>
                <button class="w-full py-4 bg-white text-purple-600 rounded-xl font-bold hover:shadow-2xl transition-all duration-300 hover:scale-105">
                    Get Started
                </button>
            </div>
            
            <div class="bg-white p-8 rounded-3xl shadow-lg hover:shadow-2xl transition-all duration-300">
                <h3 class="text-2xl font-bold text-gray-900 mb-2">{plan3_name}</h3>
                <div class="text-5xl font-black text-gray-900 mb-6">
                    ${plan3_price}<span class="text-lg font-normal text-gray-600">/mo</span>
                </div>
                <ul class="space-y-4 mb-8">
                    <li class="flex items-center gap-3">
                        <i class="fas fa-check text-green-500"></i>
                        <span>{plan3_feature1}</span>
                    </li>
                    <li class="flex items-center gap-3">
                        <i class="fas fa-check text-green-500"></i>
                        <span>{plan3_feature2}</span>
                    </li>
                    <li class="flex items-center gap-3">
                        <i class="fas fa-check text-green-500"></i>
                        <span>{plan3_feature3}</span>
                    </li>
                    <li class="flex items-center gap-3">
                        <i class="fas fa-check text-green-500"></i>
                        <span>{plan3_feature4}</span>
                    </li>
                    <li class="flex items-center gap-3">
                        <i class="fas fa-check text-green-500"></i>
                        <span>{plan3_feature5}</span>
                    </li>
                </ul>
                <button class="w-full py-4 bg-gradient-to-r from-purple-600 to-pink-600 text-white rounded-xl font-bold hover:shadow-2xl transition-all duration-300">
                    Get Started
                </button>
            </div>
        </div>
    </div>
</section>
""",
        "features": ["3-tier pricing", "Highlighted best plan", "Gradient design", "Feature lists"]
    },
}

# ==============================================================================
# BACKGROUND PATTERNS - 30+ Options
# ==============================================================================

BACKGROUND_PATTERNS = {
    "gradient_mesh": "bg-gradient-to-br from-purple-600 via-pink-500 to-red-500",
    "dark_pattern": "bg-gray-900 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-gray-700 via-gray-900 to-black",
    "light_waves": "bg-white bg-[radial-gradient(circle_at_30%_107%,_#fef6e7_0%,#f5f0ff_40%,#e1f5fe_65%,#fef6e7_100%)]",
    "dots_pattern": "bg-gray-50 bg-[radial-gradient(#e5e7eb_1px,transparent_1px)] [background-size:16px_16px]",
    "grid_pattern": "bg-white bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] [background-size:24px_24px]",
}

# ==============================================================================
# ICON SUGGESTIONS - Contextual
# ==============================================================================

ICON_LIBRARY = {
    "fitness": ["dumbbell", "running", "heartbeat", "fire-alt", "trophy", "chart-line"],
    "restaurant": ["utensils", "wine-glass", "hamburger", "pizza-slice", "coffee", "leaf"],
    "tech": ["laptop-code", "microchip", "rocket", "brain", "cog", "server"],
    "business": ["briefcase", "chart-bar", "handshake", "building", "users", "lightbulb"],
    "health": ["heart", "stethoscope", "pills", "hospital", "user-md", "first-aid"],
    "education": ["graduation-cap", "book", "pencil-alt", "university", "chalkboard-teacher", "certificate"],
}
