# Shorty: URL Shortener

A URL shortener built with Django. Paste a long link, get a short code, and every visit to the short link redirects and is counted.

## Features

- Generates a unique random short code (lowercase letters and digits) for each link
- Tells you when a link was already shortened instead of creating a duplicate
- Redirects `/<code>/` to the original URL
- Counts clicks per link in a separate `analytcs` app
- Each link has an `active` flag, and only active links are used
- `refreshcode` management command to regenerate short codes in bulk

## Pages

| Path | What it does |
| --- | --- |
| `/index/` | Form to shorten a link |
| `/<code>/` | Redirect to the original URL and count the click |
| `/view-2/<code>/` | Same redirect, written as a class-based view |
| `/admin/` | Manage links and click counts |

## Built with

- Python 3, Django
- SQLite

## Run it locally

```bash
git clone https://github.com/hamzakhalem/django_shorty_link.git
cd django_shorty_link
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install django
export DJANGO_SECRET_KEY="any-long-random-string"   # PowerShell: $env:DJANGO_SECRET_KEY="..."
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/index/ to shorten your first link.

Regenerate the short codes of the first 10 links:

```bash
python manage.py refreshcode 10
```

## Project structure

```
shorty/      Project settings and root URLs
myshorter/   Short links: model, form, code generator, views, templates, refreshcode command
analytcs/    Click events counted per short link
```
