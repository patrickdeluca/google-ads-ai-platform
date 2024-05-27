from app import ma
from app.models.ad_group import AdGroup

class AdGroupSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AdGroup
        load_instance = True