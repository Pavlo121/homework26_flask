from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():  # put application's code here
    return " Flask in Docker is working!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
