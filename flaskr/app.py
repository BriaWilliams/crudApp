from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key= "secret key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/employees'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

        

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        formData = Data(name, email, phone)
        db.session.add(formData)
        db.session.commit()

        return redirect(url_for('index'))



if __name__  == "__main__":
    app.run(debug=True)