from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, Department, Employee, Project, EmployeeProject

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:yaokouassi@localhost/employees'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

def get_directory():
    all_emps = Employee.query.all()

    for emp in all_emps:
        if emp.dept is not None:
            print(emp.name, emp.dept.dept_name, emp.dept.phone)
        else:
            print(emp.name)


def get_directory_join():
    directory = db.session.query(
        Employee.name, Department.dept_name, Department.phone).join(Department).all()

    for name, dept, phone in directory:
        print(name, dept, phone)


def get_directory_join_class():
    directory = db.session.query(Employee, Department).join(Department).all()

    for emp, dept in directory:
        print(emp.name, dept.dept_name, dept.phone)


def get_directory_all_join():
    directory = db.session.query(
        Employee.name, Department.dept_name, Department.phone).outerjoin(Department).all()

    for name, dept, phone in directory:
        print(name, dept, phone)



@app.route('/phones')
def list_phones():
    """Renders directory of employees and phone numbers  (from dept)"""
    emps = Employee.query.all()
    return render_template('phones.html', emps=emps)
