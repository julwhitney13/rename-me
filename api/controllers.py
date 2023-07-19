from http.client import HTTPException
from api.models import NameCard as NameCardModel
from api.schemas import NameCardQuery, NameCardsPaginateResponse
from apiflask import pagination_builder
from app import app, db
from flask import make_response
import time


@app.route('/time')
def get_current_time():
    print('here', time.time())
    return {'time': time.time()}


@app.get('/names')
@app.input(NameCardQuery, location='query')
@app.output(NameCardsPaginateResponse)
def get_names(request):
    pagination = db.paginate(
        db.select(NameCardModel),
        page=request['page'],
        per_page=request['per_page']
    )
    ncs = pagination.items
    return {
        'pets': ncs,
        'pagination': pagination_builder(pagination)
    }
