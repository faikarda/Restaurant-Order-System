payments = []

def process_payment(order_id, amount):
    payment = {"order_id": order_id, "amount": amount, "status": "Completed"}
    payments.append(payment)
    return {"message": "Payment completed", "payment": payment}

def list_payments():
    return payments