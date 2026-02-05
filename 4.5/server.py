from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import bcrypt

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super_secret_jwt_key'
jwt = JWTManager(app)

users_db = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users_db:
        return jsonify({"msg": "Користувач вже існує"}), 400

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    users_db[username] = {
        'username': username,
        'password': hashed_password
    }

    return jsonify({"msg": "Користувача зареєстровано"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = users_db.get(username)

    if not user or not bcrypt.checkpw(password.encode('utf-8'), user['password']):
        return jsonify({"msg": "Невірний логін або пароль"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

@app.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    current_user = get_jwt_identity()
    return jsonify({
        "msg": "Доступ дозволено",
        "user": current_user,
        "secret_data": "Це закрита інформація тільки для авторизованих"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
