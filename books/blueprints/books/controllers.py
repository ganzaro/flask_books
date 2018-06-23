from flask import jsonify, request, current_app
import json

from . import books
from .models import Publisher
from books.app import db

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
@books.route('/api/publishers<int:id>', methods=['GET'])
def get_publisher(id):
    res = Publisher.query.filter_by(id).first()
    # TODO add not found exception
    return json.dumps(res)

# add
@books.route('/api/publishers/add', methods=['POST'])
def create_publisher():

    name = request.json['name']
    # email = request.json['email']
    
    new_pub = Publisher(name)

    db.session.add(new_pub)
    db.session.commit()

    # return jsonify(new_pub)
    return new_pub.name


# edit

# delete
@books.route('/api/publishers<int:id>', methods=('DELETE',))
# @jwt_required()
def delete_publisher(id):
    pub = Publisher.query.filter_by(id=id).first()
    db.session.delete(pub)
    db.session.commit()
    return '', 200


##########
# Authors
##########







##########
# Books
##########






