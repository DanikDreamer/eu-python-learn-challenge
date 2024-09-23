from flask import Flask
from flask import request, jsonify


class FlaskExercise:
    users = {}

    @staticmethod
    def configure_routes(app: Flask) -> None:
        @app.post("/user")
        def create_user():
            data = request.get_json()

            if "name" not in data:
                return jsonify({"errors": {"name": "This field is required"}}), 422

            user_name = data["name"]
            FlaskExercise.users[user_name] = data
            return jsonify({"data": f"User {user_name} is created!"}), 201

        @app.get("/user/<name>")
        def get_user(name):
            user = FlaskExercise.users.get(name)
            if user:
                return jsonify({"data": f"My name is {user['name']}"}), 200

            return "", 404

        @app.patch("/user/<name>")
        def update_user(name):
            user = FlaskExercise.users.get(name)
            if not user:
                return "", 404

            data = request.get_json()
            new_name = data["name"]
            return jsonify({"data": f"My name is {new_name}"}), 200

        @app.delete("/user/<name>")
        def delete_user(name):
            user = FlaskExercise.users.get(name)
            if not user:
                return "", 404

            FlaskExercise.users.pop(name)
            return "", 204
