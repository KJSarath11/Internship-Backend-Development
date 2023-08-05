from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/home")
def message_section():
    return "its a homepage"

@app.route("/register/<username>/<mailid>/<passwords>/<phnno>")
def register(username,mailid,password,phnno):
    statement1="hi"+username+"your mailid is"+mailid+"your passwords is"+password+"your phn no is"+phnno
    return statement1

@app.route("/signup/<username>/<password>")
def signup(username,password):
    statement2="Hello"+username+"your password is"+password
    return statement2

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)