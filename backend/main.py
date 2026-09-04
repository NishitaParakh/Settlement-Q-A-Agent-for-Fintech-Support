from flask import Flask
from flask_cors import CORS

from routes.investigate import investigate_bp
from routes.search import search_bp


app = Flask(__name__)

CORS(app)

app.register_blueprint(investigate_bp)
app.register_blueprint(search_bp)


@app.route("/")
def home():
    return {
        "message": "Code Blues Settlement Q&A Agent API is running"
    }


@app.route("/health")
def health():
    return {
        "status": "ok",
        "service": "Code Blues Backend"
    }


if __name__ == "__main__":
    app.run(debug=True)