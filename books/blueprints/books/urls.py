

# user_view = UserAPI.as_view('user_api')
# app.add_url_rule('/users/', defaults={'user_id': None},
#                  view_func=user_view, methods=['GET',])
# app.add_url_rule('/users/', view_func=user_view, methods=['POST',])
# app.add_url_rule('/users/<int:user_id>', view_func=user_view,
#                  methods=['GET', 'PUT', 'DELETE'])

from . json_api import PublisherAPI
from . import books

# auth_blueprint = Blueprint('auth', __name__)

# Define the API resource
pub_api = PublisherAPI.as_view('pub_api')
# login_view = LoginView.as_view('login_view')

# Add the url rule for registering a user
books.add_url_rule(
    '/api/v1/publishers',
    defaults={'pub_id': None},
    view_func=pub_api,
    methods=['GET'])

books.add_url_rule(
    '/api/v1/publishers',
    view_func=pub_api,
    methods=['POST']
)

books.add_url_rule(
    '/api/v1/publishers/<int:pub_id>', 
    view_func=pub_api,
    methods=['GET', 'PUT', 'DELETE'])


# @books.route('/api/publishers', methods=['GET'])

