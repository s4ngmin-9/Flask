from flask import request, jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from Flask_day_3.db import db
from Flask_day_3.models import User

user_blp = Blueprint("Users", "users", description="Opertaions on users", url_prefix='/user')

# API LIST:
# (1) 전체 유저 데이터 조회 (GET)
# (2) 유저 생성 (POST)

@user_blp.route('/')
class UserList(MethodView):
    def get(self):
        users = User.query.all()

        # for user in users:
        #     print(user.id)
        #     print(user.name)
        #     print(user.email)
        
        user_data = [
            {'id':user.id, 'name':user.name, 'email':user.email} for user in users
        ]
        return jsonify(user_data)
    
    def post(self):
        data = request.json
        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"msg":"Successfully created new user"}), 201
        
# (1) 특정 유저 데이터 조회 (GET)
# (2) 특정 유저 데이터 업데이트 (PUT)
# (3) 특정 유저 데이터 삭제 (DELETE)
@user_blp.route("/<int:user_id>")
class UserResource(MethodView):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return jsonify({'name':user.name, 'email':user.email})

    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        data = request.json
        
        user.name = data['name']
        user.email = data['email']

        db.session.commit()

        return jsonify({"msg": "Successfully updated user"})
    
    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()

        return jsonify({"msg": "Successfully delete user"})