import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "feature_request.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

class Feature(db.Model):
    title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "<Title: {}>".format(self.title)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        feature_title = Feature(title=request.form.get("title"))
        db.session.add(feature_title)
        db.session.commit()
    features = Feature.query.all()
    return render_template("home.html", features=features)

@app.route("/update", methods=["POST"])
def update():
    newtitle = request.form.get("newtitle")
    oldtitle = request.form.get("oldtitle")
    feature = Feature.query.filter_by(title=oldtitle).first()
    feature.title = newtitle
    db.session.commit()
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    title = request.form.get("title")
    feature = Feature.query.filter_by(title=title).first()
    db.session.delete(feature)
    db.session.commit()
    return redirect("/")
  
if __name__ == "__main__":
    app.run(debug=True)
