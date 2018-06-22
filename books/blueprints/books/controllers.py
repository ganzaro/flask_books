from flask import flash, redirect, render_template, url_for, request, current_app
import json

from . import books
from .models import Publisher

@books.route('/')
def hello():
   return 'Hello Books'


# crud
##########
# Publishers
##########

# list
@books.route('/api/publishers', methods=['GET'])
def get_publishers():
    res = Publisher.query.all()
    return json.dumps(res)

# get

# add

# edit

# delete



##########
# Authors
##########







##########
# Books
##########






