from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/status')
def hello_world():
    return jsonify('OK')


@app.route('/applications', methods=['GET', 'POST'])
def applications():
    if request.method == 'POST':
        return jsonify(f'Launch Instance')
    else:
        return jsonify(f'List Instance')


@app.route('/applications/<application_id>', methods=['GET', 'POST', 'DELETE'])
def applications_by_id(application_id):
    if request.method == 'POST':
        return jsonify(f'Update Instance {application_id}')
    elif request.method == 'DELETE':
        return jsonify(f'Delete Instance {application_id}')
    else:
        return jsonify(f'Instance Info for {application_id}')


@app.route('/datasets')
def datasets():
    return jsonify('Method Coming Soon!')


@app.route('/datasets/<dataset_id>')
def datasets_by_id(dataset_id):
    return jsonify('Method Coming Soon!')
