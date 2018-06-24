import json

from flask import jsonify, request, current_app

from . import profile
from .models import UserProfile
# from .serializers import pub_schema, pubs_schema
from books.app import db

@profile.route('/profile')
def profile1():
   return 'Hello Profile'


# crud
##########
# Publishers
##########
