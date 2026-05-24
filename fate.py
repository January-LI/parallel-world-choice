
import json
import os
from datetime import datetime

import numpy as np

from fortune_data import fortunes, fortune_weights, fate_answers, lucky_colors, lucky_numbers


class FortuneSystem:
    """Manage daily fortune feature."""

    def __init__(self):
        self.fortunes = fortunes
        self.fortune_weights = fortune_weights
        self.lucky_colors = lucky_colors
        self.lucky_numbers = lucky_numbers

    def draw_daily_fortune(self):
        """Draw one daily fortune using NumPy weighted choice."""
        index = int(np.random.choice(len(self.fortunes), p=self.fortune_weights))
        level, message = self.fortunes[index]

        lucky_number = int(np.random.choice(self.lucky_numbers))
        lucky_color = str(np.random.choice(self.lucky_colors))

        return {
            "fortune_level": level,
            "fortune_message": message,
            "lucky_number": lucky_number,
            "lucky_color": lucky_color,
        }


class FateSystem:
    """Manage decision fate feature."""

    def __init__(self):
        self.answers = fate_answers

    def ask(self, question):
        """Return a random fate answer for any question string."""
        answer = str(np.random.choice(self.answers))
        return {
            "question": question,
            "fate_answer": answer,
        }


class HistorySystem:
    """Store fortune and fate history into save.json."""

    def __init__(self, save_file="save.json"):
        self.save_file = save_file
        self._ensure_save_file()

    def _ensure_save_file(self):
        if not os.path.exists(self.save_file):
            self._write_json({"fortune_history": [], "fate_history": []})

    def _read_json(self):
        try:
            with open(self.save_file, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            data = {"fortune_history": [], "fate_history": []}
            self._write_json(data)
            return data

        if "fortune_history" not in data:
            data["fortune_history"] = []
        if "fate_history" not in data:
            data["fate_history"] = []
        return data

    def _write_json(self, data):
        with open(self.save_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def save_fortune(self, result):
        data = self._read_json()
        data["fortune_history"].append(
            {
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "fortune_level": result["fortune_level"],
                "fortune_message": result["fortune_message"],
                "lucky_number": result["lucky_number"],
                "lucky_color": result["lucky_color"],
            }
        )
        self._write_json(data)

    def save_fate(self, result):
        data = self._read_json()
        data["fate_history"].append(
            {
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "question": result["question"],
                "fate_answer": result["fate_answer"],
            }
        )
        self._write_json(data)

    def get_history(self):
        """Return all saved history."""
        return self._read_json()
