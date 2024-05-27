import pytest
from app import create_app, db
from app.models.account import Account
from app.models.campaign import Campaign
from app.models.ad_group import AdGroup
from app.models.ad import Ad
from app.models.negative_keyword import NegativeKeyword

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
    })

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_account(client):
    response = client.post('/accounts/', json={
        'account_id': '123',
        'account_name': 'Test Account',
        'date_range': '2023-01-01 to 2023-12-31'
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['account_id'] == '123'
    assert data['account_name'] == 'Test Account'

def test_create_campaign(client):
    response = client.post('/campaigns/', json={
        'campaign_id': '456',
        'campaign_name': 'Test Campaign',
        'clicks': 100,
        'impressions': 1000,
        'ctr': 0.1,
        'conversions': 10,
        'cost_per_conversion': 1.0,
        'cost_micros': 1000000,
        'date_range': '2023-01-01 to 2023-12-31',
        'account_id': 1
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['campaign_id'] == '456'
    assert data['campaign_name'] == 'Test Campaign'

def test_create_ad_group(client):
    response = client.post('/ad_groups/', json={
        'ad_group_id': '789',
        'ad_group_name': 'Test Ad Group',
        'clicks': 50,
        'impressions': 500,
        'ctr': 0.1,
        'conversions': 5,
        'cost_per_conversion': 2.0,
        'cost_micros': 500000,
        'date_range': '2023-01-01 to 2023-12-31',
        'campaign_id': 1
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['ad_group_id'] == '789'
    assert data['ad_group_name'] == 'Test Ad Group'

def test_create_ad(client):
    response = client.post('/ads/', json={
        'ad_id': '101112',
        'headlines': ['Headline 1', 'Headline 2'],
        'descriptions': ['Description 1', 'Description 2'],
        'final_urls': ['http://example.com'],
        'clicks': 25,
        'impressions': 250,
        'ctr': 0.1,
        'conversions': 2.5,
        'cost_per_conversion': 4.0,
        'cost_micros': 250000,
        'date_range': '2023-01-01 to 2023-12-31',
        'ad_group_id': 1
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['ad_id'] == '101112'
    assert data['headlines'] == ['Headline 1', 'Headline 2']

def test_create_negative_keyword(client):
    response = client.post('/negative_keywords/', json={
        'keyword': 'negative keyword',
        'level': 'account',
        'level_id': 1
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['keyword'] == 'negative keyword'
    assert data['level'] == 'account'