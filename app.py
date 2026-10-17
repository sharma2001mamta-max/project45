import os
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-this-secret-key-before-deploying")
SITE_PASSWORD = os.environ.get("SITE_PASSWORD", "Sonu@1610")

def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if not session.get("birthday_unlocked"):
            return redirect(url_for("login"))
        return view(*args, **kwargs)
    return wrapped_view

@app.route("/", methods=["GET", "POST"])
def login():
    if session.get("birthday_unlocked"):
        return redirect(url_for("birthday"))
    error = None
    if request.method == "POST":
        entered = request.form.get("password", "")
        if entered and entered == SITE_PASSWORD:
            session["birthday_unlocked"] = True
            return redirect(url_for("birthday"))
        error = "That isn't the secret password. Try again, birthday star ✦"
    return render_template("login.html", error=error)

@app.route("/birthday")
@login_required
def birthday():
    # Put your photos in static/images/ and list them below.
    # Supported examples: jpg, jpeg, png, webp.
    gallery_images = [
       
    {"file": "Sonu01.jpeg", "caption": "Your beautiful smile Jo DARU Dekh ke Ayyi"},
    {"file": "Sonu02.jpeg", "caption": "Bekar Pic Jo apko Bhot Achi Lagti Hai "},
    {"file": "Sonu03.jpeg", "caption": "My favourite person & My Favourite Photo "},
    {"file": "Sonu04.jpeg", "caption": "A little moment of magic"},
    {"file": "Sonu05.jpeg", "caption": "Halki Halki Pyaar ki Nisanni"},
    {"file": "Sonu06.jpeg", "caption": "Pyaari Smile & Pyaare Aap"},
    {"file": "Sonu07.jpeg", "caption": "One for the memories"},
    {"file": "Sonu08.jpeg", "caption": "That special look Masoon Shakal"},
    {"file": "Sonu16.jpeg", "caption": "A moment frozen in time"},
    {"file": "Sonu10.jpeg", "caption": "Special Moment or Bhot Proud Moment bhi "},
    {"file": "Sonu11.jpeg", "caption": "Clicked By ME"},
    {"file": "Sonu12.jpeg", "caption": "The main character of Your Life"},
    {"file": "Sonu13.jpeg", "caption": "Apka Bestie"},
    {"file": "Sonu14.jpeg", "caption": "Forever worth celebrating"},
    {"file": "Sonu15.jpeg", "caption": "Written in the stars"},
    {"file": "Sonu09.jpeg", "caption": "Happiest birthday, Jaaaan "},

    ]
    return render_template("birthday.html", gallery_images=gallery_images)

@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.errorhandler(404)
def not_found(_error):
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
