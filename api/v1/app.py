#!/usr/bin/python3
"""
Flask App that integrates with AirBnB static HTML Template
"""

from api.v1.views import app_views
from models import storage

# Variable instance of flask named app
app = Flask(__name__)

# Flask server enviromental variables setup
host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = os.getenv('HBNB_API_PORT', 5000)

# Blueprint app_views register. (Defined in api.v1.views)
app.register_blueprint(app_views)


# Flask page rendering
@app.teardown_appcontext
def teardown_db(exception):
    """
    after each request, this method calls .close() on
    the current SQLAlchemy Session
    """
    storage.close()

if __name__ == "__main__":
    """
    MAIN Flask App
    """
    # start Flask app
    app.run(host=host, port=port)
