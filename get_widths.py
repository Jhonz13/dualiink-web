from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 400, "height": 800})
    page.goto('http://localhost:8080/')
    page.wait_for_timeout(2000)
    
    # Get all elements and their widths
    elements = page.evaluate("""() => {
        const all = Array.from(document.querySelectorAll('*'));
        return all.map(el => {
            const rect = el.getBoundingClientRect();
            return {
                tag: el.tagName.toLowerCase(),
                id: el.id,
                className: el.className,
                w: rect.width,
                r: rect.right
            };
        }).filter(e => e.r > 400 && e.w > 0).sort((a,b) => b.w - a.w).slice(0, 15);
    }""")
    
    for el in elements:
        print(f"{el['tag']}#{el['id']} .{el['className'][:30]}... Width: {el['w']}, Right: {el['r']}")
    browser.close()
