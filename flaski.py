from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def create_app():
    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app

@app.route('/')
def index():
    title = "Welcome! - ¡Bienvenidos!"
    return render_template('index.html', title=title)

@app.route('/timeline')
def timeline():
    title_timeline = "Timeline of my life!"
    return render_template("timeline.html", title=title_timeline)

@app.route('/about')
def about():
    title = "Links to Ryan's other websites"
    return render_template("about.html", title= title)

@app.route('/downloadable_files')
def downloadable_files():
    title_files = "Links to Ryan's other websites"
    return render_template("downloadable_files.html", title_files= title_files)

@app.route('/subscribe')
def subscribe():
    title_two = 'Puedes subscribirte ahora'
    return render_template('subscribe.html', title=title_two)

@app.route('/practice_Spanish')
def practice_Spanish():
    title_four = 'Practice Spanish here'
    return render_template('practice_Spanish.html', title=title_four)

#MadLibs funcationality and logic
@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    AWESOMENESS = [
        'asombroso/asombrosa', 'increíble', 'especial', 'genial', 'inteligente', 'agradable', 'una persona excelente',
        'muy importante', 'fantástico/fantástica', 'chido/chida', 'bueno/buena', 'interesante']

    compliment = choice(AWESOMENESS)

    return render_template("cumplido.html", person=player, compliment=compliment)

#End MadLibs functionality and logic

#Dictionary funcionality and logic
@app.route('/definitive')
def define():

    DICTIONARY = {'to talk': 'hablar', 'to eat': 'comer',  'to live': 'vivir', 'to work': 'trabajar', 'to read':
                  'leer', 'escribir': 'to write', 'bailar': 'to dance', 'cantar': 'to sing', 'to study': 'estudiar',
                  'to go': 'ir', 'jugar': 'to play (a sport or game)', 'tocar': 'to play (an instrument)', 'to run':
                  'correr', 'to watch': 'ver/mirar', 'to draw': 'dibujar', 'to swim': 'nadar', 'to drink': 'beber',
                  'to practice': 'practicar', 'to see': 'ver/mirar', 'to sleep': 'dormir', 'to travel': 'viajar'}

    word = request.args.get("definition_word")

    if word in DICTIONARY:
        meaning=DICTIONARY[word]
        return render_template('definition.html', meaning = meaning, word = word)
    else:
        return render_template('fail_dictionary.html')

#Dictionary funcionality and logic
@app.route('/definitive_dos')
def define_dos():

    DICTIONARY_DOS = {'hablar': 'to talk', 'comer': 'to eat',  'vivir': 'to live', 'trabajar': 'to work', 'leer':
                  'to read', 'escribir': 'to write', 'bailar': 'to dance', 'cantar': 'to sing', 'estudiar': 'to study',
                  'ir': 'to go', 'jugar': 'to play (a sport or game)', 'tocar': 'to play (an instrument)', 'correr':
                  'to run', 'ver': 'to watch/see', 'mirar': 'to watch/see', 'dibujar': 'to draw', 'nadar': 'to swim', 'beber': 'to drink',
                  'practicar': 'to practice', 'dormir': 'to sleep', 'viajar': 'to travel'}

    word_two = request.args.get("definition_word_dos")

    if word_two in DICTIONARY_DOS:
        meaning_two=DICTIONARY_DOS[word_two]
        return render_template('definition_two.html', meaning_two = meaning_two, word_two = word_two)
    else:
        return render_template('fail_dictionary.html')

@app.route('/diccionario')
def diccionario():
    title_dropdown_6 = 'Diccionario (English to Spanish)'
    return render_template("diccionario.html", title= title_dropdown_6)

#Dropdowns
@app.route('/adjetivos')
def adjetivos():
    title_dropdown_1 = 'Adjetivos/adjectives'
    return render_template("adjetivos.html", title= title_dropdown_1)

@app.route('/sustantivos')
def sustantivos():
    title_dropdown_2 = 'Sustantivos/nouns'
    return render_template("sustantivos.html", title= title_dropdown_2)

@app.route('/Cultura')
def Cultura():
    title_dropdown_3 = 'Cultura/culture'
    return render_template("Cultura.html", title= title_dropdown_3)

@app.route('/verbos')
def verbos():
    title_dropdown_5 = 'Verbos/verbs'
    return render_template("verbos.html", title= title_dropdown_5)

@app.route('/formularios')
def formularios():
    title_dropdown_5 = 'Formularios/forms'
    return render_template("formularios.html", title= title_dropdown_5)

@app.route('/llenar_los_espacios', methods = ["POST", "GET"])
def llenar_los_espacios():
    return render_template("llenar_los_espacios.html")

global answers
answers = []

@app.route('/form_dos', methods = ["POST", "GET"])
def form_dos():

    one = request.form.get("one")
    two = request.form.get("two")
    three = request.form.get("three")
    four = request.form.get("four")
    five = request.form.get("five")

    if not one or not two or not three or not four or not five:
        error_statement = "All form fields are required"
        return render_template('fail_numbers.html', error_statement = error_statement,
                               one = one, two = two, three = three, four = four, five = five)


    if one == "uno" and two == "dos" and three == "tres" and four == "cuatro" and five == "cinco":
        return render_template('perfect_score.html')
    else:
        answers.append(f" One was '{one}', Two was '{two}', Three was '{three}', Four was '{four}', Five was '{five}'.")
        return render_template('form_dos.html', answers=answers)

@app.route('/perfect_score', methods = ["POST", "GET"])
def perfect_score():
    title_perfect = "You got a perfect score!"
    return render_template('perfect_score.html', title = title_perfect, answers=answers)

    one = request.form.get("one")
    two = request.form.get("two")
    three = request.form.get("three")
    four = request.form.get("four")
    five = request.form.get("five")

    answers.append(f"'one' is {one}'two is' {two}'three is' {three} 'four is' {four} 'five is' {five}")
    return answers

@app.route('/music')
def music():
    title_four = '¡Escuche música!'
    return render_template('music.html', title=title_four)

@app.route('/problemas_de_verbos')
def problemas_de_verbos():
    title_vbs = 'Listen to the recordings and write the English or Spanish translation on the line.'
    return render_template('problemas_de_verbos.html', title=title_vbs)

global verb_answers
verb_answers = []

@app.route('/form_tres', methods = ["POST", "GET"])
def form_tres():

    vb_one_1 = request.form.get("vb_one")
    vb_two_2 = request.form.get("vb_two")
    vb_three_3 = request.form.get("vb_three")

    if vb_one_1 == "Today is Tuesday the second of November." and vb_two_2 == "It is 7:00 at night." and vb_three_3 == "I like to use the computer.":
        return render_template('perfect_score_dos.html', verb_answers = verb_answers)
    else:
        verb_answers.append(f"#1. {vb_one_1}   #2.     {vb_two_2}        #3.{vb_three_3}.")
        return render_template('form_tres.html', verb_answers=verb_answers)

global verb_answers_dos
verb_answers_dos = []

@app.route('/form_cuatro', methods = ["POST", "GET"])
def form_cuatro():

    ser = request.form.get("ser")
    ir = request.form.get("ir")
    estudiar = request.form.get("estudiar")
    hablar = request.form.get("hablar")
    leer = request.form.get("leer")

    if ser == "es" and ir == "voy" and estudiar == "estudiamos" and hablar == "habla" and leer == "leen":
        return render_template('perfect_score_tres.html', verb_answers_dos=verb_answers_dos)
    else:
        verb_answers_dos.append(f"# #1 was '{ser}' --  #2. was '{ir}'   --     #3. was '{estudiar}'   #4. was  '{hablar}'  --    #5 was '{leer}'     ")
        return render_template('form_cuatro.html', verb_answers_dos=verb_answers_dos)

#Below is the if __name__ == "__main__": statement (Dunder)

if __name__ == "__main__":
    app.run(debug=True)
