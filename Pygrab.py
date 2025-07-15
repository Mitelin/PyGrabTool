import pytesseract
import pyscreenshot as imagegrab
from PIL import Image, ImageEnhance
import tkinter as tk
import pyperclip
import configparser

config = configparser.ConfigParser()
config.read('config.cfg')

tesseract_path = config.get('tesseract', 'path')
pytesseract.pytesseract.tesseract_cmd = tesseract_path

def capture_area():
    coords = {}

    def on_mouse_down(event):
        coords['x1'], coords['y1'] = event.x, event.y
        canvas.coords(rect, event.x, event.y, event.x, event.y)

    def on_mouse_drag(event):
        canvas.coords(rect, coords['x1'], coords['y1'], event.x, event.y)

    def on_mouse_up(event):
        coords['x2'], coords['y2'] = event.x, event.y
        root.destroy()

    def on_key(event):
        if event.keysym == 'Escape':
            print("Selection stopped by Escape.")
            root.destroy()

    # GUI
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.attributes('-alpha', 0.3)
    root.config(bg='black', cursor="crosshair")

    canvas = tk.Canvas(root, bg='black')
    canvas.pack(fill=tk.BOTH, expand=True)

    rect = canvas.create_rectangle(0, 0, 0, 0, outline='red', width=2)

    canvas.bind("<ButtonPress-1>", on_mouse_down)
    canvas.bind("<B1-Motion>", on_mouse_drag)
    canvas.bind("<ButtonRelease-1>", on_mouse_up)
    root.bind("<Key>", on_key)
    root.mainloop()

    # Check if something was selected
    if 'x1' not in coords or 'x2' not in coords:
        print("No selection.")
        return

    # Calculate area for screenshot
    bbox = (
        min(coords['x1'], coords['x2']),
        min(coords['y1'], coords['y2']),
        max(coords['x1'], coords['x2']),
        max(coords['y1'], coords['y2'])
    )

    # Screenshot selected area
    image = imagegrab.grab(bbox)

    # Screenshot conversion for better readability:
    gray = image.convert('L')  # grayscale
    scaled = gray.resize((gray.width * 2, gray.height * 2), Image.LANCZOS)  # Resize
    contrast = ImageEnhance.Contrast(scaled).enhance(1.5)  # Contrast

    # OCR Text detection
    text = pytesseract.image_to_string(contrast, lang='eng')

    # Fix the spaces
    cleaned = '\n'.join(' '.join(line.split()) for line in text.splitlines() if line.strip())

    # Output
    if cleaned:
        pyperclip.copy(cleaned)
        print("Text copied to clipboard.!")
        print("--- Output OCR ---\n" + cleaned)
    else:
        print("No text found.")

if __name__ == "__main__":
    capture_area()




