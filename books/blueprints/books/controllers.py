from flask import flash, redirect, render_template, url_for, request, current_app

from . import books


@books.route('/')
def hello():
   return 'Hello Books'









