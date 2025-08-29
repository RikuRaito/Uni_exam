from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])

@app.route('/api/health', methods=["GET"])
def health_check():
    return jsonify({
        "status": "OK",
        "message": "Everything is OK"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)