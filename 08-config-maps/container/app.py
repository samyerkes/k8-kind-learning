from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    greeting = os.getenv("GREETING")
    name = os.getenv("NAME")

    return f'<h1>{greeting} {name}</h1><p>(Set by a ConfigMap)</p>'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(debug=True,host='0.0.0.0',port=port)
