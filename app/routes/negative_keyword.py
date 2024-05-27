from flask import Blueprint, request, jsonify
from app import db
from app.models.negative_keyword import NegativeKeyword
from app.schemas.negative_keyword import NegativeKeywordSchema

bp = Blueprint('negative_keyword', __name__, url_prefix='/negative_keywords')

@bp.route('/', methods=['POST'])
def create_negative_keyword():
    data = request.get_json()
    negative_keyword_schema = NegativeKeywordSchema()
    negative_keyword = negative_keyword_schema.load(data)
    db.session.add(negative_keyword)
    db.session.commit()
    return negative_keyword_schema.jsonify(negative_keyword), 201