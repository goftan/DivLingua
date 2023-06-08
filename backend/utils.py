# file: utils.py

from typing import List, Dict, Union
from pathlib import Path
import json

def load_quizzes(quiz_file: Path) -> Union[List[Dict[str, Union[str, int]]], None]:
    try:
        with open(quiz_file.resolve(), 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File not found at {quiz_file}")
    except json.JSONDecodeError:
        print(f"File at {quiz_file} is not a valid JSON file")
    return None
