# payment.py
from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime, timedelta

@dataclass
class PaymentRecord:
    policy_id: str
    product_code: str
    amount: float
    paid_at: datetime
    due_date: datetime
    penalty_applied: float = 0.0

class PaymentProcessor:
    """
    Simple in-memory payment processor.
    - process_payment: records a payment, computes any penalty
    - upcoming_reminders: returns accounts due within a window
    - overdue_with_penalties: returns overdue accounts with dynamic penalties
    """
    def __init__(self) -> None:
        self._payments: List[PaymentRecord] = []

    def process_payment(
        self,
        *,
        policy_id: str,
        product_code: str,
        amount: float,
        due_date: datetime,
        paid_at: Optional[datetime] = None,
        penalty_policy: str = "flat"  # "flat" or "percent"
    ) -> PaymentRecord:
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        paid_at = paid_at or datetime.utcnow()
        penalty = self._compute_penalty(due_date=due_date, paid_at=paid_at, amount=amount, policy=penalty_policy)

        rec = PaymentRecord(
            policy_id=policy_id,
            product_code=product_code,
            amount=amount,
            paid_at=paid_at,
            due_date=due_date,
            penalty_applied=penalty
        )
        self._payments.append(rec)
        return rec

    def upcoming_reminders(self, *, horizon_days: int = 7) -> List[PaymentRecord]:
        """Find payments with due dates in the next `horizon_days` that are not yet paid.
        In this simplified model, a 'reminder' is generated for any due date in the window
        without a matching paid_at before due_date.
        """
        now = datetime.utcnow()
        horizon = now + timedelta(days=horizon_days)
        # In a real system you'd check an accounts table; here we approximate with due dates
        return [
            p for p in self._payments
            if now <= p.due_date <= horizon and p.paid_at > p.due_date  # paid late -> still remind others
        ]

    def overdue_with_penalties(self) -> List[PaymentRecord]:
        now = datetime.utcnow()
        return [p for p in self._payments if p.paid_at > p.due_date and p.penalty_applied > 0]

    # --- defining penalty preferences---
    def _compute_penalty(self, *, due_date: datetime, paid_at: datetime, amount: float, policy: str) -> float:
        """Return penalty based on lateness; policy customizable to  preference."""
        if paid_at <= due_date:
            return 0.0
        days_late = (paid_at.date() - due_date.date()).days or 1

        if policy == "flat":
            # Flat ₦ amount per late day (edit this to your taste)
            per_day = 500.0 #I chose a flat ₦500 daily late fee to keep it simple and predictable.
            return per_day * days_late
        elif policy == "percent":
            # % of amount per late day, capped to avoid runaway penalties
            daily_rate = 0.005  # 0.5% per day late
            cap = 0.15        # 15% cap
            penalty = min(amount * daily_rate * days_late, amount * cap)
            return round(penalty, 2)
        else:
            raise ValueError("Unknown penalty policy. Use 'flat' or 'percent'.")
