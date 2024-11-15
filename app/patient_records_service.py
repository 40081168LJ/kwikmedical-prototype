# - IMPORTS START ---------------------------------------------------------------------------------------------------- #
from flask import Blueprint, jsonify
import sqlite3

from flask_jwt_extended import jwt_required
# - IMPORTS END ------------------------------------------------------------------------------------------------------ #

# - BLUEPRINT START -------------------------------------------------------------------------------------------------- #
# Define the Blueprint
patient_records_bp = Blueprint('patient_records', __name__)

@patient_records_bp.route('/patient/<int:patient_id>', methods=['GET'])
@jwt_required()  # Secures the endpoint
def get_patient_info(patient_id):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('../db/patients.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM patients WHERE id = ?", (patient_id,))
        patient = cursor.fetchone()
        conn.close()

        if patient:
            # Return patient information as JSON
            return jsonify({
                'id': patient[0],
                'name': patient[1],
                'nhs_number': patient[2],
                'medical_history': patient[3]
            }), 200
        else:
            # Return a 404 error if the patient is not found
            return jsonify({'error': 'Patient not found'}), 404

    except Exception as e:
        # Return a 500 error for unexpected issues
        return jsonify({'error': 'An internal server error occurred', 'details': str(e)}), 500
# - BLUEPRINT END ---------------------------------------------------------------------------------------------------- #