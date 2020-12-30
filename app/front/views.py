from flask import Flask, render_template
from . import front


@front.route('/')
def index():
    return render_template("index.html")
