from PIL import Image

try:
    img = Image.open('logo-dualink.png')
    # Resize, maintaining aspect ratio but fitting within 192x192
    img.thumbnail((192, 192), Image.Resampling.LANCZOS)
    
    # Create square background
    bg = Image.new("RGBA", (192, 192), (255, 255, 255, 0))
    # Paste centered
    offset = ((192 - img.width) // 2, (192 - img.height) // 2)
    bg.paste(img, offset)
    
    # Save as favicon.png and favicon.ico
    bg.save('favicon.png')
    bg.save('favicon.ico', format='ICO', sizes=[(32,32), (64,64)])
    print("Favicon created successfully.")
except Exception as e:
    print(f"Error: {e}")
