# from flask import Flask, jsonify, request, render_template
# import json
# from pathlib import Path

# # Get the directory where this file is located
# BASE_DIR = Path(__file__).resolve().parent

# FRONTEND_DIR = (BASE_DIR / '..' / 'frontend').resolve()
# STATIC_DIR = (FRONTEND_DIR / 'static').resolve()
# TEMPLATES_DIR = (FRONTEND_DIR / 'templates').resolve()

# DATABASE_DIR = (BASE_DIR / '..' / 'database').resolve()

# app = Flask(__name__,
#             static_folder=STATIC_DIR,
#             template_folder=TEMPLATES_DIR)

# # Load quizzes from JSON file
# with open((DATABASE_DIR / 'quizzes.json').resolve()) as f:
#     quizzes = json.load(f)

# @app.route('/')
# def home():
#     return render_template('quiz.html')


# @app.route('/quiz/<int:index>', methods=['GET'])
# def get_quiz(index):
#     # Return the quiz at the given index
#     if 0 <= index < len(quizzes):
#         return jsonify(quizzes[index])
#     else:
#         return "Invalid quiz index.", 404


# @app.route('/quiz/total', methods=['GET'])
# def get_total_quizzes():
#     # Return the total number of quizzes
#     return jsonify({'total': len(quizzes)})


# @app.route('/quiz', methods=['POST'])
# def check_answers():
#     # Assume the request data is a dictionary where keys are quiz indices
#     # and values are the user's answers
#     user_answers = request.json

#     # Check each answer and count how many are correct
#     correct_count = 0
#     for index, user_answer in user_answers.items():
#         if 0 <= index < len(quizzes):
#             correct_answer = quizzes[index]['answer']
#             if user_answer == correct_answer:
#                 correct_count += 1

#     # Return the number of correct answers
#     return jsonify({'correct_count': correct_count})


# @app.route('/quiz/check_answers', methods=['POST'])
# def check_all_answers():
#     # Assume the request data is a dictionary where keys are quiz indices
#     # and values are the user's answers
#     user_answers = request.json

#     # Check each answer and count how many are correct
#     correct_count = 0
#     for index_str, user_answer in user_answers.items():
#         index = int(index_str)
#         if 0 <= index < len(quizzes):
#             correct_answer = quizzes[index]['answer']
#             if user_answer == correct_answer:
#                 correct_count += 1

#     # Return the number of correct answers
#     return jsonify({'correct_count': correct_count})


# if __name__ == '__main__':
#     app.run(debug=True)
