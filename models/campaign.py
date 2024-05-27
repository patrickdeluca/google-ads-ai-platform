from app import db

class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.String(64), unique=True, nullable=False)
    campaign_name = db.Column(db.String(128), nullable=False)
    clicks = db.Column(db.Integer, nullable=False)
    impressions = db.Column(db.Integer, nullable=False)
    ctr = db.Column(db.Float, nullable=False)
    conversions = db.Column(db.Float, nullable=False)
    cost_per_conversion = db.Column(db.Float, nullable=False)
    cost_micros = db.Column(db.Float, nullable=False)
    date_range = db.Column(db.String(64), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    ad_groups = db.relationship('AdGroup', backref='campaign', lazy=True)