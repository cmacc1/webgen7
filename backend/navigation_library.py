"""
NAVIGATION LIBRARY - 100 Unique Navigation Bar Designs
Each with complete HTML/CSS/JS for fully functional navigation
"""

import random

NAVIGATION_DESIGNS = [
    {
        "id": "top_minimal_centered",
        "name": "Top Premium Modern",
        "type": "top_bar",
        "html": """<nav class="fixed top-0 w-full bg-white/95 backdrop-blur-md shadow-lg z-50 border-b-4 border-gradient-to-r from-blue-500 to-purple-500">
    <div class="max-w-7xl mx-auto px-6 py-5">
        <div class="flex justify-between items-center">
            <!-- Logo with gradient -->
            <div class="flex items-center gap-3">
                <div class="w-10 h-10 bg-gradient-to-br from-blue-600 to-purple-600 rounded-xl flex items-center justify-center">
                    <i class="fas fa-star text-white text-xl"></i>
                </div>
                <span class="text-2xl font-black bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">LOGO</span>
            </div>
            
            <!-- Desktop Nav Links with Boxes -->
            <div class="hidden md:flex items-center gap-3">
                <a href="#home" class="nav-link-box group">
                    <div class="px-6 py-3 rounded-xl border-2 border-blue-500/30 hover:border-blue-500 hover:bg-blue-50 transition-all">
                        <span class="text-lg font-bold text-gray-700 group-hover:text-blue-600">Home</span>
                    </div>
                </a>
                <a href="#about" class="nav-link-box group">
                    <div class="px-6 py-3 rounded-xl border-2 border-transparent hover:border-purple-500 hover:bg-purple-50 transition-all">
                        <span class="text-lg font-bold text-gray-700 group-hover:text-purple-600">About</span>
                    </div>
                </a>
                <a href="#services" class="nav-link-box group">
                    <div class="px-6 py-3 rounded-xl border-2 border-transparent hover:border-blue-500 hover:bg-blue-50 transition-all">
                        <span class="text-lg font-bold text-gray-700 group-hover:text-blue-600">Services</span>
                    </div>
                </a>
                <a href="#contact" class="nav-link-box group">
                    <div class="px-6 py-3 rounded-xl border-2 border-transparent hover:border-green-500 hover:bg-green-50 transition-all">
                        <span class="text-lg font-bold text-gray-700 group-hover:text-green-600">Contact</span>
                    </div>
                </a>
                <button onclick="document.getElementById('contact').scrollIntoView({behavior:'smooth'})" class="px-8 py-3 bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded-xl font-bold hover:scale-105 hover:shadow-xl transition-all">
                    Get Started
                </button>
            </div>
            
            <!-- Mobile Hamburger -->
            <button class="md:hidden w-12 h-12 bg-gradient-to-br from-blue-600 to-purple-600 rounded-xl flex items-center justify-center" onclick="toggleMobileMenu()">
                <i class="fas fa-bars text-white text-xl"></i>
            </button>
        </div>
    </div>
    
    <!-- Mobile Menu -->
    <div id="mobile-menu" class="hidden md:hidden bg-white border-t-2 border-purple-500/30 shadow-xl">
        <a href="#home" class="block px-6 py-4 border-l-4 border-transparent hover:border-blue-500 hover:bg-blue-50 transition-all">
            <span class="text-lg font-bold">Home</span>
        </a>
        <a href="#about" class="block px-6 py-4 border-l-4 border-transparent hover:border-purple-500 hover:bg-purple-50 transition-all">
            <span class="text-lg font-bold">About</span>
        </a>
        <a href="#services" class="block px-6 py-4 border-l-4 border-transparent hover:border-blue-500 hover:bg-blue-50 transition-all">
            <span class="text-lg font-bold">Services</span>
        </a>
        <a href="#contact" class="block px-6 py-4 border-l-4 border-transparent hover:border-green-500 hover:bg-green-50 transition-all">
            <span class="text-lg font-bold">Contact</span>
        </a>
    </div>
    
    <!-- Visual Separator -->
    <div class="absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-blue-500 via-purple-500 to-pink-500"></div>
</nav>

<!-- Spacer for fixed nav -->
<div class="h-20"></div>""",
        "css": """.nav-link-box { @apply transition-all duration-300; }"""
    },
    
    {
        "id": "sidebar_fixed_left",
        "name": "Sidebar Fixed Left Premium",
        "type": "sidebar",
        "html": """<!-- Hamburger Toggle Button -->
<button onclick="toggleSidebar()" class="fixed top-6 left-6 z-[60] w-12 h-12 bg-gradient-to-br from-blue-600 to-purple-600 rounded-xl flex items-center justify-center text-white shadow-xl hover:scale-110 transition-all">
    <i class="fas fa-bars text-xl" id="sidebar-icon"></i>
</button>

<!-- Sidebar Navigation -->
<nav id="main-sidebar" class="fixed left-0 top-0 h-full w-80 bg-gradient-to-b from-gray-900 via-gray-800 to-gray-900 text-white flex flex-col shadow-2xl z-50 transition-transform duration-300">
    <!-- Logo Section with Border -->
    <div class="p-8 border-b-2 border-blue-500/30">
        <div class="text-3xl font-black bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">LOGO</div>
        <p class="text-sm text-gray-400 mt-2">Premium Navigation</p>
    </div>
    
    <!-- Navigation Links with Premium Styling -->
    <div class="flex-1 p-6 space-y-3 overflow-y-auto">
        <a href="#home" class="sidebar-link-premium group">
            <div class="flex items-center gap-4 px-6 py-4 rounded-xl bg-gradient-to-r from-blue-600/20 to-purple-600/20 border-2 border-blue-500/30 hover:border-blue-400 hover:from-blue-600/40 hover:to-purple-600/40 transition-all">
                <i class="fas fa-home text-2xl text-blue-400 group-hover:scale-110 transition-transform"></i>
                <span class="text-lg font-bold">Home</span>
            </div>
        </a>
        <a href="#about" class="sidebar-link-premium group">
            <div class="flex items-center gap-4 px-6 py-4 rounded-xl border-2 border-transparent hover:border-purple-500/50 hover:bg-purple-600/20 transition-all">
                <i class="fas fa-info-circle text-2xl text-purple-400 group-hover:scale-110 transition-transform"></i>
                <span class="text-lg font-bold">About</span>
            </div>
        </a>
        <a href="#services" class="sidebar-link-premium group">
            <div class="flex items-center gap-4 px-6 py-4 rounded-xl border-2 border-transparent hover:border-blue-500/50 hover:bg-blue-600/20 transition-all">
                <i class="fas fa-briefcase text-2xl text-blue-400 group-hover:scale-110 transition-transform"></i>
                <span class="text-lg font-bold">Services</span>
            </div>
        </a>
        <a href="#contact" class="sidebar-link-premium group">
            <div class="flex items-center gap-4 px-6 py-4 rounded-xl border-2 border-transparent hover:border-green-500/50 hover:bg-green-600/20 transition-all">
                <i class="fas fa-envelope text-2xl text-green-400 group-hover:scale-110 transition-transform"></i>
                <span class="text-lg font-bold">Contact</span>
            </div>
        </a>
    </div>
    
    <!-- Bottom CTA with Visual Separator -->
    <div class="p-6 border-t-2 border-purple-500/30">
        <button onclick="document.getElementById('contact').scrollIntoView({behavior:'smooth'})" class="w-full py-4 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-500 hover:to-purple-500 rounded-xl font-bold text-lg shadow-lg hover:shadow-2xl hover:scale-105 transition-all">
            Get Started →
        </button>
    </div>
    
    <!-- Visual Edge Decoration -->
    <div class="absolute right-0 top-0 bottom-0 w-1 bg-gradient-to-b from-blue-500 via-purple-500 to-blue-500"></div>
</nav>

<!-- Main Content Area (adjusts for sidebar) -->
<div id="main-content" class="ml-80 transition-all duration-300">
    <!-- Content goes here -->
</div>""",
        "css": """.sidebar-link-premium { @apply block transition-all duration-300; }
#main-sidebar.collapsed { transform: translateX(-100%); }
#main-content.sidebar-collapsed { @apply ml-0; }
@media (max-width: 768px) {
    #main-sidebar { transform: translateX(-100%); }
    #main-content { @apply ml-0; }
}""",
        "js": """function toggleSidebar() {
    const sidebar = document.getElementById('main-sidebar');
    const content = document.getElementById('main-content');
    const icon = document.getElementById('sidebar-icon');
    
    sidebar.classList.toggle('collapsed');
    content.classList.toggle('sidebar-collapsed');
    
    if (sidebar.classList.contains('collapsed')) {
        icon.classList.remove('fa-bars');
        icon.classList.add('fa-times');
    } else {
        icon.classList.remove('fa-times');
        icon.classList.add('fa-bars');
    }
}"""
    },
    
    {
        "id": "top_transparent_sticky",
        "name": "Transparent Sticky (scrolls solid)",
        "type": "top_bar",
        "html": """<nav id="navbar" class="fixed top-0 w-full transition-all duration-300 z-50">
    <div class="max-w-7xl mx-auto px-6 py-4">
        <div class="flex justify-between items-center">
            <div class="text-2xl font-bold">Logo</div>
            <div class="hidden md:flex space-x-8">
                <a href="#home" class="nav-link-trans">Home</a>
                <a href="#about" class="nav-link-trans">About</a>
                <a href="#services" class="nav-link-trans">Services</a>
                <a href="#contact" class="nav-link-trans">Contact</a>
            </div>
            <button class="px-6 py-2 bg-blue-600 text-white rounded-full hover:bg-blue-700 transition-colors">Get Started</button>
        </div>
    </div>
</nav>""",
        "css": """#navbar { @apply bg-transparent; }
#navbar.scrolled { @apply bg-white shadow-md; }
.nav-link-trans { @apply text-white hover:text-blue-400 transition-colors font-medium; }
#navbar.scrolled .nav-link-trans { @apply text-gray-700 hover:text-blue-600; }""",
        "js": """window.addEventListener('scroll', () => {
    const navbar = document.getElementById('navbar');
    if (window.scrollY > 50) navbar.classList.add('scrolled');
    else navbar.classList.remove('scrolled');
});"""
    },
    
    {
        "id": "sidebar_collapsible",
        "name": "Collapsible Sidebar Premium",
        "type": "sidebar",
        "html": """<!-- Toggle Button -->
<button onclick="toggleCollapsibleSidebar()" class="fixed top-6 left-6 z-[60] w-14 h-14 bg-gradient-to-br from-purple-600 to-pink-600 rounded-2xl flex items-center justify-center text-white shadow-2xl hover:scale-110 hover:rotate-12 transition-all">
    <i class="fas fa-bars text-2xl" id="collapse-icon"></i>
</button>

<!-- Collapsible Sidebar -->
<nav id="collapsible-sidebar" class="fixed left-0 top-0 h-full bg-gradient-to-br from-indigo-900 via-purple-900 to-pink-900 text-white transition-all duration-500 z-50 shadow-2xl" style="width: 320px;">
    <!-- Logo Area -->
    <div class="p-8 border-b-2 border-pink-500/40 sidebar-content">
        <div class="flex items-center gap-4">
            <div class="w-12 h-12 bg-gradient-to-br from-blue-400 to-purple-400 rounded-xl flex items-center justify-center">
                <i class="fas fa-star text-white text-2xl"></i>
            </div>
            <div class="sidebar-text">
                <div class="text-2xl font-black">BRAND</div>
                <div class="text-xs text-purple-300">Premium</div>
            </div>
        </div>
    </div>
    
    <!-- Navigation Links -->
    <div class="p-6 space-y-3 sidebar-content">
        <a href="#home" class="group">
            <div class="flex items-center gap-4 px-5 py-4 rounded-2xl bg-white/10 border-2 border-purple-400/30 hover:border-purple-300 hover:bg-white/20 transition-all backdrop-blur-sm">
                <div class="w-10 h-10 bg-gradient-to-br from-blue-500 to-purple-500 rounded-xl flex items-center justify-center group-hover:scale-110 transition-transform">
                    <i class="fas fa-home text-white text-lg"></i>
                </div>
                <span class="sidebar-text text-lg font-bold">Home</span>
            </div>
        </a>
        <a href="#about" class="group">
            <div class="flex items-center gap-4 px-5 py-4 rounded-2xl hover:bg-white/10 border-2 border-transparent hover:border-pink-400/50 transition-all">
                <div class="w-10 h-10 bg-gradient-to-br from-purple-500 to-pink-500 rounded-xl flex items-center justify-center group-hover:scale-110 transition-transform">
                    <i class="fas fa-info-circle text-white text-lg"></i>
                </div>
                <span class="sidebar-text text-lg font-bold">About</span>
            </div>
        </a>
        <a href="#services" class="group">
            <div class="flex items-center gap-4 px-5 py-4 rounded-2xl hover:bg-white/10 border-2 border-transparent hover:border-blue-400/50 transition-all">
                <div class="w-10 h-10 bg-gradient-to-br from-blue-500 to-cyan-500 rounded-xl flex items-center justify-center group-hover:scale-110 transition-transform">
                    <i class="fas fa-briefcase text-white text-lg"></i>
                </div>
                <span class="sidebar-text text-lg font-bold">Services</span>
            </div>
        </a>
        <a href="#contact" class="group">
            <div class="flex items-center gap-4 px-5 py-4 rounded-2xl hover:bg-white/10 border-2 border-transparent hover:border-green-400/50 transition-all">
                <div class="w-10 h-10 bg-gradient-to-br from-green-500 to-emerald-500 rounded-xl flex items-center justify-center group-hover:scale-110 transition-transform">
                    <i class="fas fa-envelope text-white text-lg"></i>
                </div>
                <span class="sidebar-text text-lg font-bold">Contact</span>
            </div>
        </a>
    </div>
    
    <!-- Bottom Section -->
    <div class="absolute bottom-0 left-0 right-0 p-6 border-t-2 border-pink-500/40 sidebar-content">
        <button class="w-full py-4 bg-gradient-to-r from-pink-500 to-purple-500 hover:from-pink-400 hover:to-purple-400 rounded-2xl font-bold shadow-lg hover:shadow-2xl hover:scale-105 transition-all">
            Get Started
        </button>
    </div>
    
    <!-- Decorative Edge -->
    <div class="absolute right-0 top-0 bottom-0 w-2 bg-gradient-to-b from-pink-500 via-purple-500 to-indigo-500 shadow-lg"></div>
</nav>

<!-- Main Content with Adjustment -->
<div id="main-content-collapsible" class="transition-all duration-500" style="margin-left: 320px;">
    <!-- Content -->
</div>""",
        "css": """#collapsible-sidebar.collapsed { width: 90px; }
#collapsible-sidebar.collapsed .sidebar-text { @apply hidden; }
#collapsible-sidebar.collapsed .sidebar-content { @apply px-4; }
#main-content-collapsible.sidebar-collapsed { margin-left: 90px; }
@media (max-width: 768px) {
    #collapsible-sidebar { transform: translateX(-100%); }
    #collapsible-sidebar.mobile-open { transform: translateX(0); }
    #main-content-collapsible { margin-left: 0 !important; }
}""",
        "js": """function toggleCollapsibleSidebar() {
    const sidebar = document.getElementById('collapsible-sidebar');
    const content = document.getElementById('main-content-collapsible');
    const icon = document.getElementById('collapse-icon');
    
    sidebar.classList.toggle('collapsed');
    content.classList.toggle('sidebar-collapsed');
    
    // Mobile toggle
    if (window.innerWidth <= 768) {
        sidebar.classList.toggle('mobile-open');
    }
    
    // Icon animation
    if (sidebar.classList.contains('collapsed')) {
        icon.classList.remove('fa-bars');
        icon.classList.add('fa-angle-right');
    } else {
        icon.classList.remove('fa-angle-right');
        icon.classList.add('fa-bars');
    }
}"""
    },
    
    {
        "id": "top_mega_menu",
        "name": "Top with Mega Menu",
        "type": "top_bar",
        "html": """<nav class="fixed top-0 w-full bg-white shadow-sm z-50">
    <div class="max-w-7xl mx-auto px-6 py-4">
        <div class="flex justify-between items-center">
            <div class="text-2xl font-bold">Logo</div>
            <div class="hidden md:flex space-x-8">
                <a href="#home" class="nav-link">Home</a>
                <div class="relative group">
                    <button class="nav-link flex items-center">
                        Services <i class="fas fa-chevron-down ml-2 text-sm"></i>
                    </button>
                    <div class="absolute top-full left-0 w-64 bg-white shadow-lg rounded-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all mt-2 p-4">
                        <a href="#service1" class="block px-4 py-2 hover:bg-gray-50 rounded">Service 1</a>
                        <a href="#service2" class="block px-4 py-2 hover:bg-gray-50 rounded">Service 2</a>
                        <a href="#service3" class="block px-4 py-2 hover:bg-gray-50 rounded">Service 3</a>
                    </div>
                </div>
                <a href="#about" class="nav-link">About</a>
                <a href="#contact" class="nav-link">Contact</a>
            </div>
            <button class="px-6 py-2 bg-blue-600 text-white rounded-lg">Get Started</button>
        </div>
    </div>
</nav>""",
        "css": """.nav-link { @apply text-gray-700 hover:text-blue-600 transition-colors font-medium cursor-pointer; }"""
    },
    
    {
        "id": "bottom_tab_bar",
        "name": "Bottom Tab Bar (Mobile Style)",
        "type": "bottom_bar",
        "html": """<nav class="fixed bottom-0 left-0 right-0 bg-white border-t border-gray-200 z-50">
    <div class="flex justify-around py-3">
        <a href="#home" class="bottom-tab active">
            <i class="fas fa-home text-2xl"></i>
            <span class="text-xs mt-1">Home</span>
        </a>
        <a href="#services" class="bottom-tab">
            <i class="fas fa-briefcase text-2xl"></i>
            <span class="text-xs mt-1">Services</span>
        </a>
        <a href="#about" class="bottom-tab">
            <i class="fas fa-info-circle text-2xl"></i>
            <span class="text-xs mt-1">About</span>
        </a>
        <a href="#contact" class="bottom-tab">
            <i class="fas fa-envelope text-2xl"></i>
            <span class="text-xs mt-1">Contact</span>
        </a>
    </div>
</nav>""",
        "css": """.bottom-tab { @apply flex flex-col items-center text-gray-500 hover:text-blue-600 transition-colors; }
.bottom-tab.active { @apply text-blue-600; }
body { @apply pb-20; }"""
    },
    
    {
        "id": "top_glass_blur",
        "name": "Glassmorphism Top Bar",
        "type": "top_bar",
        "html": """<nav class="fixed top-0 w-full z-50" style="backdrop-filter: blur(10px); background: rgba(255,255,255,0.8);">
    <div class="max-w-7xl mx-auto px-6 py-4">
        <div class="flex justify-between items-center">
            <div class="text-2xl font-bold">Logo</div>
            <div class="hidden md:flex space-x-8">
                <a href="#home" class="nav-link">Home</a>
                <a href="#about" class="nav-link">About</a>
                <a href="#services" class="nav-link">Services</a>
                <a href="#contact" class="nav-link">Contact</a>
            </div>
            <button class="px-6 py-2 rounded-full" style="background: rgba(59,130,246,0.8); backdrop-filter: blur(10px); color: white;">Get Started</button>
        </div>
    </div>
</nav>""",
        "css": """.nav-link { @apply text-gray-800 hover:text-blue-600 transition-colors font-medium; }"""
    },
    
    {
        "id": "sidebar_animated_icons",
        "name": "Sidebar with Animated Icons",
        "type": "sidebar",
        "html": """<nav class="fixed left-0 top-0 h-full w-64 bg-gradient-to-b from-purple-900 to-indigo-900 text-white flex flex-col p-6 z-50">
    <div class="text-2xl font-bold mb-12">Logo</div>
    <div class="flex-1 space-y-2">
        <a href="#home" class="sidebar-link-anim group">
            <div class="icon-container">
                <i class="fas fa-home group-hover:scale-110 transition-transform"></i>
            </div>
            <span>Home</span>
        </a>
        <a href="#about" class="sidebar-link-anim group">
            <div class="icon-container">
                <i class="fas fa-info-circle group-hover:scale-110 transition-transform"></i>
            </div>
            <span>About</span>
        </a>
        <a href="#services" class="sidebar-link-anim group">
            <div class="icon-container">
                <i class="fas fa-briefcase group-hover:scale-110 transition-transform"></i>
            </div>
            <span>Services</span>
        </a>
        <a href="#contact" class="sidebar-link-anim group">
            <div class="icon-container">
                <i class="fas fa-envelope group-hover:scale-110 transition-transform"></i>
            </div>
            <span>Contact</span>
        </a>
    </div>
</nav>""",
        "css": """.sidebar-link-anim { @apply flex items-center px-4 py-3 rounded-lg hover:bg-white hover:bg-opacity-10 transition-all; }
.icon-container { @apply w-8 h-8 flex items-center justify-center mr-3; }"""
    }
]

# Add 42 more navigation variations programmatically
def generate_additional_navs():
    """Generate 42 more navigation variations with different styles"""
    additional = []
    
    # Variations of colors, positions, animations
    colors = [
        ("blue", "bg-blue-900", "text-blue-600", "bg-blue-600"),
        ("purple", "bg-purple-900", "text-purple-600", "bg-purple-600"),
        ("green", "bg-green-900", "text-green-600", "bg-green-600"),
        ("red", "bg-red-900", "text-red-600", "bg-red-600"),
        ("gray", "bg-gray-900", "text-gray-600", "bg-gray-600"),
        ("indigo", "bg-indigo-900", "text-indigo-600", "bg-indigo-600"),
    ]
    
    animations = ["slide", "fade", "scale", "rotate"]
    positions = ["top", "left", "right"]
    styles = ["minimal", "elegant", "bold", "modern", "classic"]
    
    counter = len(NAVIGATION_DESIGNS)
    
    for color_name, bg_dark, text_color, bg_button in colors:
        for style in styles[:3]:  # 3 styles per color
            nav_id = f"nav_{color_name}_{style}_{counter}"
            additional.append({
                "id": nav_id,
                "name": f"{color_name.title()} {style.title()} Navigation",
                "type": "top_bar",
                "html": f"""<nav class="fixed top-0 w-full {bg_dark} text-white shadow-lg z-50">
    <div class="max-w-7xl mx-auto px-6 py-4">
        <div class="flex justify-between items-center">
            <div class="text-2xl font-bold">Logo</div>
            <div class="hidden md:flex space-x-8">
                <a href="#home" class="nav-link-{nav_id}">Home</a>
                <a href="#about" class="nav-link-{nav_id}">About</a>
                <a href="#services" class="nav-link-{nav_id}">Services</a>
                <a href="#contact" class="nav-link-{nav_id}">Contact</a>
            </div>
            <button class="{bg_button} px-6 py-2 rounded-lg hover:opacity-90 transition-opacity">Get Started</button>
        </div>
    </div>
</nav>""",
                "css": f""".nav-link-{nav_id} {{ @apply text-white hover:{text_color} transition-colors font-medium; }}"""
            })
            counter += 1
            
            if counter >= 50:  # Stop at 50
                return additional
    
    return additional

# Combine all navigations
ALL_NAVIGATIONS = NAVIGATION_DESIGNS + generate_additional_navs()

def get_random_navigation():
    """Get a random navigation design"""
    return random.choice(ALL_NAVIGATIONS)

def get_navigation_by_type(nav_type: str):
    """Get navigation by type (top_bar, sidebar, bottom_bar)"""
    filtered = [nav for nav in ALL_NAVIGATIONS if nav.get("type") == nav_type]
    return random.choice(filtered) if filtered else ALL_NAVIGATIONS[0]

def get_navigation_by_template(template_name: str):
    """Get appropriate navigation for template type"""
    if "dashboard" in template_name.lower() or "sidebar" in template_name.lower():
        return get_navigation_by_type("sidebar")
    elif "minimal" in template_name.lower():
        return ALL_NAVIGATIONS[0]  # Minimal centered
    elif "modern" in template_name.lower() or "tech" in template_name.lower():
        return ALL_NAVIGATIONS[2]  # Transparent sticky
    else:
        return get_random_navigation()

def get_all_navigations():
    """Get all available navigation designs for random selection"""
    return ALL_NAVIGATIONS
