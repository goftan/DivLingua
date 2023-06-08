# file: database.py

from typing import List, Dict, Union, Any
from pathlib import Path
import json

class Database:
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.data = None

    def load_data(self) -> None:
        try:
            with open(self.db_path.resolve(), 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            print(f"File not found at {self.db_path}")
        except json.JSONDecodeError:
            print(f"File at {self.db_path} is not a valid JSON file")
    
    def get_quizzes(self, level: str) -> Dict[str, Any]:
        if not self.data:
            self.load_data()
        return self.data.get(level, [])
