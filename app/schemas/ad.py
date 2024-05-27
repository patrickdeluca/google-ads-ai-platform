from app import ma
from app.models.ad import Ad
from marshmallow import validates, ValidationError

class AdSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ad
        load_instance = True

    @validates('headlines')
    def validate_headlines(self, value):
        if len(value) > 15:
            raise ValidationError('Maximum 15 headlines are allowed.')
        for headline in value:
            if len(headline) > 30:
                raise ValidationError('Each headline must be 30 characters or less.')

    @validates('descriptions')
    def validate_descriptions(self, value):
        if len(value) > 4:
            raise ValidationError('Maximum 4 descriptions are allowed.')
        for description in value:
            if len(description) > 90:
                raise ValidationError('Each description must be 90 characters or less.')