# - IMPORTS START ---------------------------------------------------------------------------------------------------- #
from flask import Blueprint, request, jsonify
# - IMPORTS END ------------------------------------------------------------------------------------------------------ #

# - BLUEPRINT START -------------------------------------------------------------------------------------------------- #
# Define the Blueprint
ambulance_dispatch_bp = Blueprint('ambulance_dispatch', __name__)

@ambulance_dispatch_bp.route('/dispatch-ambulance', methods=['POST'])
def dispatch_ambulance():
    dispatch_data = request.json
    return jsonify({
        'status': 'Success',
        'message': f"Ambulance dispatched to {dispatch_data['location']} for {dispatch_data['name']}"
    }), 200
# - BLUEPRINT END ---------------------------------------------------------------------------------------------------- #