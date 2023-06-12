import json
from pathlib import Path
from typing import Dict, List, Any


class Database:
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.data = None

    def load_data(self) -> None:
        """
        Load data from a JSON file at the specified path.

        :raises FileNotFoundError: If the file is not found at the specified path.
        :raises json.JSONDecodeError: If the file at the specified path is not a valid JSON file.
        """
        try:
            with open(self.db_path.resolve(), 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            print(f"File not found at {self.db_path}")
        except json.JSONDecodeError:
            print(f"File at {self.db_path} is not a valid JSON file")

    def get_quizzes(self, level: str) -> List[Dict[str, Any]]:
        if not self.data and self.data is not None:
            self.load_data()
            return self.data.get(level, [])
        else:
            raise ValueError(f"No quizzes found for level '{level}'")
