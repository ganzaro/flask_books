from flask import Blueprint

auth = Blueprint('auth', __name__, template_folder='templates')

from . api import json_api, web_api