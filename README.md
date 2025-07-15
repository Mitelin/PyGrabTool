# PyGrabTool

PyGrabTool je lehký nástroj pro okamžité OCR snímání textu z obrazovky (např. chybové hlášky, výpisy, logy) přímo do schránky.

Pomocí jednoduchého výběru myší přes GUI získáš přesný text z obrazovky, který je okamžitě připraven ke vložení – například do chatu s ChatGPT nebo pro Google hledání chyb.

## Funkce

- Výběr libovolné oblasti obrazovky myší
- Automatický screenshot a OCR pomocí Tesseract
- Úprava obrázku (grayscale, zvětšení, zvýšení kontrastu) pro lepší čitelnost
- Výsledek se ihned zkopíruje do schránky
- Minimální závislosti – extrémně rychlý nástroj

## Použití

1. Spusť skript `main.py`
2. Myší označ oblast s textem (například chybovou hlášku)
3. Text se přečte a vloží do schránky
4. Vlož ho pomocí `Ctrl + V` kamkoli potřebuješ

## Instalace

Instaluj potřebné knihovny pomocí:

```
pip install -r requirements.txt
```

Nebo ručně:

```
pip install pytesseract pillow pyscreenshot pyperclip
```

## Tesseract OCR

Tento nástroj vyžaduje mít nainstalovaný Tesseract OCR engine:

- Stažení: https://github.com/tesseract-ocr/tesseract/wiki
- Doporučená cesta pro Windows:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

## Proč to vzniklo

Nástroj vznikl pro rychlé kopírování textů z GUI oken (hlavně error hlášek), které lze snadno:
- vložit do ChatGPT
- použít při debugování
- nebo vyhledat na webu

## Možný další vývoj

- Export do `.exe`
- Globální klávesová zkratka
- Překlad OCR výstupu
- Ukládání OCR historie

## Licence

MIT License – můžeš tento nástroj volně používat, upravovat i sdílet.
