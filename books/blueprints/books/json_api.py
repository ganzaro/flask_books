import json

from flask import jsonify, request, current_app
from flask.views import MethodView

from . import books
from .models import Publisher
from .serializers import pub_schema, pubs_schema
from books.app import db
from . usecase import GetPublishersUseCase, \
            GetPublisherUseCase, AddPublisherUseCase

##########
# Publishers
##########

class PublisherAPI(MethodView):

    def __init__(self, 
                get_pubs_uc=None, 
                get_pub_uc=None,
                create_pub_uc=None,
                edit_pub_uc=None):

        self.get_pubs_uc = get_pubs_uc or GetPublishersUseCase()
        self.get_pub_uc = get_pub_uc or GetPublisherUseCase()
        self.create_pub_uc = create_pub_uc or AddPublisherUseCase()
    
    def get(self, pub_id):
        if not pub_id:
            query = self.get_pubs_uc.execute()
            result = pubs_schema.dump(query)
        else:
            self.get_pub_uc.set_params(pub_id)
            query = self.get_pub_uc.execute()
            result = pub_schema.dump(query)

        return jsonify(result.data)


    def post(self, **kwargs):
        # TODO check for duplicate b4 adding to db
        name = request.json['name']
        # email = request.json['email']
        
        new_pub = Publisher(name, **kwargs)

        self.create_pub_uc.set_params(new_pub)
        self.create_pub_uc.execute()

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






