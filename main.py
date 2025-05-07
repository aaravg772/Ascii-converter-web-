import pyfiglet
from colorama import Fore
from python.slowprint import *
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

all_fonts = pyfiglet.FigletFont.getFonts()

@app.route("/", methods = ["GET"])
def home():
    return render_template("index.html", list = all_fonts, len = len(all_fonts), text = "")

@app.route("/?font=&text=", methods = ["GET", "POST"])
def idk():
    font = request.args.get("font")
    text = request.args.get("text")
    font2 = pyfiglet.Figlet(font=font)
    result = font2.renderText(text=text)

    return render_template("index2.html", list = all_fonts, len = len(all_fonts), text = result)


if __name__ == '__main__':
    app.run(debug = True)