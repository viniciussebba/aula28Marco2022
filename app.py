from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "<h1>Minha home - app Flask</h1>"

if __name__ == "__main__":
    app.run