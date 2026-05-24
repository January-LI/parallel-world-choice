
import json
import os
from datetime import datetime

import numpy as np

from fortune_data import fortunes, fortune_weights, lucky_colors, lucky_numbers


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
    """Manage mystery boxes fate assist feature."""

    def __init__(self):
        self.lucky_colors = lucky_colors
        self.fate_messages = [
            "Parallel paths open where your intuition points.",
            "A hidden signal says this is your moment.",
            "Your timeline favors bold but joyful choices.",
            "Destiny echoes softly: trust this direction.",
            "The parallel worlds align around this option.",
            "An unexpected blessing follows this selection.",
            "Your energy and this choice are in sync today.",
        ]
        # Multi-dimensional lists for beginner-friendly keyword resonance rules.
        self.keyword_groups = [
            ["secret", "limited", "edition", "rare", "exclusive"],
            ["pink", "gold", "silver", "emerald", "azure", "crimson", "ivory", "black"],
            ["special", "premium", "collector", "set", "box"],
            ["cute", "dream", "magic", "lucky", "star"],
        ]

    def _calc_weight_for_choice(self, choice_text, lucky_color):
        """Return weighted score and resonance tags for one choice."""
        weight = 1.0
        tags = []
        lower_text = choice_text.lower()

        # Lucky color matching
        if lucky_color.lower() in lower_text:
            weight += 1.3
            tags.append("lucky color match")

        # Keyword resonance from multi-dimensional list
        for group in self.keyword_groups:
            for word in group:
                if word in lower_text:
                    weight += 0.35
                    tags.append("keyword resonance")
                    break

        # Small random shake for ritual-like unpredictability
        weight += float(np.random.uniform(0.0, 0.5))
        return weight, tags

    def analyze_choices(self, choices):
        """Analyze input choices and recommend one option by weighted randomness."""
        lucky_color = str(np.random.choice(self.lucky_colors))
        weights = []
        tag_rows = []

        for text in choices:
            w, tags = self._calc_weight_for_choice(text, lucky_color)
            weights.append(w)
            tag_rows.append(tags)

        weights_array = np.array(weights, dtype=float)
        probs = weights_array / weights_array.sum()
        selected_index = int(np.random.choice(len(choices), p=probs))
        recommended = choices[selected_index]

        # Parallel energy by selected probability
        selected_prob = float(probs[selected_index])
        if selected_prob >= 0.45:
            energy = "HIGH"
        elif selected_prob >= 0.30:
            energy = "MEDIUM"
        else:
            energy = "RISING"

        message = str(np.random.choice(self.fate_messages))
        selected_tags = tag_rows[selected_index]
        resonance = " / ".join(selected_tags) if selected_tags else "random destiny pulse"

        return {
            "system": "Mystery Boxes Fate Assist System",
            "input_choices": choices,
            "recommended_choice": recommended,
            "lucky_color": lucky_color,
            "parallel_energy": energy,
            "resonance": resonance,
            "fate_message": message,
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
        # Keep compatibility with old records while supporting new mystery-boxes format.
        record = {"time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

        if "input_choices" in result and "recommended_choice" in result:
            record["system"] = result.get("system", "Mystery Boxes Fate Assist System")
            record["input_choices"] = result["input_choices"]
            record["recommended_choice"] = result["recommended_choice"]
            record["lucky_color"] = result.get("lucky_color", "")
            record["parallel_energy"] = result.get("parallel_energy", "")
            record["resonance"] = result.get("resonance", "")
            record["fate_message"] = result.get("fate_message", "")
        else:
            record["question"] = result.get("question", "")
            record["fate_answer"] = result.get("fate_answer", "")

        data["fate_history"].append(record)
        self._write_json(data)

    def get_history(self):
        """Return all saved history."""
        return self._read_json()
