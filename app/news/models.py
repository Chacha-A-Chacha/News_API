from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from app import db

Base = declarative_base()


class Article(Base):
    __tablename__: str = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    url = Column(String, unique=True)
    urlToImage = Column(String)
    publishedAt = Column(DateTime)
    content = Column(String)


class NewsArticle(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    source = Column(String)
    author = Column(String)
    url = Column(String)
    image_url = Column(String)
    published_at = Column(DateTime, default=datetime.utcnow)


def get_all_news():
    news = NewsArticle.query.all()
    return [article.to_dict() for article in news]


def get_news_by_id(article_id):
    article = NewsArticle.query.filter_by(id=article_id).first()
    return article.to_dict() if article else None
