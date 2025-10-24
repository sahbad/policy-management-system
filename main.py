# main.py
from datetime import datetime, timedelta
from product import Product
from policyholder import Policyholder
from payment import PaymentProcessor

def seed_products():
    basic = Product(code="BAS01", name="Basic Health", premium=15000)
    family = Product(code="FAM10", name="Family Cover", premium=40000)
    return {p.code: p for p in (basic, family)}

def describe_policyholder(ph: Policyholder) -> None:
    print(f"\n--- Policyholder ---\n{ph}")
    for code, start in ph.products.items():
        print(f"  - {code} (since {start.date()})")

def run_demo():
    products = seed_products()
    pay = PaymentProcessor()

    # Two policyholders
    ada = Policyholder(policy_id="PH1001", full_name="Adaeze Okoye", email="ada@example.com")
    femi = Policyholder(policy_id="PH1002", full_name="Femi Badru", email="femi@example.com")

    # Register for products
    ada.register_for_product("BAS01")
    femi.register_for_product("FAM10")

    # Product maintenance
    products["BAS01"].update(premium=16000)  # small refresh
    products["FAM10"].suspend()              # show suspend/reactivate path
    products["FAM10"].reactivate()

    # Payments (one on time, one late to trigger penalty)
    today = datetime.utcnow()
    on_time_due = today
    late_due = today - timedelta(days=10)

    pay_ada = pay.process_payment(
        policy_id=ada.policy_id,
        product_code="BAS01",
        amount=products["BAS01"].premium,
        due_date=on_time_due,
        paid_at=today,  # on time
        penalty_policy="percent"
    )
    pay_femi = pay.process_payment(
        policy_id=femi.policy_id,
        product_code="FAM10",
        amount=products["FAM10"].premium,
        due_date=late_due,
        paid_at=today,  # late by ~5 days
        penalty_policy="percent"
    )

    # Display account details
    describe_policyholder(ada)
    print(f"Last payment: {pay_ada.amount} | penalty: {pay_ada.penalty_applied}")
    describe_policyholder(femi)
    print(f"Last payment: {pay_femi.amount} | penalty: {pay_femi.penalty_applied}")

if __name__ == "__main__":
    run_demo()
