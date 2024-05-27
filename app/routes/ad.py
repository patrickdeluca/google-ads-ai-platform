from flask import Blueprint, request, jsonify
from app import db
from app.models.ad import Ad
from app.schemas.ad import AdSchema

bp = Blueprint('ad', __name__, url_prefix='/ads')

@bp.route('/', methods=['POST'])
def create_ad():
    data = request.get_json()
    ad_schema = AdSchema()
    ad = ad_schema.load(data)
    db.session.add(ad)
    db.session.commit()
    return ad_schema.jsonify(ad), 201