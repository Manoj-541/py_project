from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
from models import db, User
from ml import predict_disease, get_all_symptoms

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

# -----------------------------
# Home
# -----------------------------
@app.route("/")
def home():
    return render_template("login.html")


# -----------------------------
# Register
# -----------------------------
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])

        if User.query.filter_by(username=username).first():
            return "User already exists"

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("register.html")


# -----------------------------
# Login
# -----------------------------
@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        session["user_id"] = user.id
        return redirect(url_for("dashboard"))

    return "Invalid Credentials"


# -----------------------------
# Dashboard (Dynamic Symptoms)
# -----------------------------
@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("home"))

    symptoms = get_all_symptoms()
    return render_template("dashboard.html", symptoms=symptoms)


# -----------------------------
# Predict
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():

    if "user_id" not in session:
        return redirect(url_for("home"))

    selected_symptoms = request.form.getlist("symptoms")

    if not selected_symptoms:
        return "Please select at least one symptom"

    disease = predict_disease(selected_symptoms)

    return render_template("result.html", disease=disease)


# -----------------------------
# Logout
# -----------------------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
