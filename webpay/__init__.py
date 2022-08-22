from flask import Blueprint

bp = Blueprint('webpay_plus', __name__)

from . import views
