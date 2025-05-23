## Here as per my application requirement, I will check the image by using their url

# from flask import request, Response, jsonify
from app.services.copyright_check_service import CopyrightCheckerService
from fastapi import  Request
from fastapi.responses import JSONResponse

async def copyright_check(request:Request):
    
    # data = request.get_json()
    data = await request.json()

    if not data or 'image_url' not in data:
        #return jsonify({'error': 'Missing image url'}), 400
        return JSONResponse(content={'error': 'Missing image url'}, status_code=400)
    url = data['image_url']
    # Call grammer service to handle the rest
    try:
     corrected = CopyrightCheckerService().detect_copyrighted_text(url)
     # return jsonify({'data': corrected}), 200
     return JSONResponse(content={'data': corrected}, status_code=200, media_type="application/json")

    except Exception as e:
     # return jsonify({'error': str(e)}), 500
     return JSONResponse(content={'error': str(e)}, status_code=500, media_type="application/json")


