from flask import Flask
from . import front


@front.route('/')
def hello_world():
    return 'Hello World!'
