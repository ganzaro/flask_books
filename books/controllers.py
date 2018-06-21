
import os
from flask import flash, redirect, render_template, url_for, request, current_app

from books.app import create_app
config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

@app.route('/hello')
def hello():
   return 'Hello World'









