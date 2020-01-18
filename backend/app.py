from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://readAndWrite:uJkfM1V7bi3xT13k@cluster0-ksxj2.gcp.mongodb.net/CharityDB?retryWrites=true&w=majority"
app.config["MONGO_DBNAME"] = 'CharityDB'
mongo = PyMongo(app)

mongo.db.user.insert_one({
    'name' : 'Sam',
    'happiness' : 'nan'
});


@app.route("/")
def home_page():
    return render_template("index.html")