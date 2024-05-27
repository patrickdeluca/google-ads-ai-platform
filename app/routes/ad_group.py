from flask import Blueprint, request, jsonify
from app import db
from app.models.ad_group import AdGroup
from app.schemas.ad_group import AdGroupSchema

bp = Blueprint('ad_group', __name__, url_prefix='/ad_groups')

@bp.route('/', methods=['POST'])
def create_ad_group():
    data = request.get_json()
    ad_group_schema = AdGroupSchema()
    ad_group = ad_group_schema.load(data)
    db.session.add(ad_group)
    db.session.commit()
    return ad_group_schema.jsonify(ad_group), 201