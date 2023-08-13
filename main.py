from exceptions import DuplicateValue, ValueNotFound
from cars import Cars
from http import HTTPStatus
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint
import json


from logger import create_log

app = Flask(__name__)
api = Api(app)

cars = Cars()

log = create_log("Cars_logger", "app.log")


class AllCarsGet(Resource):
    def get(self):
        log.info(f"Getting all cars")
        return cars.get_cars(), HTTPStatus.OK


class CarGet_Delete(Resource):
    def get(self, car_id):
        log.info(f"Getting car {car_id}")
        try:
            return cars.get_car(car_id), HTTPStatus.OK
        except ValueNotFound:
            log.error(f"Car {car_id} not found")
            return {"error": "Car not found"}, 400

    def delete(self, car_id):
        log.info(f"Deleting car {car_id}")
        try:
            return cars.delete_car(car_id), HTTPStatus.OK
        except ValueNotFound:
            log.error(f"Car {car_id} not found")
            return {"error": "Car not found"}, HTTPStatus.BAD_REQUEST


class CarAdd_Update(Resource):
    def post(self):
        car = request.get_json()
        log.info(f"Adding car {car}")
        try:
            return cars.add_car(car), HTTPStatus.CREATED
        except DuplicateValue:
            log.error(f"Car {car} allready exists")
            return {"error": "Duplicate car"}, HTTPStatus.BAD_REQUEST

    def put(self):
        car = request.get_json()
        log.info(f"Updating car {car}")
        try:
            return cars.update_car(car), HTTPStatus.OK
        except ValueNotFound:
            log.error(f"Car {car} not found")
            return {"error": "Car not found"}, HTTPStatus.BAD_REQUEST


api.add_resource(AllCarsGet, "/cars")
api.add_resource(CarGet_Delete, "/car/<int:car_id>")
api.add_resource(CarAdd_Update, "/car")
# api.add_resource(Get_Swagger, "/swagger")


# Swagger documentation route
@app.route("/swagger.json")
def swagger():
    with open("swagger.json", "r") as f:
        return jsonify(json.load(f))


# Swagger UI route
SWAGGER_URL = "/swagger-ui"
API_URL = "/swagger.json"
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Cars API"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


if __name__ == "__main__":
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
