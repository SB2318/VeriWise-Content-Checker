# from flask import request, Response, jsonify
from app.services.grammar_service import GrammarService
from fastapi import  Request
from fastapi.responses import JSONResponse, HTMLResponse

async def check_grammar(request: Request):
    # This function checks the grammar of a sentence
    # It will take HTML Text as an input, and convert it to plain text
    # Then it will use the language tool to check the grammar of the text
    # data = request.get_json()
    data = await request.json()

    if not data or 'text' not in data:
        # return jsonify({'error': 'Missing text'}), 400
        return JSONResponse(content={'error': 'Missing text'}, status_code=400)
    text = data['text']
    # Call grammer service to handle the rest
    try:
     corrected = GrammarService().parse_text(text)
     # return jsonify({'corrected': corrected}), 200
     return JSONResponse(content={'corrected': corrected}, status_code=200)

    except Exception as e:
     # return jsonify({'error': str(e)}), 500
     return JSONResponse(content={'error': str(e)}, status_code=500)


async def render_suggestion(request:Request):

    #data = request.get_json()
    data = await request.json()

    if not data or 'text' not in data:
        #return jsonify({'error': 'Missing text'}), 400
        return JSONResponse(content={'error': 'Missing text'}, status_code=400)
    text = data['text']
    # Call grammer service to handle the rest
    try:
     corrected = GrammarService().render_grammar_suggestion(text)
     html_content = corrected['suggestions']
     original_content = corrected['original']
     full_html = f"""
        <html lang="en">
        <head>
            <meta charset="utf-8" />
            <title>Grammar Suggestions</title>
        </head>
        <body>
            <h1>Grammar Suggestions (Highlighted)</h1>
            <div>
                <h3>With Suggestions:</h3>
                {html_content}
            </div>
            <hr />
            <div>
                <h3>Original Content:</h3>
                <pre style="white-space: pre-wrap;">{original_content}</pre>
            </div>
        </body>
        </html>
        """
     return HTMLResponse(content= full_html, status_code=200)

    except Exception as e:
     #return jsonify({'error-h': str(e)}), 500
     return JSONResponse(content={'error': str(e)}, status_code=500)
     
     
    