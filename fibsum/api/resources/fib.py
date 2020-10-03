from flask_restful import Resource
from fibsum.services.fibsum import all_comb_sum


class FibSumGenerator(Resource):
    """
    Sum Fibonacci series endpoint:

    ---
    get:
      tags:
        - api
      parameters:
        - in: path
          name: target
          schema:
            type: integer
      responses:
        200:
          content:
            application/json:
              schema:
                type: list
    """

    def get(self, target):
        return all_comb_sum(target)
