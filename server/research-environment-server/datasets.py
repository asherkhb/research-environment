from flask import jsonify


def list_datasets():
    return jsonify(f'List Datasets')


def create_dataset():
    return jsonify(f'Create Dataset')


def describe_dataset(dataset_id):
    return jsonify(f'Dataset Info for {dataset_id}')


def update_dataset(dataset_id):
    return jsonify(f'Update Dataset {dataset_id}')


def delete_dataset(dataset_id):
    return jsonify(f'Delete Dataset {dataset_id}')
