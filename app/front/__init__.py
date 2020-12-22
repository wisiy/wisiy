from flask import Blueprint

front = Blueprint("front", __name__)

import app.front.views
