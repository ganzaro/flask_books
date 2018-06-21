import os

from books.app import create_app


config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

@app.route("/")
def index():
    return "Hello, World!"




if __name__ == '__main__':
    app.run()







