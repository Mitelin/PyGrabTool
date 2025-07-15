import pytesseract
import pyscreenshot as ImageGrab
from PIL import Image, ImageEnhance
import tkinter as tk
import pyperclip

# Cesta k Tesseractu – uprav jen pokud máš jinde
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

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
            print("❌ Výběr zrušen klávesou Escape.")
            root.destroy()

    # GUI – výběrové plátno
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

    # Kontrola, jestli se vůbec něco vybralo
    if 'x1' not in coords or 'x2' not in coords:
        print("⚠️ Výběr neproběhl.")
        return

    # Vypočítání oblasti pro snímek
    bbox = (
        min(coords['x1'], coords['x2']),
        min(coords['y1'], coords['y2']),
        max(coords['x1'], coords['x2']),
        max(coords['y1'], coords['y2'])
    )

    # Screenshot dané oblasti
    image = ImageGrab.grab(bbox)

    # 📈 Předzpracování pro lepší čitelnost:
    gray = image.convert('L')  # grayscale
    scaled = gray.resize((gray.width * 2, gray.height * 2), Image.LANCZOS)  # zvětšení
    contrast = ImageEnhance.Contrast(scaled).enhance(1.5)  # zvýšení kontrastu

    # 🧠 OCR rozpoznání textu
    text = pytesseract.image_to_string(contrast, lang='eng')

    # ✂️ Úprava mezer
    cleaned = '\n'.join(' '.join(line.split()) for line in text.splitlines() if line.strip())

    # 📋 Výstup
    if cleaned:
        pyperclip.copy(cleaned)
        print("📋 Text zkopírován do schránky!")
        print("--- Výsledek OCR ---\n" + cleaned)
    else:
        print("⚠️ Žádný text nebyl detekován.")

if __name__ == "__main__":
    capture_area()




