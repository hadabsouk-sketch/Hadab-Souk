# Hadab Souk — Python (Flask) Version

Premium Arabic-style electronics marketplace. English + Arabic (RTL), cart, checkout, categories, product pages.

## VS Code mein chalane ka tareeqa (Step by step)

### 1. Python install karein
- https://www.python.org/downloads/ se Python 3.10+ install karein
- Install karte waqt **"Add Python to PATH"** ka checkbox zaroor on karein

### 2. Project open karein
- VS Code kholein → `File` → `Open Folder` → `python-version` folder select karein

### 3. Terminal kholein
- VS Code mein `Ctrl + ` ` (backtick) dabaayein ya `Terminal` → `New Terminal`

### 4. Virtual environment banayein (recommended)
```bash
python -m venv venv
```
Activate karein:
- **Windows**: `venv\Scripts\activate`
- **Mac/Linux**: `source venv/bin/activate`

### 5. Flask install karein
```bash
pip install -r requirements.txt
```

### 6. App chalayein
```bash
python app.py
```

### 7. Browser kholein
👉 http://localhost:5000

Bas! Website chalegi.

## File structure
```
python-version/
├── app.py              # Main Flask app (routes + logic)
├── catalog.py          # Products + categories data
├── translations.py     # English + Arabic text
├── requirements.txt    # Python packages
├── templates/          # HTML pages (Jinja2)
│   ├── base.html
│   ├── index.html
│   ├── shop.html
│   ├── product.html
│   ├── category.html
│   ├── cart.html
│   ├── checkout.html
│   ├── about.html
│   └── contact.html
└── static/
    └── css/style.css   # Styling
```

## Language toggle
Top header mein **EN / ع** button se language switch hoga. Arabic mein layout automatically RTL ho jaayega.

## Cart
LocalStorage nahi, Flask session use hoti hai — server-side persistent.

## Coupon
Checkout pe `HADAB10` lagayein → 10% off.
