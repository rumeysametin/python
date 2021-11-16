from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

class RegisterForm(Form):
    name = StringField("name", validators=[validators.Length(min= 4, max=25)])
    username = StringField("username", validators=[validators.Length(min= 5, max=35)])
    email = StringField("email", validators=[validators.Length(min=10, max=30)])
    password = PasswordField("password", validators=[
        validators.DataRequired(message="please set password"),
        validators.EqualTo(fieldname= "confirm", message= "your password doesn't match")
    ])
    confirm = PasswordField("verify password")

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "blog"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/article/<string:id>")
def detail(id):
    return "Article id:" + id

@app.route("/register")
def register():
    form = RegisterForm(request.form)
    if request.method == "POST":
         return redirect(url_for("index"))
    else:
        return render_template("register.html", form = form)
if __name__ == "__main__":
    app.run(debug=True)