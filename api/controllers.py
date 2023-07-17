from functools import wraps
from http.client import HTTPException
from api.models import NameCard
from app import app, db
from flask import make_response
import time


@app.route('/time')
def get_current_time():
    print('here', time.time())
    return {'time': time.time()}


@app.route('/names')
def get_names():
    page = db.paginate(db.select(NameCard))
    return page
