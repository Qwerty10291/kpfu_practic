def middle_result(marks: dict[str, int], scholarship: float, factor: int = 1):
    avg_score = sum(marks.values()) / len(marks)
    if avg_score < 3.5:
        print("стипендия не оплачивается")
    elif avg_score > 4.5:
        return scholarship * (1.5 * factor)
    else:
        return scholarship * factor
