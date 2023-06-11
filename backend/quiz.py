from typing import Dict, Optional, Union

from database import Database


class Quiz:
    def __init__(self, db: Database, level: str):
        self.db = db
        self.quizzes = self.db.get_quizzes(level)

    def refresh_quizzes(self, level: str) -> None:
        self.quizzes = self.db.get_quizzes(level)

    def get_quiz(self, index: int) -> Optional[Dict[str, Union[str, int]]]:
        if 0 <= index < len(self.quizzes):
            return self.quizzes[index]
        else:
            return None

    def get_total_quizzes(self) -> int:
        return len(self.quizzes)

    def check_answers(self, user_answers: Dict[int, str]) -> int:
        # Check each answer and count how many are correct
        correct_count = 0
        for index, user_answer in user_answers.items():
            if 0 <= index < len(self.quizzes):
                correct_answer = self.quizzes[index]['answer']
                if user_answer == correct_answer:
                    correct_count += 1
        return correct_count
