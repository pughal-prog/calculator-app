from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Calculator API Running"

@app.route("/add")
def add():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify({
        "Result": a+b
    })

@app.route("/sub")
def sub():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify({
        "Result": a-b
    })

@app.route("/mul")
def mul():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify({
        "Result": a*b
    })

@app.route("/div")
def div():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify({
        "Result": a/b
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)