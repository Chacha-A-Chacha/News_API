from app import app
from flask import render_template, jsonify
from .request import businessArticles, entArticles, get_news_source, healthArticles, publishedArticles, randomArticles, scienceArticles, sportArticles, techArticles, topHeadlines

@app.route('/')
def home():
    articles = publishedArticles()

    render_template('home.html', articles=articles)
    return jsonify(articles) 

@app.route('/headlines')
def headlines():
    headlines = topHeadlines()

    return jsonify(headlines)

@app.route('/articles')
def articles():
    random = randomArticles()

    return jsonify(random)

@app.route('/sources')
def sources():
    newsSource = get_news_source()

    return newsSource

@app.route('/category/business')
def business():
    sources = businessArticles()

    return jsonify(sources)

@app.route('/category/tech')
def tech():
    sources = techArticles()

    return jsonify(sources)

@app.route('/category/entertainment')
def entertainment():
    sources = entArticles()

    return jsonify(sources)

@app.route('/category/science')
def science():
    sources = scienceArticles()

    return jsonify(sources)

@app.route('/category/sports')
def sports():
    sources = sportArticles()

    return jsonify(sources)

@app.route('/category/health')
def health():
    sources = healthArticles()

    return jsonify(sources)
