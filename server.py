from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database (for demonstration purposes)
items = [
    {"id":1, "title":"Book 1", "author":"Author 1"},
    {"id":2, "title":"Book 2", "author":"Author 2"},
    {"id":3, "title":"Book 3", "author":"Author 3"}
]

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is not None:
        return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = {
        'id': len(items) + 1,
        'name': data['name']
    }
    items.append(new_item)
    return jsonify(new_item), 201

@app.route('/items/<int:item_id>;', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    item = next((item for item in items if item['id'] == item_id), None)
    if item is not None:
        item['name'] = data['name']
        return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'message': 'Item deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)