from flask import Blueprint, request, jsonify
from app.services.ai_service import generate_response

bp = Blueprint('ai', __name__, url_prefix='/ai')

@bp.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = generate_response(user_input)
    return jsonify(response)