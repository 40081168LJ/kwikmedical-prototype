# - IMPORTS START ---------------------------------------------------------------------------------------------------- #
from flask import Flask, render_template
from flask_cors import CORS
from flask_jwt_extended import JWTManager

# Import the Blueprint objects from each service
from .emergency_call_service import emergency_call_bp
from .patient_records_service import patient_records_bp
from .ambulance_dispatch_service import ambulance_dispatch_bp
from .auth_service import auth_bp
# - IMPORTS END ------------------------------------------------------------------------------------------------------ #

# - APP CREATE START ------------------------------------------------------------------------------------------------- #
def create_app():
    app = Flask(__name__)
    CORS(app)

    # Set up JWT
    app.config["JWT_SECRET_KEY"] = "your_jwt_secret_key"  # Change this in production!
    jwt = JWTManager(app)

    # Register Blueprints
    app.register_blueprint(emergency_call_bp)
    app.register_blueprint(patient_records_bp)
    app.register_blueprint(ambulance_dispatch_bp)
    app.register_blueprint(auth_bp)

    # Add a route for the home page
    @app.route('/')
    def home():
        return render_template('index.html')  # Renders the index.html from the templates directory

    return app
print("App created.")
# - APP CREATE END --------------------------------------------------------------------------------------------------- #