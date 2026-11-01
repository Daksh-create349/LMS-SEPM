"""LMS Circulation & Loan Policy Service."""

class CirculationService:
    STANDARD_LOAN_DAYS = 14
    DAILY_OVERDUE_FINE = 5.0  # Rs. 5 per day

    @staticmethod
    def calculate_overdue_fine(overdue_days: int) -> float:
        if overdue_days <= 0:
            return 0.0
        return float(overdue_days * CirculationService.DAILY_OVERDUE_FINE)
