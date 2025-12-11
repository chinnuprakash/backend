from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "CI-CD Deployment is working!"}

@app.route("/status")
def status():
    return jsonify({"status": "running", "version": "1.0.1"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
