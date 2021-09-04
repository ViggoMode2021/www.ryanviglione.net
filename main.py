from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = 'Ryan Vig blog'
    return render_template('index.html', title=title)

@app.route('/about')
def about():
    names = ['Vida', 'Trabajo', 'Pasatiempos', 'Enlaces']
    return render_template("about.html", names = names)

if __name__ == "__main__":
    app.run(debug=True)


'''

   {% if title %}
        {{ title }}
      {% else %}
        Ryan Viglione
        {{ endif }}
'''
