from flask import Blueprint, request, jsonify
from app import db
from app.models.account import Account
from app.schemas.account import AccountSchema

bp = Blueprint('account', __name__, url_prefix='/accounts')

@bp.route('/', methods=['POST'])
def create_account():
    data = request.get_json()
    account_schema = AccountSchema()
    account = account_schema.load(data)
    db.session.add(account)
    db.session.commit()
    return account_schema.jsonify(account), 201