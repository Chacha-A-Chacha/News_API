#!/bin/env/python3

# from app import db
from app.news.models import Article, Category
import requests
import re
from datetime import datetime
from bs4 import BeautifulSoup


def scrape_news_articles():
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

    """
    Scrapes news articles from a list of URLs and returns the article titles, category, content, URLs, article date and image urls as a list of dictionaries.
    """
    article_data = []

    for url in urls:
        # Send a GET request to the URL
        response = requests.get(url)

        # Parse the HTML content of the page using Beautiful Soup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the category of the article
        category = soup.find('meta', {'property': 'article:section'})
        if category:
            category = category.get('content')

        # Find the article date
        date = soup.find('meta', {'property': 'article:published_time'})
        if date:
            date = date.get('content')
            date = datetime.fromisoformat(date)

        # Find the article title, content, URL, and image URL
        title_element = soup.find('h1')
        if title_element:
            title = title_element.text.strip()

        content_element = soup.find('div', {'class': 'article__content'})
        if content_element:
            content = content_element.text.strip()

        url = url

        image_element = soup.find('meta', {'property': 'og:image'})
        if image_element:
            img_url = image_element.get('content')

        # Add the article data to the list of dictionaries
        article_data.append({
                'title': title, 'category': category, 'content': content, 'url': url, 'date': date, 'img_url': 'img_url'
            }
        )

    return article_data


def clean_news_data(article_data):
    cleaned_data = []

    for article in article_data:
        title = article['title']
        category = article['category']
        content = article['content']
        url = article['url']
        date_str = article['date']
        image_url = article['image_url']

        # Convert date string to datetime object
        date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')

        # Remove HTML tags from content
        content = re.sub('<[^<]+?>', '', content)

        # Remove any excess whitespace from title, content, and category
        title = title.strip()
        content = content.strip()
        category = category.strip()

        # Create dictionary of cleaned data and append to list
        cleaned_data.append({
            'title': title,
            'category': category,
            'content': content,
            'url': url,
            'date': date,
            'img_url': image_url
        })

    return cleaned_data


def scrape_and_store_data():
    # Scrape news data from source
    news_data = scrape_news_articles(urls)

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
                          image_url=article_data['img_url'],
                          published_at=article_data['published_at'],
                          category=category)
        db.session.add(article)

    db.session.commit()

    for article_data in cleaned_data:
        article = Article(title=article_data['title'],
                          author=article_data['author'],
                          content=article_data['content'],
                          image_url=article_data['img_url'],
                          published_at=article_data['published_at'])
        db.session.add(article)

    db.session.commit()
