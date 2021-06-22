from flask import Flask, render_template, url_for, request, flash, redirect
from forms import ContactForm

app = Flask(__name__)
app.secret_key = "secretKey"


@app.route("/")
def index():
    return render_template("carousel.html")


@app.route("/about")
def aboutme():
    return render_template("aboutme.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        flash("The message was sent! We will contact you by email you provided.")
        return redirect(url_for("contact"))
    return render_template("contact.html", form=form)


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


if __name__ == "__main__":
    app.run(debug=True)
