from flask import Flask, render_template
import pyrebase
import time

firebaseConfig = {
    "apiKey": "AIzaSyACjvHy9WX_Cx0NC8B24I1UIiGBC8ifyNA",
    "authDomain": "smart-farm-3ef1a.firebaseapp.com",
    "databaseURL": "https://smart-farm-3ef1a.firebaseio.com",
    "projectId": "smart-farm-3ef1a",
    "storageBucket": "smart-farm-3ef1a.appspot.com",
    "messagingSenderId": "849173162919",
    "appId": "1:849173162919:web:542600f2780ef5ed93e482",
    "measurementId": "G-XQ2P0TX564",
}
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/servo")
def control_servo():
    data = {"servo_status": 1}
    db.child("device").update(data)
    time.sleep(0.5)
    data = {"servo_status": 0}
    db.child("device").update(data)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=5001)
