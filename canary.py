#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request, url_for

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Your canary is dead'}), 404)

canaries = [
    {
        '_id': 1,
        'canary': u'BitCanary',
        'description': u'BitCanary status',
        'status': True
    }
]

def make_public_canary(canary):
    new_canary = {}
    for field in canary:
        if field == '_id':
            new_canary['uri'] = url_for('get_canary', canary_id=canary['_id'], _external=True)
        else:
            new_canary[field] = canary[field]
    return new_canary

@app.route('/canary', methods=['GET'])
def get_canaries():
    return jsonify({'canaries': [make_public_canary(canary) for canary in canaries]})

@app.route('/canary/<int:canary_id>', methods=['GET'])
def get_canary(canary_id):
    canary = [canary for canary in canaries if canary['_id'] == canary_id]
    if len(canary) == 0:
        abort(404)
    return jsonify({'canary': canary[0]})

@app.route('/canary', methods=['POST'])
def create_canary():
    if not request.json or not 'canary' in request.json:
        abort(400)
    canary = {
        '_id': canaries[-1]['_id'] + 1,
        'title': request.json['canary'],
        'description': request.json.get('description', ""),
        'status': True
    }
    canaries.append(canary)
    return jsonify({'canary': canary}), 201

@app.route('/canary/<int:canary_id>', methods=['DELETE'])
def delete_canary(canary_id):
    canary = [canary for canary in canaries if canary['_id'] == canary_id]
    if len(canary) == 0:
        abort(404)
    canaries.remove(canary[0])
    return jsonify({'status': True})

if __name__ == '__main__':
    app.run(debug=True)