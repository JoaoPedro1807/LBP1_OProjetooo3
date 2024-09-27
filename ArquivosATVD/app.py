from flask import Flask, render_template, Blueprint
from controller import blueprint01

app = Flask(__name__)
app.register_blueprint(blueprint01)

@app.route("/", methods=["GET"])
def hello_world():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)