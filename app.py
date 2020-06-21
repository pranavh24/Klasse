from flask import Flask, render_template, session, request, send_file, Response, redirect, url_for, flash
from flask_session import Session

app = Flask(__name__)

app.secret_key = "hello there"

users = []
admin = {
    "email": "janedoe@gmail.com",
    "password": "hello123",
    "parentName": "Jane Doe",
    "childName": "John Doe",
    "age": 9
}
users.append(admin)


@app.route("/", methods=["POST", "GET"])
@app.route("/home", methods=["POST", "GET"])
def index():
    global users

    if "currentUser" not in session:
        return redirect(url_for('login'))
    
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    global users

    if request.method == "POST":
        # Get login form data

        newUser = {
            "email": request.form["em"],
            "password": request.form["pw"]
        }

        accountMatch = False

        for user in users:
            if newUser.get("email") == user.get("email") and newUser.get("password") == user.get("password"):
                session["currentUser"] = user
                accountMatch = True

        if accountMatch:
            return redirect(url_for('index'))
        else:
            print("Incorrect email or password!")
            return render_template("login.html")
        
    elif "currentUser" in session:
        return redirect(url_for('index'))
    elif request.method == "GET" or "currentUser" not in session:
        return render_template("login.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    global users

    if request.method == "POST":
        # Get register form data
        
        newUser = {
            "name": request.form["nm"],
            "phone_num": request.form["ph"],
            "email": request.form["em"],
            "password": request.form["pw"]
        }

        accountExists = False

        for user in users:
            if newUser.get("email") == user.get("email"):
                accountExists = True
        
        if not accountExists:
            print("Registration successful!")

            users.append(newUser)
            session["currentUser"] = newUser

            return redirect(url_for('index'))
        else:
            print("Account with that email exists!")
            return render_template("register.html")
    
    elif "currentUser" in session:
        return redirect(url_for('index'))
    elif request.method == "GET" or "currentUser" not in session:
        return render_template("register.html")

@app.route("/logout")
def logout():
    session.pop("currentUser", None)
    return redirect(url_for("index"), code=302)

@app.context_processor
def context_processor():
    global users

    isLoggedIn = False
    currentUser = None

    if "currentUser" in session:
        isLoggedIn = True
        currentUser = session["currentUser"]

    return dict(isLoggedIn=isLoggedIn, users=users, currentUser=currentUser)

if __name__ == "__main__":
    app.run(debug=True)