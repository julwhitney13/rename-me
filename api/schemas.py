from apiflask import APIFlask, Schema, PaginationSchema, pagination_builder
from apiflask.fields import Integer, String, List, Nested, Field, Dict, DateTime
from apiflask.validators import Range


class NameCardQuery(Schema):
    page = Integer(load_default=1)
    per_page = Integer(load_default=20, validate=Range(max=30))


class NameCardResponse(Schema):
    id = Integer()
    name = String()


class NameCardsPaginateResponse(Schema):
    namecards = List(Nested(NameCardResponse))
    pagination = Nested(PaginationSchema)
