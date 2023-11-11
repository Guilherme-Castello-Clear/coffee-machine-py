from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=datetime.datetime.now().year)

@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    response = requests.get(gender_url).json()
    gender = response["gender"]

    age_url = f"https://api.agify.io?name={name}"
    response_age = requests.get(age_url).json()
    age = response_age["age"]

    return render_template("guess.html", gender=gender, name=name, age=age)

@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/82975389c85afb34e389"
    response = requests.get(blog_url)
    all_posts = response.json()

    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
