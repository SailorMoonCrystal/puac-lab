from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def aboutme():
    return render_template("aboutme.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

if __name__ == "__main__":
    app.run(debug=True)