from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def addition():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a,b)

    return str(result)

@app.route("/subtract")
def subtract():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a,b)

    return str(result)

@app.route("/multiply")
def multiply():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a,b)

    return str(result)

@app.route("/divide")
def divide():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)

    return str(result)    

# -----------------------------------------------
# Further Study

operations = {
    "add": add,
    "subtract": sub,
    "multiply": mult,
    "divide": div
}

@app.route("/math/<operation>")
def math_operations(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations[operation](a,b)

    return str(result)