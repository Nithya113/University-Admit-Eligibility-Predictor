from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "ABC@123"

@app.route("/registration")
def index():
  return render_template("registration.html")
  
@app.route("/login")
def login():
  return render_template("login.html")
