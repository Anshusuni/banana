from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    name = data.get("name", "Guest")
    return jsonify({"result": f"Hello {name}, Python program executed!"})
