def classify_esg_risk(esg_score: int) -> str:
    """
    Classifies the ESG risk level based on the score.
    """
    if esg_score >= 90:
        return "Leader (AAA)"
    elif esg_score >= 75:
        return "Strong (AA)"
    elif esg_score >= 60:
        return "Average (A)"
    else:
        return "Under Watch (B)"


def get_trend_indicator(current_score: int, previous_score: int = None) -> str:
    """
    Provides a visual trend indicator for sustainability performance.
    """
    if previous_score is None:
        return "Stable"
    if current_score > previous_score:
        return "Improving 📈"
    elif current_score < previous_score:
        return "Declining 📉"
    else:
        return "Stable ➡️"
