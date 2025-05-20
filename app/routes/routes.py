from flask import Blueprint
from app.controllers.grammar_controller import check_grammar, render_suggestion
from app.controllers.palagrism_controller import check_plagrism


grammar_routes = Blueprint("grammar_routes", __name__)
grammar_routes.route('/check-grammar', methods=['POST'])(check_grammar)
grammar_routes.route('/render-suggestion', methods=['POST'])(render_suggestion)
grammar_routes.route('/check-plagrism', methods=['POST'])(check_plagrism)
