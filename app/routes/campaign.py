from flask import Blueprint, request, jsonify
from app import db
from app.models.campaign import Campaign
from app.schemas.campaign import CampaignSchema

bp = Blueprint('campaign', __name__, url_prefix='/campaigns')

@bp.route('/', methods=['POST'])
def create_campaign():
    data = request.get_json()
    campaign_schema = CampaignSchema()
    campaign = campaign_schema.load(data)
    db.session.add(campaign)
    db.session.commit()
    return campaign_schema.jsonify(campaign), 201