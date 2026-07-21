from flask import Flask, jsonify

app = Flask(__name__)


def add_numbers(a, b):
    """A simple, testable business-logic function."""
    return a + b


@app.route("/health")
def health():
    """Health-check endpoint used by orchestrators/load balancers."""
    return jsonify(status="healthy"), 200


@app.route("/")
def home():
    return jsonify(message="Welcome to the CI/CD sample app!"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)