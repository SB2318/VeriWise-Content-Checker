from flask import request, Response, jsonify
from app.services.grammar_service import GrammarService

def check_grammar():
    # This function checks the grammar of a sentence
    # It will take HTML Text as an input, and convert it to plain text
    # Then it will use the language tool to check the grammar of the text
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({'error': 'Missing text'}), 400
    text = data['text']
    # Call grammer service to handle the rest
    try:
     corrected = GrammarService().parse_text(text)
     return jsonify({'corrected': corrected}), 200

    except Exception as e:
     return jsonify({'error': str(e)}), 500


def render_suggestion():

    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({'error': 'Missing text'}), 400
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
     return Response(full_html, mimetype='text/html')

    except Exception as e:
     return jsonify({'error-h': str(e)}), 500
     
     
    