from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/home")
def home():
    return "its a home page"

@app.route("/register/<username>/<usermailid>/<userpassword>/<phno>")
def register (username,usermailid,userpassword,phno):
    return("username is "+username+" mail id is "+usermailid+" password is "+userpassword+" phone no is "+phno)

@app.route("/signup/<username>/<userpassword>")
def signup(username,userpassword):
    return ("username is "+username+" password is "+userpassword)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
