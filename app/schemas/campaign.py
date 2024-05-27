from app import ma
from app.models.campaign import Campaign

class CampaignSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Campaign
        load_instance = True