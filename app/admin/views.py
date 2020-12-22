from flask import Flask
from . import admin


@admin.route('/<name>')
def hello_admin(name):
    return 'Hello Admin %s!' % name
