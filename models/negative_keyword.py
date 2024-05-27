from app import db

class NegativeKeyword(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    keyword = db.Column(db.String(128), nullable=False)
    level = db.Column(db.String(64), nullable=False)  # account, campaign, or ad_group
    level_id = db.Column(db.Integer, nullable=False)  # ID of the account, campaign, or ad_group