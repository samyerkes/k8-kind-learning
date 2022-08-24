from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def my_secret():
    my_secret_phrase = os.getenv("SECRET_PHRASE")
    return f'<h1>My secret phrase was: "{my_secret_phrase}"</h1>'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(debug=True,host='0.0.0.0',port=port)
