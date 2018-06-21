
//
development
------------
export FLASK_CONFIG=development

export FLASK_APP=run.py

export FLASK_DEBUG=1


//setup app db on development local machine
flask db init

flask db migrate

flask db upgrade


