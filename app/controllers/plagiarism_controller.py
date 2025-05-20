from flask import request, Response, jsonify
from app.services.plagiarism_service import PlagiarismService

def check_plagiarism():
    
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({'error': 'Missing text'}), 400
    text = data['text']
    # Call grammer service to handle the rest
    try:
     corrected = PlagiarismService().check_plagiarism(text)
     return jsonify({'data': corrected}), 200

    except Exception as e:
     return jsonify({'error': str(e)}), 500


