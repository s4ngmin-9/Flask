from flask import Flask
from flask_smorest import Api
from Flask_day_3.db import db
from Flask_day_3.models import User, Board

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:qwer9805@localhost/oz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# blueprint 설정
app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

from routes.board import board_blp
from routes.user import user_blp

api.register_blueprint(board_blp)
api.register_blueprint(user_blp)

from flask import render_template
@app.route('/manage-boards')
def manage_boards():
  return render_template('boards.html')

@app.route('/manage-users')
def manage_users():
  return render_template('users.html')

if __name__ == '__main__':
    with app.app_context():
      print("여기 실행?")
      db.create_all()
  
    app.run(debug=True)
