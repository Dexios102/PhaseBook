from flask import Blueprint, request
from .data.search_data import USERS

bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    results = []
    if "id" in args:
        results += [user for user in USERS if user["id"] == args["id"]]

    if "name" in args:
        results += [
            user for user in USERS if args["name"].lower() in user["name"].lower()
        ]

    if "age" in args:
        results += [
            user
            for user in USERS
            if int(args["age"]) - 1 <= user["age"] <= int(args["age"]) + 1
        ]

    if "occupation" in args:
        results += [
            user
            for user in USERS
            if args["occupation"].lower() in user["occupation"].lower()
        ]
    results = list({v["id"]: v for v in results}.values())

    return results
