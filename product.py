# product.py
from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime

@dataclass
class Product:
    code: str
    name: str
    premium: float
    is_active: bool = True
    updated_at: Optional[datetime] = field(default=None)

    def update(self, *, name: Optional[str] = None, premium: Optional[float] = None) -> None:
        """Update mutable fields of a product."""
        if name is not None:
            self.name = name
        if premium is not None:
            if premium <= 0:
                raise ValueError("Premium must be positive.")
            self.premium = premium
        self.updated_at = datetime.utcnow()

    def suspend(self) -> None:
        """Soft-suspend a product (can be reactivated later)."""
        self.is_active = False
        self.updated_at = datetime.utcnow()

    def reactivate(self) -> None:
        self.is_active = True
        self.updated_at = datetime.utcnow()

    def __str__(self) -> str:
        status = "ACTIVE" if self.is_active else "SUSPENDED"
        return f"{self.code} | {self.name} | Premium: {self.premium:.2f} | {status}"
