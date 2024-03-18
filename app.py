from enum import Enum

from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import LargeBinary, Column, func

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)


# declaring the database table
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    surname = db.Column(db.String(150), nullable=False)
    id_number = db.Column(db.Integer, unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)

    def __repr__(self):
        return f'<Student {self.name}>'


# Route for the index page
@app.route('/')
def index():
    return render_template('index.html')


# Edit routing
@app.route('/<int:student_id>/edit/', methods=('GET', 'POST'))
def edit(student_id):
    student = Student.query.get_or_404(student_id)

    if request.method == 'POST':
        # Update student information based on form input
        student.name = request.form['name']
        student.surname = request.form['surname']
        student.id_number = request.form['id_number']
        student.email = request.form['email']

        db.session.commit()
        return redirect(url_for('index'))

    return render_template('update.html', student=student)


# Route for seeding information into the database
@app.route('/seed', methods=['POST'])
def seed_data():
    data = request.json
    student = Student()
    db.session.add(student)
    db.session.commit()
    return jsonify({'message': 'Data seeded successfully'})


# Route for retrieving information from the database
@app.route('/profile/<username>', methods=['GET'])
def get_profile(username):
    student = Student.query.filter_by(username=username).first()
    if student:
        return jsonify({
            'fullname': student.fullname,
            'email': student.email,
            'dob': student.dob,
            'gender': student.gender,
            'address': student.address,
            'phone': student.phone
        })
    else:
        return jsonify({'error': 'Student not found'})


if __name__ == '__main__':
    db.create_all()
    app.run()
