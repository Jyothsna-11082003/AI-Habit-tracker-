def get_suggestions(water, sleep, screen):
    suggestions = []
    if water < 2.0:
        suggestions.append("💧 Increase water intake to at least 2L.")
    if sleep < 7:
        suggestions.append("🛌 Try getting at least 7 hours of sleep.")
    if screen > 5:
        suggestions.append("📵 Reduce screen time for better health.")
    if not suggestions:
        suggestions.append("✅ Great job! Keep up the good habits!")
    return suggestions
