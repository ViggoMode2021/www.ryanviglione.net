from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


def create_app():
    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app

#Initialize the db
db = SQLAlchemy(app)

#Create db model
class Friends(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __init__(self, first_name, last, email, date_created):
        self.first_name = first_name
        self.last = last
        self.email = email
        self.date_created = date_created

#Create a function to return string
    #def __repr__(self):
        #return '<Name %r>' % self.id

subscribers = []

db.create_all()
db.session.commit()

@app.route('/')
def index():
    title = 'Ryan Vig blog'
    return render_template('index.html', title=title)

@app.route('/about')
def about():
    title = 'Sobre Ryan Viglione'
    attributes = ['Vida', 'Trabajo', 'Pasatiempos', 'Enlaces']
    return render_template("about.html", attributes = attributes, title= title)

@app.route('/subscribe')
def subscribe():
    title_two = 'Puedes subscribirte ahora.'
    return render_template('subscribe.html', title=title_two)

@app.route('/practice_Spanish')
def practice_Spanish():
    title_four = 'Practice Spanish here.'
    return render_template('practice_Spanish.html', title=title_four)

@app.route('/practice_Spanish', methods = ["POST"])
def form_two():
    respuesta = request.form.get("respuesta")
    if request.form.get == "hola":
        print('wow')

@app.route('/form', methods = ["POST", "GET"])
def form():
    '''
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    '''
    if request.method == "POST":
        friend_name = request.form['first_name', 'last_name', 'email']
        new_friend = Friends(name=friend_name)

        try:
            db.session.add(new_friend)
            db.session.commit()
            return redirect ('/subscribe')

        except:
            return "Error"

    else:
        friends = Friends.query.order_by(Friends.date_created)
        return render_template("subscribe.html")

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
    db.create_all()
    app.run(debug=True)

#####################################RESERVES###############################################

#first_name = first_name, last_name= last_name, email = email
    '''
 <img src="static/images/SoundCloud.png" width="300">
        <a href="https://www.qries.com/">
    '''
