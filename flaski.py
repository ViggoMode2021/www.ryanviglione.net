from flask import Flask, render_template, request
import smtplib
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///friends.db'

def create_app():
    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app

#Initialize the db
db = SQLAlchemy(app)

#Create db model
class Friends(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    data_created = db.Column(db.DateTime, default = datetime.utcnow)
#Create a function to return string
    def __repr__(self):
        return '<Name %r>' % self.id
subscribers = []

@app.route('/')
def index():
    title = 'Ryan Vig blog'
    return render_template('index.html', title=title)

@app.route('/about')
def about():
    title = 'Sobre Ryan Viglione'
    names = ['Vida', 'Trabajo', 'Pasatiempos', 'Enlaces']
    return render_template("about.html", names = names, title= title)

@app.route('/subscribe')
def subscribe():
    title_two = 'Puedes subscribirte ahora.'
    return render_template('subscribe.html', title=title_two)

@app.route('/form', methods = ["POST"])
def form():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    '''
    message = "You have been subscribed to my email newsletter"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("ryansviglione@gmail.com", "")
    server.sendmail("ryansviglione@gmail.com", email, message)
    '''
    if not first_name or not last_name or not email:
        error_statement = "All form fields are required"
        return render_template('fail.html', error_statement = error_statement,
                               first_name = first_name, last_name = last_name, email = email)

    subscribers.append(f"{first_name} {last_name} {email}")
    title_three = 'Muchas gracias.'
    return render_template('form.html', title=title_three, subscribers=subscribers)

@app.route('/music')
def music():
    title_four = 'Escuche gratis.'
    return render_template('music.html', title=title_four)

if __name__ == "__main__":
    app.run(debug=True)

#####################################RESERVES###############################################

#first_name = first_name, last_name= last_name, email = email
    '''
 <img src="static/images/SoundCloud.png" width="300">
        <a href="https://www.qries.com/">
    '''
