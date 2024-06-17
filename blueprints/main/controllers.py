from flask import Blueprint
from blueprints.main.views import index, api_items, update_item_view, delete_item_view

main_bp = Blueprint('main',  __name__)

main_bp.add_url_rule('/',view_func=index)
main_bp.add_url_rule('/api/items',view_func=api_items, methods=['GET', 'POST'])
main_bp.add_url_rule('/api/items/<int:item_id>', view_func=update_item_view, methods=['PUT'])
main_bp.add_url_rule('/api/items/<int:item_id>', view_func=delete_item_view, methods=['DELETE'])
