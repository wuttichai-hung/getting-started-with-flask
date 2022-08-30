from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api', methods=["POST", "GET"])
def api():
    if request.method == "POST":
        return jsonify(msg="Post Method Ok", value="30")
    else:
        return jsonify(msg="Get Methood Ok", value="30")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
