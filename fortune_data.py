fortunes = [
    ["Supreme Luck", "Clouds part, your wish draws near."],
    ["Great Luck", "Stars align, a helper approaches."],
    ["Moderate Luck", "Wait with patience, your season comes."],
    ["Small Luck", "Steady steps lead to brighter ground."],
    ["Low Luck", "Move gently today, sharpen your heart."],
]

# Probability weights for numpy.random.choice(..., p=fortune_weights)
# Order must match fortunes list:
# Supreme 10%, Great 20%, Moderate 40%, Small 20%, Low 10%
fortune_weights = [0.10, 0.20, 0.40, 0.20, 0.10]

# Decision fate answer pool
fate_answers = [
    "YES",
    "NO",
    "Worth a try",
    "Not the right time",
    "Destiny says wait",
    "Follow your heart",
    "Prepare first, then act",
    "Ask again at dawn",
    "The signs point to success",
    "A hidden opportunity is near",
    "Your timing feels fortunate",
    "The parallel worlds agree",
    "Luck favors bold choices",
    "A small risk may bring reward",
    "Destiny remains uncertain",
    "Patience will reveal the answer",
    "The stars are not aligned yet",
    "A better path may appear soon",
    "Trust your first instinct",
    "Today is not ideal for action",
    "The future feels promising",
    "An unexpected outcome awaits",
    "Your energy attracts good fortune",
    "The omen is positive",
    "The omen is unclear",
    "Fortune whispers yes",
    "Fortune whispers no",
    "Proceed with caution",
    "Your luck is increasing",
    "The universe suggests balance",
    "A rare chance is approaching",
    "Fate encourages exploration",
    "A calm mind will guide you",
    "The answer may already be within you",
]

# Lucky color pool
lucky_colors = [
    "Gold",
    "Crimson",
    "Emerald",
    "Azure",
    "Silver",
    "Ivory",
    "Black",
]

# Lucky number pool
lucky_numbers = [1, 3, 5, 6, 7, 8, 9]