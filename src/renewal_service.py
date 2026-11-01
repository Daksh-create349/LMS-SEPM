"""LMS Book Loan Renewal Service."""

class RenewalService:
    MAX_RENEWALS_PERMITTED = 2

    @staticmethod
    def is_eligible_for_renewal(current_renewals: int, has_active_hold: bool) -> bool:
        if has_active_hold:
            return False
        return current_renewals < RenewalService.MAX_RENEWALS_PERMITTED
