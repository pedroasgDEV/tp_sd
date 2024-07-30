from flask import Blueprint, request, jsonify, current_app
from bson.objectid import ObjectId

person_bp = Blueprint('person', __name__)

@person_bp.route('/', methods=['GET'])
def get_all_person():
    person = current_app.db.person.find()
    result = [{'_id': str(item['_id']), 'name': item['name']} for item in person]
    return jsonify(result)

@person_bp.route('/<item_id>', methods=['GET'])
def get_item(item_id):
    item = current_app.db.person.find_one({'_id': ObjectId(item_id)})
    if item:
        return jsonify({'_id': str(item['_id']), 'name': item['name']})
    return jsonify({'error': 'Item not found'}), 404

@person_bp.route('/', methods=['POST'])
def create_item():
    data = request.get_json()
    result = current_app.db.person.insert_one({'name': data['name']})
    return jsonify({'_id': str(result.inserted_id)}), 201

@person_bp.route('/<item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    result = current_app.db.person.update_one(
        {'_id': ObjectId(item_id)},
        {'$set': {'name': data['name']}}
    )
    if result.modified_count:
        return jsonify({'message': 'Item updated'})
    return jsonify({'error': 'Item not found'}), 404

@person_bp.route('/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    result = current_app.db.person.delete_one({'_id': ObjectId(item_id)})
    if result.deleted_count:
        return jsonify({'message': 'Item deleted'})
    return jsonify({'error': 'Item not found'}), 404
