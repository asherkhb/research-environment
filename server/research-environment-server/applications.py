from flask import jsonify


def list_applications():
    return jsonify('List Instances')


def launch_application():
    return jsonify(f'Launch Instance')


def describe_application(application_id):
    return jsonify(f'Instance Info for {application_id}')


def update_application(application_id):
    return jsonify(f'Update Instance {application_id}')


def delete_application(application_id):
    return jsonify(f'Delete Instance {application_id}')
