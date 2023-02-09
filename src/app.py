from flask import Flask
from routes import routes
from database.models import db
import config

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)
print(app.config)

app.register_blueprint(routes)
with app.app_context():
    db.init_app(app)
    db.create_all()

if __name__ == "__main__":
    app.run()