import json

from flask import jsonify, request, current_app

from . import books
from .models import Publisher
from .serializers import pub_schema, pubs_schema
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
    query = Publisher.query.all()
    result = pubs_schema.dump(query)
    return jsonify(result.data)
    # return query


# get
@books.route('/api/publishers/<int:id>', methods=['GET'])
def get_publisher(id):
    query = Publisher.query.filter_by(id=id).first()
    result = pub_schema.dump(query)
    return jsonify(result.data)
    # TODO add not found exception


# add
@books.route('/api/publishers/add', methods=['POST'])
def create_publisher(**kwargs):
    # TODO check for duplicate b4 adding to db
    name = request.json['name']
    # email = request.json['email']
    
    new_pub = Publisher(name, **kwargs)

    db.session.add(new_pub)
    db.session.commit()

    result = pub_schema.dump(new_pub).data
    return jsonify(result)


# update
@books.route('/api/publishers/edit/<int:id>', methods=['PUT'])
def update_publisher(id):
    pub = Publisher.query.filter_by(id=id).first()

    name = request.json['name']
    # email = request.json['email']

    pub.name = name

    db.session.commit()

    result = pub_schema.dump(pub).data
    return jsonify(result)    


# delete
@books.route('/api/publishers/del/<int:id>', methods=('DELETE',))
# @jwt_required()
def delete_publisher(id):
    pub = Publisher.query.filter_by(id=id).first()
    db.session.delete(pub)
    db.session.commit()
    return 'Deleted', 200


##########
# Authors
##########







##########
# Books
##########






