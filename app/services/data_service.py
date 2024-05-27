from app import db
from app.models.ad import Ad

def get_hierarchical_data():
    query = """
    WITH RECURSIVE AdHierarchy AS (
        SELECT id, campaign_id, ad_group_id, ad_id, headlines, descriptions, final_urls, clicks, impressions, ctr, conversions, cost_per_conversion, cost_micros, date_range
        FROM ad_data
        WHERE ad_group_id IS NULL
        UNION ALL
        SELECT a.id, a.campaign_id, a.ad_group_id, a.ad_id, a.headlines, a.descriptions, a.final_urls, a.clicks, a.impressions, a.ctr, a.conversions, a.cost_per_conversion, a.cost_micros, a.date_range
        FROM ad_data a
        JOIN AdHierarchy ah ON a.ad_group_id = ah.ad_id
    )
    SELECT * FROM AdHierarchy;
    """
    result = db.session.execute(query)
    return result.fetchall()