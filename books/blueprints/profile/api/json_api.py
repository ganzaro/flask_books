import json

from flask import jsonify, request, current_app

from .. import profile
from ..data.models import UserProfile
# from .serializers import pub_schema, pubs_schema
from books.app import db

# TODO implement Profile endpoints

@profile.route('/profile')
def profile1():
   return 'Hello Profile'


# mail check
@profile.route('/send_mail')
def send_mail():
    from ..tasks.tasks import send_email
    send_email()

    return 'mail'
