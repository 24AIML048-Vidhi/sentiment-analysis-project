from flask import Flask, render_template, request
from model import train_model

app = Flask(__name__)

# train model once when app starts
model, cv = train_model()


@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        text = request.form["text"]

        text = cv.transform([text])

        result = model.predict(text)[0]

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)