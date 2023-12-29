from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/about', methods=['GET'])
def about():
    data = {
        "gender": "Male",
        "github_url": "https://github.com/cdJohnEl",
        "name": "John Chimdike"
    }
    return jsonify(data)

@app.route('/data', methods=['POST'])
def data():
    data = request.get_json()
    return jsonify({'message': 'Data received successfully'})


if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)