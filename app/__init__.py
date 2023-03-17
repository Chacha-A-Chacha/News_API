#!/bin/env/python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


Base = declarative_base()

engine = create_engine('sqlite:///news.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


