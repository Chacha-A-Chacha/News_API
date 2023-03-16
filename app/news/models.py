from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from app import db

Base = declarative_base()


class Article(Base):
    __tablename__: str = 'articles'

    id = db.Column(Integer, primary_key=True)
    title = db.Column(String(255), nullable=False)
    description = db.Column(String(255), nullable=False)
    url = db.Column(String, unique=True)
    urlToImage = db.Column(String)
    publishedAt = db.Column(DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(String)

    def __repr__(self):
        return f"<Article(id={self.id}, title='{self.title}', author='{self.author}', published_date='{self.published_date}')>"

"""
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
"""
