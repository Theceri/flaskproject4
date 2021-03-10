from flask import Flask, render_template, request, redirect, url_for
# import psycopg2
# from flask import Flask
from configs.base_config import Development, Staging, Production
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Development)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/sqlalchemy'
db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()
    # db.drop_all()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80), unique=False, nullable=False)
    lname = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

@app.route('/', methods = ['GET', 'POST'])
def hello():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']

        print(fname, lname, email)

        a = User(fname = fname, lname = lname, email = email)
        db.session.add(a)
        db.session.commit()
        print("Record successfully added")
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug = True)