from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Олексій", "role": "admin"},
    {"id": 2, "name": "Марія", "role": "user"}
]


def find_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({
        "status": "success",
        "data": users,
        "message": "Список користувачів отримано"
    })


@app.route('/users', methods=['POST'])
def create_user():
    request_data = request.get_json()

    if not request_data or 'name' not in request_data:
        return jsonify({
            "status": "error",
            "data": None,
            "message": "Не вказано ім'я користувача"
        }), 400

    new_id = users[-1]["id"] + 1 if users else 1
    new_user = {
        "id": new_id,
        "name": request_data["name"],
        "role": request_data.get("role", "user")
    }

    users.append(new_user)

    return jsonify({
        "status": "success",
        "data": new_user,
        "message": "Користувача створено"
    }), 201


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = find_user(user_id)
    if user:
        return jsonify({
            "status": "success",
            "data": user,
            "message": "Користувача знайдено"
        })
    else:
        return jsonify({
            "status": "error",
            "data": None,
            "message": "Користувача не знайдено"
        }), 404


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = find_user(user_id)
    if not user:
        return jsonify({
            "status": "error",
            "data": None,
            "message": "Користувача не знайдено"
        }), 404

    request_data = request.get_json()
    user["name"] = request_data.get("name", user["name"])
    user["role"] = request_data.get("role", user["role"])

    return jsonify({
        "status": "success",
        "data": user,
        "message": "Дані оновлено"
    })


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = find_user(user_id)
    if not user:
        return jsonify({
            "status": "error",
            "data": None,
            "message": "Користувача не знайдено"
        }), 404

    users.remove(user)
    return jsonify({
        "status": "success",
        "data": None,
        "message": "Користувача видалено"
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)
