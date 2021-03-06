from flask import Flask
from flask import render_template

from flask_bootstrap import Bootstrap

app = Flask(__name__, static_folder="static")
application = app

Bootstrap(app)

@app.route("/")
def home():
    return render_template("home.html")
  
if __name__ == "__main__":
    app.run(debug=True)
