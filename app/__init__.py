from flask import Flask
from .config import DevConfig
#initializing application
app = Flask(__name__, instance_relative_config = True)


# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views

from flask_bootstrap import Bootstrap

#setting up congigurations
app.config.from_object(DevConfig)
app.config.from_pyfile("config.py")

#initializing flask bootstarp extension
bootstrap = Bootstrap(app)