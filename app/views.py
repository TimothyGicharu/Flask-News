from flask import render_template
from app import app
from .request import get_source, get_source_articles

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    # Getting news headlines
    news_source = get_source()
    title = 'Home - Top News'
    return render_template('index.html', title = title,  sources = news_source)

@app.route('/sources/<id>')
def source_articles(id):
    '''
    View news page function that returns the news details and the 
    content 
    '''
    articles = get_source_articles(id)
    return render_template('articles.html', articles = articles)

@app.route('/about')
def about():
    return render_template('about.html')