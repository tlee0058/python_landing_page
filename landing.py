from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/ninjas")
def ninjas():
    return render_template('ninjas.html')

@app.route("/dojos/new", methods=['POST'])
def dojos():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    
    return redirect ("/")

app.run(debug=True)