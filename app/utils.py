#!/bin/env/python3

from app import db
from app.models import Article, Category

news_sources = {
    "General News": {
        "BBC News": "http://www.bbc.com/news/",
        "CNN": "http://www.cnn.com/",
        "Reuters": "http://www.reuters.com/",
        "The New York Times": "https://www.nytimes.com/",
        "The Guardian": "https://www.theguardian.com/"
    },
    "Technology News": {
        "TechCrunch": "https://techcrunch.com/",
        "Wired": "https://www.wired.com/",
        "The Verge": "https://www.theverge.com/",
        "Engadget": "https://www.engadget.com/",
        "CNET": "https://www.cnet.com/"
    },
    "Sports News": {
        "ESPN": "http://www.espn.com/",
        "BBC Sport": "http://www.bbc.com/sport",
        "Sky Sports": "https://www.skysports.com/",
        "NBC Sports": "https://www.nbcsports.com/",
        "Sports Illustrated": "https://www.si.com/"
    },
    "Business News": {
        "Bloomberg": "https://www.bloomberg.com/",
        "Forbes": "https://www.forbes.com/",
        "The Wall Street Journal": "https://www.wsj.com/",
        "Financial Times": "https://www.ft.com/",
        "CNBC": "https://www.cnbc.com/"
    }
}

def get_news_links(news_sources):
    links = []
    for category, sources in news_sources.items():
        for source in sources:
            links.append(source)
    return links

urls = get_news_links(news_sources)

def scrape_news_data(urls):


def scrape_and_store_data():
    # Scrape news data from source
    news_data = scrape_news_data()

    # Process and clean data
    cleaned_data = clean_news_data(news_data)

    # Create SQLAlchemy model instances and add to database


    def scrape_and_store_data():
        # Scrape news data from source
        news_data = scrape_news_data()

        # Process and clean data
        cleaned_data = clean_news_data(news_data)

        # Create SQLAlchemy model instances and add to database
        for article_data in cleaned_data:
            # Check if the category already exists in the database
            category_name = article_data['category']
            category = Category.query.filter_by(name=category_name).first()
            if not category:
                # If category doesn't exist, create a new category instance and add to the database
                category = Category(name=category_name)
                db.session.add(category)
                db.session.commit()

            # Create an article instance and add to the database
            article = Article(title=article_data['title'],
                              author=article_data['author'],
                              content=article_data['content'],
                              image_url=article_data['image_url'],
                              published_at=article_data['published_at'],
                              category=category)
            db.session.add(article)

        db.session.commit()

    for article_data in cleaned_data:
        article = Article(title=article_data['title'],
                          author=article_data['author'],
                          content=article_data['content'],
                          image_url=article_data['image_url'],
                          published_at=article_data['published_at'])
        db.session.add(article)

    db.session.commit()
