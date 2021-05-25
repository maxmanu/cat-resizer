from flask import Flask
from flask.globals import request
from PIL import Image
from io import BytesIO
from flask.helpers import send_file

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/greeting/<nombre>")
def greeting(nombre):
    return f"hello {nombre}"


@app.route("/sorteo/<nombre>/<number>")
def sorteo(nombre, number):
    return f"<b>{nombre} : </b>{number}"


@app.route("/search")
def search():
    query = request.args.get("q")
    return f"search: {query}"


@app.route("/cat.jpg")
def cat():
    width = request.args.get("width")
    height = request.args.get("height")
    size = (int(width), int(height))
    img = Image.open("cat.jpg")
    img.thumbnail(size)
    img_io = BytesIO()
    img.save(img_io, "JPEG")
    img_io.seek(0)
    return send_file(img_io, mimetype="image/jpeg")
