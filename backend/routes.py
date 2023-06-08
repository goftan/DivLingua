# file: routes.py

from typing import Dict, Union
from flask import Blueprint, jsonify, request, render_template
from quiz import Quiz
from pathlib import Path
from database import Database

quiz_bp = Blueprint('quiz', __name__)

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_DIR = BASE_DIR / 'database'

# You can select the category here.
LEVEL = "A1"

db = Database((DATABASE_DIR / 'quizzes.json').resolve())
quiz_obj = Quiz(db, LEVEL)

@quiz_bp.route('/')
def home():
    return render_template('quiz.html')

@quiz_bp.route('/quiz/<int:index>', methods=['GET'])
def get_quiz(index: int):
    quiz = quiz_obj.get_quiz(index)
    return jsonify(quiz) if quiz else ("Invalid quiz index.", 404)

@quiz_bp.route('/quiz/total', methods=['GET'])
def get_total_quizzes():
    return jsonify({'total': quiz_obj.get_total_quizzes()})

@quiz_bp.route('/quiz', methods=['POST'])
def check_answers():
    user_answers = request.json
    return jsonify({'correct_count': quiz_obj.check_answers(user_answers)})

@quiz_bp.route('/quiz/check_answers', methods=['POST'])
def check_all_answers():
    user_answers = {int(k): v for k, v in request.json.items()}
    return jsonify({'correct_count': quiz_obj.check_answers(user_answers)})
