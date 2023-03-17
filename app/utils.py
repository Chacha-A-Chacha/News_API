#!/bin/env/python3

from app import db
from app.models import Article


def scrape_and_store_data():
    # Scrape news data from source
    news_data = scrape_news_data()

    # Process and clean data
    cleaned_data = clean_news_data(news_data)

    # Create SQLAlchemy model instances and add to database
    for article_data in cleaned_data:
        article = Article(title=article_data['title'],
                          author=article_data['author'],
                          content=article_data['content'],
                          image_url=article_data['image_url'],
                          published_at=article_data['published_at'])
        db.session.add(article)

    db.session.commit()
