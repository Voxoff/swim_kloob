from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route("/")
def hello():
  images = os.listdir('static/images')
  images = ['images/' + file for file in images]
  return render_template("home.html", images = images)

@app.route("/join")
def join():
  return "To become a fellow Swim Kloob member, you must be given permission by the President. Failing that, the interim leader. Failing that, the substitute interim leader."

@app.route("/upload")
def upload():
  return "Please upload your photos here:"


if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)

