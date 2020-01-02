from flask import render_template
from app import app
from .request import get_news,get_sources

#Views
@app.route('/')
def index():
    
    '''
    View root page function that returns the index page and its data
    '''
    
    title = 'News World'
    country_news = get_news('uk')
    news_source = get_sources()
    return render_template('index.html', title = title, country = country_news, sources = news_source)

# @app.route('/news/<news_id>')
# def news(news_id):

#     '''
#     View news page function that returns the movie details page and its data
#     '''
#     return render_template('news.html',id = news_id)