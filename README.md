# Taj Minar Constructions — Flask App

## Project Structure

```
flask_project/
│
├── app.py                     # Flask routes & app entry point
├── requirements.txt
│
├── templates/
│   ├── base.html              # Base layout (head, navbar, footer)
│   ├── partials/
│   │   ├── navbar.html        # Navbar + mobile menu
│   │   └── footer.html        # Footer
│   └── pages/
│       ├── index.html         # Home page
│       ├── about.html         # About page
│       ├── services.html      # Services page
│       ├── projects.html      # Projects page
│       ├── gallery.html       # Gallery page
│       └── contact.html       # Contact page
│
└── static/
    ├── css/
    │   ├── style.css
    │   └── style2.css
    ├── js/
    │   └── script.js
    └── images/
        └── ...                # All project images

```

## Setup & Run

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the app
python app.py
```

Then open http://127.0.0.1:5000 in your browser.

## Routes

| URL         | Page      |
|-------------|-----------|
| `/`         | Home      |
| `/about`    | About     |
| `/services` | Services  |
| `/projects` | Projects  |
| `/gallery`  | Gallery   |
| `/contact`  | Contact   |
