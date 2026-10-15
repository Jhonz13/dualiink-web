import re

with open('proyectos.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Tailwind Configs
# We use regex to add backgroundImage after the colors object in both tailwind.config blocks.
content = re.sub(
    r'(colors: \{[\s\S]*?brand: \{[\s\S]*?\},?\s*\}(,?))',
    r'\1\n          backgroundImage: {\n            "brand-gradient": "linear-gradient(135deg, #115e59 0%, #84cc16 100%)",\n          },',
    content
)

# 2. Card styles
content = content.replace('hover:border-emerald-500/30', 'hover:border-brand-blue/30')
content = content.replace('rgba(16,185,129,0.1)', 'rgba(132,204,22,0.1)')

# 3. Navbar Logo & Links
content = content.replace(
    '<span class="text-emerald-500">Dua</span><span class="text-white">Link</span>',
    '<span class="text-emerald-500">Dua</span><span class="text-brand-blue">Link</span>'
)
content = content.replace('hover:text-emerald-400', 'hover:text-brand-blue')

# 4. Navbar Contacto
content = content.replace(
    'bg-emerald-600 text-white px-4 py-1.5 rounded-full font-bold hover:bg-emerald-500',
    'bg-violet-600 text-white px-4 py-1.5 rounded-full font-bold hover:bg-violet-500'
)

# 5. Hero
content = content.replace(
    'Nuestros <span class="text-emerald-500">Proyectos</span>',
    'Nuestros <span class="text-brand-blue">Proyectos</span>'
)

# 6. Global Utility replaces
content = content.replace('text-emerald-400', 'text-brand-blue')
content = content.replace('bg-emerald-500', 'bg-brand-blue')
content = content.replace('hover:text-emerald-300', 'hover:text-[#65a30d]')

# 7. Final CTA
content = content.replace(
    'bg-emerald-600 text-white px-10 py-5 rounded-full font-black text-xl hover:scale-105',
    'bg-brand-gradient text-white px-10 py-5 rounded-full font-black text-xl hover:scale-105'
)

with open('proyectos.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Colors updated successfully.")
