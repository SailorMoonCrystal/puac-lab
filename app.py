from flask import Flask, render_template, url_for, request, flash, redirect
from forms import ContactForm, GuestBookForm
from datetime import datetime
from azure.AzureDB import AzureDB


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


@app.route("/guestbook", methods=["GET", "POST"])
def guestbook():
    form = GuestBookForm()
    date = datetime.now()
    str_date = date.strftime("%d/%m/%Y %H:%M")
    with AzureDB() as a:
        data = a.azureGetData()
        if request.method == "POST":
            name = request.form["name"]
            message = request.form["message"]
            if request.form["id"]:
                a.azureUpdateData(request.form["id"], name, message)
            else:
                a.azureAddData(name, message, date.strftime("%Y-%m-%dT%H:%M:%S"))
            return redirect(url_for("guestbook"))
    return render_template("guestbook.html", form=form, date=str_date, data=data)


@app.route("/guestbook/<int:id>/delete", methods=["GET", "POST"])
def delete(id):
    with AzureDB() as a:
        if request.method == "POST":
            a.azureDeleteData(id)
            return redirect(url_for("guestbook"))
    return redirect(url_for("guestbook"))


@app.route("/guestbook/<int:id>/edit", methods=["GET", "POST"])
def edit(id):
    form = GuestBookForm()
    date = datetime.now()
    str_date = date.strftime("%d/%m/%Y %H:%M")
    with AzureDB() as a:
        data = a.azureGetData()
        pre_data_raw = [row for row in data if row["id"] == id]
        pre_data = {
            "id": pre_data_raw[0][0],
            "name": pre_data_raw[0][1],
            "message": pre_data_raw[0][2],
            "date": pre_data_raw[0][3],
        }
        form.message.data = pre_data["message"]
    return render_template(
        "guestbook.html", form=form, date=str_date, data=data, pre_data=pre_data
    )


if __name__ == "__main__":
    app.run(debug=True)
