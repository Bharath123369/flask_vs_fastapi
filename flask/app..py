from flask import Flask, request, jsonify

app = Flask(__name__)
name = None

@app.route('/post', methods=['POST'])
def post_name():
    global name
    name = request.json.get('name')
    return jsonify({"message": f"Saved: {name}"})

@app.route('/get', methods=['GET'])
def get_name():
    return jsonify({"name": name or "No name saved"})

if __name__ == '__main__':
    app.run(debug=True)
