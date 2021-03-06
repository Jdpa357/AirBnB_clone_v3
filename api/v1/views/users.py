#!/usr/bin/python3
'''
Handles all default RestFul API actions for users
'''
from api.v1.views import app_views
from models import storage
from flask import jsonify, request, abort
from models.user import User


@app_views.route('/users/', methods=['GET'], strict_slashes=False)
def get_all_users():
    ''' Retrieves a list of all user objects in the DB '''
    data = storage.all(User)
    new = [val.to_dict() for key, val in data.items()]
    return jsonify(new)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id=None):
    ''' Retrieves an individual user object '''
    obj = storage.get(User, user_id)
    if obj is None:
        ''' If no state object with that id exists aborts '''
        abort(404)
    obj = obj.to_dict()
    return jsonify(obj)


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_user(user_id=None):
    ''' Deletes an individual user object '''
    obj = storage.get(User, user_id)
    if obj is None:
        ''' If no state object with that id exists aborts '''
        abort(404)

    storage.delete(obj)
    storage.save()
    return jsonify({}), 200


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id=None):
    ''' Updates an individual user object '''
    obj = storage.get(User, user_id)
    if obj is None:
        ''' If no state object with that id '''
        abort(404)
    args = request.get_json()
    if args is None:
        return jsonify({"error": "Not a JSON"}), 400
    for k, v in args.items():
        if k not in ["id", "email", "updated_at", "created_at"]:
            setattr(obj, k, v)
    storage.save()
    return jsonify(obj.to_dict()), 200


@app_views.route("/users/", methods=["POST"], strict_slashes=False)
def create_user():
    ''' Creates an user object if it doesn't exists yet '''
    args = request.get_json()
    if args is None:
        return jsonify({"error": "Not a JSON"}), 400
    elif 'email' not in args:
        return jsonify({"error": "Missing email"}), 400
    elif 'password' not in args:
        return jsonify({"error": "Missing password"}), 400
    obj = User(**args)
    storage.new(obj)
    storage.save()
    return jsonify(obj.to_dict()), 201
