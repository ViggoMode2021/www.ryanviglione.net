from flask import Flask, render_template, request

app = Flask(__name__)

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
    subscribers.append(f"{first_name} {last_name} {email}")
    title_three = 'Muchas gracias.'
    return render_template('form.html', title=title_three, subscribers=subscribers)

if __name__ == "__main__":
    app.run(debug=True)

#first_name = first_name, last_name= last_name, email = email
