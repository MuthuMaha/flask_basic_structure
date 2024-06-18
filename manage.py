from flask import Flask
from flask_migrate import Migrate
from flask_script import Manager
from models import db
from models.item_model import Item
from models.user_model import User
from blueprints.main.controllers import main_bp

app=Flask(__name__)
# app.config.from_pyfile('config.app')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://@localhost/tr8_test?driver=ODBC+Driver+17+for+SQL+Server'

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(main_bp)

manager = Manager(app)
# manager.add_command('db', MigrateCommand)

if __name__ == '':
    manager.run()