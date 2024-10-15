from flask import Blueprint, jsonify
import sqlite3

# Define the Blueprint
patient_records_bp = Blueprint('patient_records', __name__)

@patient_records_bp.route('/patient/<int:patient_id>', methods=['GET'])
def get_patient_info(patient_id):
    conn = sqlite3.connect('../db/patients.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients WHERE id = ?", (patient_id,))
    patient = cursor.fetchone()
    conn.close()

    if patient:
        return jsonify({
            'id': patient[0],
            'name': patient[1],
            'nhs_number': patient[2],
            'medical_history': patient[3]
        }), 200
    else:
        return jsonify({'error': 'Patient not found'}), 404
