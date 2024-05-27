from app import db

class Ad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ad_id = db.Column(db.String(64), unique=True, nullable=False)
    headlines = db.Column(db.Text, nullable=False)
    descriptions = db.Column(db.Text, nullable=False)
    final_urls = db.Column(db.Text, nullable=False)
    clicks = db.Column(db.Integer, nullable=False)
    impressions = db.Column(db.Integer, nullable=False)
    ctr = db.Column(db.Float, nullable=False)
    conversions = db.Column(db.Float, nullable=False)
    cost_per_conversion = db.Column(db.Float, nullable=False)
    cost_micros = db.Column(db.Float, nullable=False)
    date_range = db.Column(db.String(64), nullable=False)
    ad_group_id = db.Column(db.Integer, db.ForeignKey('ad_group.id'), nullable=False)