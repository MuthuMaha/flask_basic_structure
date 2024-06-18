from flask import Flask
from .models import db
from flask_migrate import Migrate
from .blueprints.main.controllers import main_bp
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://@localhost/tr8_test?driver=ODBC+Driver+17+for+SQL+Server'

migrate = Migrate(app, db)
db.init_app(app)
#register the blueprint
app.register_blueprint(main_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

