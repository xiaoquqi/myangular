from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_security import SQLAlchemyUserDatastore, Security

app = Flask(__name__, static_url_path='')
app.config.from_object('config')
db = SQLAlchemy(app)


# For Flask-Security Token based validation
from ruler.database.models import User, Role
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


from ruler.routes import index

# Initial user create method
#@app.before_first_request
#def create_user():
#    db.create_all()
#    if not User.query.first():
#        user_datastore.create_user(email='test@example.com', password='test123')
#        db.session.commit()
