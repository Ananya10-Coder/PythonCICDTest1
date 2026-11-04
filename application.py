from flask import Flask, jsonify

application = Flask(__name__)

@application.get("/")
def home():
    return jsonify({
        "message": "Hello from AWS CI/CD!",
        "status": "running",
        "version": "1.0"
    })

@application.get("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
   application.run(host="0.0.0.0", port=5000)
