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
    "age": 9,
    "level": "Beginner",
    "xp": 45,
    "achievements": [
        "Completed Biology 1 Course",
        "Completed CS 1 Course",
        "Completed Literature 1 Course"
    ]
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
            "email": request.form["em"],
            "password": request.form["pw"],
            "parentName": request.form["parent_name"],
            "childName": request.form["child_name"],
            "age": request.form["child_age"],
            "level": "Beginner",
            "xp": 0,
            "achievements": []
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

@app.route('/default_profile.png')
def default_profile():
    filename = 'default-profile.png'
    return send_file(filename, mimetype='image/png')

@app.route('/trophy.png')
def trophy():
    filename = 'trophy.png'
    return send_file(filename, mimetype='image/png')

@app.route('/help')
def help():
    return render_template("help.html")

@app.route('/courses')
def courses():
    return render_template("courses.html")

@app.route('/cs')
def cs():
    return render_template("cs.html")

@app.route('/csimg.jpg')
def csimg():
    filename = 'csimg.jpg'
    return send_file(filename, mimetype='image/png')

@app.route('/bioimg.jpg')
def bioimg():
    filename = 'bioimg.jpg'
    return send_file(filename, mimetype='image/png')

@app.route('/mimg.jpg')
def mimg():
    filename = 'mimg.jpg'
    return send_file(filename, mimetype='image/png')

@app.route('/litimg.jpg')
def litimg():
    filename = 'litimg.jpg'
    return send_file(filename, mimetype='image/png')


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