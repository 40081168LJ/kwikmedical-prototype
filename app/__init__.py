from flask import Flask, render_template
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)

    from .emergency_call_service import emergency_call_bp
    from .patient_records_service import patient_records_bp
    from .ambulance_dispatch_service import ambulance_dispatch_bp

    app.register_blueprint(emergency_call_bp)
    app.register_blueprint(patient_records_bp)
    app.register_blueprint(ambulance_dispatch_bp)

    # Add a route for the home page
    @app.route('/')
    def home():
        return render_template('index.html')  # Renders the index.html from the templates directory

    return app
