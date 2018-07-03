from flask import Blueprint

books = Blueprint('books', __name__)

from .api import urls