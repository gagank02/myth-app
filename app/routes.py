from flask import render_template
from app import app, db
from app.models import Name
import random
import wikipedia

@app.route('/')
@app.route('/home')
def home():
    wikipedia.set_lang("en")
    db_size = len(Name.query.all())
    deity = Name.query.get(random.randint(1, db_size)).name
    query = deity + ' (mythology)'

    if deity == 'Sol':
        query = deity + ' (Norse mythology)'
    print('Query: ' + query)

    try:
        deity_page = wikipedia.page(query, auto_suggest=False)
    except wikipedia.exceptions.PageError as e:
        print("Page Error")
        deity_page = wikipedia.page(deity, auto_suggest=False)
        query = deity_page.title
    print(deity_page.title)

    try:
        summary = wikipedia.summary(query, sentences=3, auto_suggest=False)
    except wikipedia.exceptions.DisambiguationError as e:
        print("Disambiguation Error")
        summary = wikipedia.summary(deity, auto_suggest=False)
        
    try:
        img_path = deity_page.images[0]
    except IndexError as e:
        img_path = 'https://st4.depositphotos.com/14953852/24787/v/600/depositphotos_247872612-stock-illustration-no-image-available-icon-vector.jpg'
    
    return render_template('home.html', deity=deity,
                                        summary=summary,
                                        img=img_path)