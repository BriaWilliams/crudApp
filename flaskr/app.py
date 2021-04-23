from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key= "secret key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:opensesame@localhost/employees'
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
    employeeData = Data.query.all()

    return render_template("index.html", employees = employeeData)

@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        formData = Data(name, email, phone)
        db.session.add(formData)
        db.session.commit()

        flash("Employee Added Successfully")

        return redirect(url_for('index')) #redirects back to index page

@app.route('/update', methods = ['GET', 'POST'])
def update():

    if request.method == 'POST':
        employeeData = Data.query.get(request.form.get('id'))

        employeeData.name = request.form['name']
        employeeData.email = request.form['email']
        employeeData.phone = request.form['phone']

        db.session.commit()
        flash("Employee Information Updated Successfully")

        return redirect(url_for('index'))

@app.route('/delete/<id>/', methods =['GET', 'POST'])
def delete(id):
    employeeData = Data.query.get(id)
    db.session.delete(employeeData)
    db.session.commit()
    flash("Employee Deleted Successfully")

    return redirect(url_for('index'))

