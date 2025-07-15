# PyGrabTool

PyGrabTool je lehký nástroj pro okamžité OCR snímání textu z obrazovky (např. chybové hlášky, výpisy, logy) přímo do schránky.

Pomocí jednoduchého výběru myší přes GUI získáš přesný text z obrazovky, který je okamžitě připraven ke vložení – například do chatu s ChatGPT nebo pro Google hledání chyb.

---

## Funkce

- Výběr libovolné oblasti obrazovky myší
- Automatický screenshot a OCR pomocí Tesseract
- Úprava obrázku (grayscale, zvětšení, zvýšení kontrastu) pro lepší čitelnost
- Výsledek se ihned zkopíruje do schránky
- Minimální závislosti – extrémně rychlý nástroj

---

## Použití

1. Spusť skript `Pygrab.py`
2. Myší označ oblast s textem (například chybovou hlášku)
3. Text se přečte a vloží do schránky
4. Vlož ho pomocí `Ctrl + V` kamkoli potřebuješ

---

## Instalace

Instaluj potřebné knihovny pomocí:

```
pip install -r requirements.txt
```

Nebo ručně:

```
pip install pytesseract pillow pyscreenshot pyperclip
```

---

## Tesseract OCR

Tento nástroj vyžaduje mít nainstalovaný Tesseract OCR engine:

- Stažení: https://github.com/tesseract-ocr/tesseract/wiki

---

## Nastavení Tesseractu

V kořenové složce projektu se nachází soubor `config.cfg`, kde je nastavena cesta k programu Tesseract OCR.

Pokud máte Tesseract nainstalovaný v jiné složce, upravte hodnotu v tomto souboru:

```ini
[tesseract]
path = C:\Program Files\Tesseract-OCR\tesseract.exe
```

---

## Proč to vzniklo

Nástroj vznikl pro rychlé kopírování textů z GUI oken (hlavně error hlášek), které lze snadno:
- vložit do ChatGPT
- použít při debugování
- nebo vyhledat na webu

---

## Možný další vývoj

- Export do `.exe`
- Globální klávesová zkratka
- Překlad OCR výstupu
- Ukládání OCR historie

---

## Licence

MIT License – můžeš tento nástroj volně používat, upravovat i sdílet.

---

# English

**PyGrabTool** is a lightweight tool for instant OCR capture of screen text (errors, logs, debug output) directly into the clipboard.

Use simple mouse selection to grab any visible text and get it ready for pasting – for ChatGPT, Google search, debugging and more.

---

## Features

- Select any screen region with your mouse
- Automatic screenshot and OCR via Tesseract
- Image preprocessing (grayscale, zoom, contrast boost) for better accuracy
- Clipboard-ready output in milliseconds
- Minimal dependencies – lightning-fast

---

## Usage

1. Run `Pygrab.py`
2. Select the text region with your mouse
3. The tool runs OCR and puts the result into clipboard
4. Paste anywhere using `Ctrl + V`

---

## Installation

Install dependencies:

```
pip install -r requirements.txt
```

Or manually:

```
pip install pytesseract pillow pyscreenshot pyperclip
```

---

## Tesseract Setup

You must have [Tesseract OCR](https://github.com/tesseract-ocr/tesseract/wiki) installed.

In the root of the project there is a config file `config.cfg` with the Tesseract executable path. Change it if needed:

```ini
[tesseract]
path = C:\Program Files\Tesseract-OCR\tesseract.exe
```

---

## Motivation

Tool was built to speed up copying error messages and logs from GUI windows, ready for:
- ChatGPT
- debugging
- web search

---

## Future ideas

- `.exe` build
- Global hotkey
- Integrated translation
- Save OCR history

---

## License

MIT License – free to use, modify and share.

