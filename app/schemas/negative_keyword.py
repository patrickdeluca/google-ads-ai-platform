from app import ma
from app.models.negative_keyword import NegativeKeyword

class NegativeKeywordSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = NegativeKeyword
        load_instance = True