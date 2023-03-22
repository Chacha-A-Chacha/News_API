from app import app
from flask import render_template, jsonify
from .request import businessArticles, entArticles, get_news_source, healthArticles, publishedArticles, randomArticles, scienceArticles, sportArticles, techArticles, topHeadlines

@app.route('/')
def home():
    articles = publishedArticles()

    #render_template('home.html', articles = articles)
    return jsonify(articles) 

@app.route('/headlines')
def headlines():
    headlines = topHeadlines()

    #render_template('headlines.html', headlines = headlines)
    return jsonify(headlines) 

@app.route('/articles')
def articles():
    random = randomArticles()

    #render_template('articles.html', random = random)
    return jsonify(random) 

@app.route('/sources')
def sources():
    newsSource = get_news_source()

    #render_template('sources.html', newsSource = newsSource)
    return newsSource

@app.route('/category/business')
def business():
    sources = businessArticles()

    #render_template('business.html', sources = sources)
    return jsonify(sources) 

@app.route('/category/tech')
def tech():
    sources = techArticles()

    #render_template('tech.html', sources = sources)
    return jsonify(sources) 

@app.route('/category/entertainment')
def entertainment():
    sources = entArticles()

    #render_template('entertainment.html', sources = sources)
    return jsonify(sources) 

@app.route('/category/science')
def science():
    sources = scienceArticles()

    #render_template('science.html', sources = sources)
    return jsonify(sources) 

@app.route('/category/sports')
def sports():
    sources = sportArticles()

    #render_template('sport.html', sources = sources)
    return jsonify(sources) 

@app.route('/category/health')
def health():
    sources = healthArticles()

    #render_template('health.html', sources = sources)
    return jsonify(sources) 
