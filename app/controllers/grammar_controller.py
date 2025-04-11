from flask import request, jsonify
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
     
     
    