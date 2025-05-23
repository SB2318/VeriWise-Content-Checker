## Here as per my application requirement, I will check the image by using their url

from flask import request, Response, jsonify
from app.services.copyright_check_service import CopyrightCheckerService

def copyright_check():
    
    data = request.get_json()

    if not data or 'image_url' not in data:
        return jsonify({'error': 'Missing image url'}), 400
    url = data['image_url']
    # Call grammer service to handle the rest
    try:
     corrected = CopyrightCheckerService().detect_copyrighted_text(url)
     return jsonify({'data': corrected}), 200

    except Exception as e:
     return jsonify({'error': str(e)}), 500


