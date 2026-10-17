# Sonu Dhanda — Advanced Midnight Birthday Website

Features:
- Server-checked password gate
- Midnight blue, silver stars, floating hearts, moonlight design
- Birthday hero section and letter
- Responsive photo gallery with click-to-open lightbox, next/previous buttons and keyboard navigation
- “Little things” cards and birthday wish interaction
- Optional local music picker (the selected audio stays in the visitor's browser; it is not uploaded)
- Render Blueprint configuration

## Add 15–20 photos

1. Copy the photos into `static/images/`.
2. Rename them in order, for example `sonu01.jpg`, `sonu02.jpg`, ... `sonu20.jpg`. JPG, PNG, and WebP are supported.
3. In `app.py`, find `gallery_images` in the `birthday()` route and replace the sample comment with entries like:

```python
gallery_images = [
    {"file": "sonu01.jpg", "caption": "That unforgettable smile"},
    {"file": "sonu02.jpg", "caption": "A little moment to remember"},
    {"file": "sonu03.jpg", "caption": "Looking like a star"},
]
```

Add one dictionary per photo. Use the exact filename and captions you like. Captions appear under the photos and in the photo lightbox.

## Change the birthday message

Edit `templates/birthday.html`. Search for `Dear Sonu,` and replace the sample paragraphs with your personal letter. You can also edit the “Things that make you you” cards in that file.

## Local run

```bash
pip install -r requirements.txt
```

Windows PowerShell:
```powershell
$env:SITE_PASSWORD="blueheart"
$env:SECRET_KEY="replace-with-a-long-random-secret"
python app.py
```

Then open http://127.0.0.1:5000

## Deploy on Render

If you already have a Render service, you can update the same GitHub repository with these advanced files; Render should redeploy automatically. If you want to keep the previous website unchanged, create a separate GitHub repository and a new Render service.

- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app`
- Environment variables: set `SITE_PASSWORD` to your chosen password and `SECRET_KEY` to a private random value. Render's Blueprint can generate the secret key.
- Keep `app.py`, `requirements.txt`, and `render.yaml` at repository root.

## Important

- Never put a real password or secret key in public source code. The environment variable overrides the fallback value in `app.py`.
- A shared password is a simple gate, not a full account system.
- Only use photos you have permission to share.
