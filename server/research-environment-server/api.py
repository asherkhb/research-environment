from flask import Flask, jsonify, request
from applications import *
from datasets import *

app = Flask(__name__)


@app.route('/status')
def hello_world():
    return jsonify('OK')


@app.route('/applications', methods=['GET', 'POST'])
def applications():
    if request.method == 'POST':
        return launch_application()
    else:
        return list_applications()


@app.route('/applications/<application_id>', methods=['GET', 'POST', 'DELETE'])
def applications_by_id(application_id):
    if request.method == 'POST':
        return update_application(application_id)
    elif request.method == 'DELETE':
        return delete_application(application_id)
    else:
        return describe_application(application_id)


@app.route('/datasets', methods=['GET', 'POST'])
def datasets():
    if request.method == 'POST':
        return create_dataset()
    else:
        return list_datasets()


@app.route('/datasets/<dataset_id>', methods=['GET', 'POST', 'DELETE'])
def datasets_by_id(dataset_id):
    if request.method == 'POST':
        return update_dataset(dataset_id)
    elif request.method == 'DELETE':
        return delete_dataset(dataset_id)
    else:
        return describe_dataset(dataset_id)
