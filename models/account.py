from app import db

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.String(64), unique=True, nullable=False)
    account_name = db.Column(db.String(128), nullable=False)
    date_range = db.Column(db.String(64), nullable=False)
    campaigns = db.relationship('Campaign', backref='account', lazy=True)