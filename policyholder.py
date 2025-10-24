# policyholder.py
from dataclasses import dataclass, field
from typing import Dict, Optional
from datetime import datetime

@dataclass
class Policyholder:
    policy_id: str
    full_name: str
    email: str
    status: str = "REGISTERED"  # REGISTERED | SUSPENDED | CANCELLED
    products: Dict[str, datetime] = field(default_factory=dict)  # product_code -> start_date

    def register_for_product(self, product_code: str, start_date: Optional[datetime] = None) -> None:
        """Assign a product to the policyholder."""
        if self.status != "REGISTERED":
            raise PermissionError("Only registered policyholders can add products.")
        self.products[product_code] = start_date or datetime.utcnow()

    def suspend(self) -> None:
        if self.status == "SUSPENDED":
            return
        self.status = "SUSPENDED"

    def reactivate(self) -> None:
        if self.status != "REGISTERED":
            self.status = "REGISTERED"

    def cancel(self) -> None:
        self.status = "CANCELLED"

    def __str__(self) -> str:
        prods = ", ".join(sorted(self.products.keys())) or "None"
        return f"{self.policy_id} | {self.full_name} | {self.status} | Products: {prods}"
