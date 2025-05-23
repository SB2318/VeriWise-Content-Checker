# from flask import request, Response, jsonify
from app.services.plagiarism_service import PlagiarismService
from fastapi import  Request
from fastapi.responses import JSONResponse

async def check_plagiarism(request:Request):
    
    #data = request.get_json()
    data = await request.json()

    if not data or 'text' not in data:
       # return jsonify({'error': 'Missing text'}), 400
       return JSONResponse(content={'error': 'Missing text'}, status_code=400)

    text = data['text']
    # Call grammer service to handle the rest
    try:
     corrected = PlagiarismService().check_plagiarism(text)
     # return jsonify({'data': corrected}), 200
     return JSONResponse(content={'data': corrected}, status_code=200)

    except Exception as e:
     # return jsonify({'error': str(e)}), 500
     return JSONResponse(content={'error': str(e)}, status_code=500)



