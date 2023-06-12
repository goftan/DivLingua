from typing import Dict, Optional, Union, List

from flask import session

from database_reader import DatabaseReader


class Quiz:
    def __init__(self, db: DatabaseReader):
        self.db = db
        self.quizzes: List[Dict[str, Union[str, int]]] = []

    def get_quiz(self, index: int) -> Optional[Dict[str, Union[str, int]]]:
        level = session.get('level')
        if level is None or not isinstance(level, str):
            raise ValueError("Level must be a non-empty string")
        self.refresh_quizzes(level)
        if 0 <= index < len(self.quizzes):
            return self.quizzes[index]
        else:
            return None

    def refresh_quizzes(self, level: str) -> None:
        self.quizzes = self.db.get_quizzes(level)

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
