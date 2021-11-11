from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    article = dict()
    article["title"] = "Test"
    article["body"] = "Test 123"
    article["author"] = "Joseph Addison"
    number = 10
    return render_template("index.html", n1 = number, article = article)
if __name__ == "__main__":
    app.run(debug=True)