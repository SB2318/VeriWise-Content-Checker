from flask import Blueprint
from app.controllers.grammar_controller import check_grammar

grammar_routes = Blueprint("grammar_routes", __name__)
grammar_routes.route('/check-grammar', methods=['POST'])(check_grammar)
