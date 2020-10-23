from flask import Flask, jsonify, request
from flask_restx import Resource, Api

from applications import *
from datasets import *

app = Flask(__name__)
api = Api(app)


@api.route('/status')
class Status(Resource):
    def get(self):
        return jsonify('OK')


@api.route('/applications')
class Applications(Resource):
    def get(self):
        return list_applications()
    def post(self):
        return launch_application()


@api.route('/applications/<application_id>')
class ApplicationsById(Resource):
    def get(self, application_id):
        return describe_application(application_id)
    def post(self, application_id):
        return update_application(application_id)
    def delete(self, application_id):
        return delete_application(application_id)


@api.route('/datasets')
class Datasets(Resource):
    def get(self):
        return list_datasets()
    def post(self):
        return create_dataset()


@api.route('/datasets/<dataset_id>')
class DatasetsById(Resource):
    def get(self, dataset_id):
        return describe_dataset(dataset_id)
    def post(self, dataset_id):
        return update_dataset(dataset_id)
    def delete(self, dataset_id):
        return delete_dataset(dataset_id)


if __name__ == '__main__':
    app.run(debug=True)
