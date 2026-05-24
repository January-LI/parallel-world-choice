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
