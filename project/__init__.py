# projectの実体

import flask import Flask

def create_app():
    

    @app.route("/")
    def hello():
        return "Hello, World!!"

    from . import app
    app.name_of_the_program()