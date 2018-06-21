import os
from flask import Flask, render_template, jsonify

from books.app import create_app


config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

@app.route("/hello")
def index():
    return "Hello, World!"

@app.route('/help', methods = ['GET'])
def help():
    """Print available functions."""
    func_list = {}
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            func_list[rule.rule] = app.view_functions[rule.endpoint].__doc__
    return jsonify(func_list)


if __name__ == '__main__':
    app.run()







