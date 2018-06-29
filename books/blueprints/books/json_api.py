import json

from flask import jsonify, request, current_app
from flask.views import MethodView

from . import books
from .models import Publisher
from .serializers import pub_schema, pubs_schema
from books.app import db
from . usecase import GetPublishersUseCase

##########
# Publishers
##########

class PublisherAPI(MethodView):

    def __init__(self, usecase=GetPublishersUseCase):
        self.usecase = usecase()
    
    def get(self, pub_id):
        if not pub_id:
            self.usecase.execute()
            # query = Publisher.query.all()
        else:
            query = Publisher.query.filter_by(id=id).first()
        result = pubs_schema.dump(query)
        return jsonify(result.data)


    # @books.route('/api/publishers/add', methods=['POST'])
    def post(self, **kwargs):
        # TODO check for duplicate b4 adding to db
        name = request.json['name']
        # email = request.json['email']
        
        new_pub = Publisher(name, **kwargs)

        db.session.add(new_pub)
        db.session.commit()

        result = pub_schema.dump(new_pub).data
        return jsonify(result)


    # update
    # @books.route('/api/publishers/edit/<int:id>', methods=['PUT'])
    def put(self, pub_id):
        pub = Publisher.query.filter_by(id=id).first()

        name = request.json['name']
        # email = request.json['email']

        pub.name = name

        db.session.commit()

        result = pub_schema.dump(pub).data
        return jsonify(result)    


    # delete
    # @books.route('/api/publishers/del/<int:id>', methods=('DELETE',))
    # @jwt_required()
    def delete(self, id):
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






