from flask import Blueprint

profile = Blueprint('profile', __name__)

from .api import json_api