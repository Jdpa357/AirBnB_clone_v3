#!/usr/bin/python3
"""
handles all default RestFul API actions for review
"""
from api.v1.views import app_views
from models import storage
from flask import jsonify
from flask import request
from flask import abort
from models.review import Review
from models.place import Place
from models.user import User


@app_views.route('/places/<place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def get_reviews(place_id):
    """
    get all review by place id
    """
    list_objects = []

    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    places = place.reviews
    for place in places:
        list_objects.append(place.to_dict())
    return jsonify(list_objects)


@app_views.route('/reviews/<review_id>', methods=['GET'],
                 strict_slashes=False)
def get_reviews_by_id(review_id):
    """
    get review by id
    """
    reviews = storage.get(Review, review_id)
    if reviews is None:
        abort(404)

    return jsonify(reviews.to_dict())


@app_views.route('/reviews/<review_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_reviews(review_id):
    """
    delete review by id
    """
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)

    review.delete()
    storage.save()

    return jsonify({})


@app_views.route('/places/<place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def create_reviews(place_id):
    """
    create review by place id
    """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)

    json_data = request.get_json()
    if json_data is None:
        abort(400, "Not a JSON")

    if "user_id" not in json_data:
        abort(400, "Missing user_id")

    user = storage.get(User, json_data.get("user_id"))
    if user is None:
        abort(404)

    if "text" not in json_data:
        abort(400, "Missing text")

    json_data["place_id"] = place_id
    new_place = Place(**json_data)
    storage.new(new_place)
    storage.save()

    return (jsonify(new_place.to_dict()), 201)


@app_views.route('/reviews/<review_id>', methods=['PUT'],
                 strict_slashes=False)
def update_reviews(review_id):
    """
    Update review by id
    """
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)

    json_data = request.get_json()
    if json_data is None:
        abort(400, "Not a JSON")

    for key, value in json_data.items():
        if key not in ["id", "user_id", "place_id", "created_at",
                       "updated_at"]:
            setattr(review, key, value)
    review.save()
    return jsonify(review.to_dict())
