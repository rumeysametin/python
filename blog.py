from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "Home Page"
@app.route("/about")
def about():
    return "About Me"
if __name__ == "__main__":
    app.run(debug=True)