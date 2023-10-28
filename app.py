from flask import Flask, request
from operations import *

app = Flask(__name__)


@app.route("/add")
def adding():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)
    return str(result)


@app.route("/sub")
def subtract():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)
    return str(result)


@app.route("/mult")
def multiply():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)
    return str(result)


@app.route("/div")
def divide():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    if b == 0:
        return "Division by zero is not allowed"
    result = div(a, b)
    return str(result)
