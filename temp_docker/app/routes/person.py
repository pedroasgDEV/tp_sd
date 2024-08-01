from flask import Blueprint, request, jsonify, current_app
from app.utils.database.collections.people import PeopleCollection

person_bp = Blueprint('person', __name__)
col = PeopleCollection(current_app.config["db"])

@person_bp.route('/<int:qnt>', methods=['GET'])
def get_random_persons(qnt):
    result = col.select_many_random(qnt)
    return jsonify(result)

@person_bp.route('/', methods=['POST'])
def create_item():
    data = request.get_json()
    result = col.insert_document(data)
    return jsonify({'_id': str(result.inserted_id)}), 201

@person_bp.route('/<item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    result = col.edit_registry(item_id, data)
    if result.modified_count:
        return jsonify({'message': 'Item updated'})
    return jsonify({'error': 'Item not found'}), 404

@person_bp.route('/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    result = col.delete_registry(item_id)
    if result.deleted_count:
        return jsonify({'message': 'Item deleted'})
    return jsonify({'error': 'Item not found'}), 404
