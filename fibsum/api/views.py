from flask import Blueprint
from flask_restful import Api
from fibsum.api.resources import FibSumGenerator

blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(blueprint)

api.add_resource(FibSumGenerator, "/fibsum/<int:target>", endpoint="fibsum-generator")
