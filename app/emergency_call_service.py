# - IMPORTS START ---------------------------------------------------------------------------------------------------- #
from flask import Blueprint, request, jsonify
import requests
# - IMPORTS END ------------------------------------------------------------------------------------------------------ #

# - BLUEPRINT START -------------------------------------------------------------------------------------------------- #
# Define the Blueprint
emergency_call_bp = Blueprint('emergency_call', __name__)

@emergency_call_bp.route('/emergency-call', methods=['POST'])
def handle_emergency_call():
    call_data = request.json
    patient_id = call_data.get('patient_id')

    # Query the Patient Records Service for patient info
    patient_info_response = requests.get(f'http://localhost:5000/patient/{patient_id}')
    if patient_info_response.status_code == 200:
        patient_info = patient_info_response.json()
        dispatch_data = {
            'patient_id': patient_id,
            'name': patient_info['name'],
            'condition': call_data.get('condition'),
            'location': call_data.get('location')
        }
        dispatch_response = requests.post('http://localhost:8000/dispatch-ambulance', json=dispatch_data)

        if dispatch_response.status_code == 200:
            return jsonify({'message': 'Ambulance dispatched successfully!', 'dispatch_details': dispatch_response.json()}), 200
        else:
            return jsonify({'error': 'Failed to dispatch ambulance'}), 500
    else:
        return jsonify({'error': 'Patient not found'}), 404
# - BLUEPRINT END ---------------------------------------------------------------------------------------------------- #