from flask import render_template, jsonify
from ...models.item_model import get_all_items, create_item, update_item, delete_item, get_item

def index():
    items = get_all_items()
    return render_template('index.html', items=items)

def api_items():
    if request.method == 'POST':
        data = request.json
        item = create_item(data['name'],data['price'])
        return jsonify(item.to_dict(), 201)
    else:
        items = get_all_items()
        return jsonify([item.to_dict() for item in items])
def update_item_view(item_id):
    data = request.json
    item = update_item(item_id, data['name'], data['price'])
    if item:
        return jsonify(item.to_dict())
    return jsonify({'error': 'Item not found'}), 404

def delete_item_view(item_id):
    item = delete_item(item_id)
    if item:
        return jsonify({'message': 'Item Deleted'})
    return jsonify({'error': 'Item not found'}), 404
