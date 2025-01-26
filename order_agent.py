from menu_agent import menu

orders = []

def create_order(order_id, items):
    for item_id in items:
        if not any(item["id"] == item_id for item in menu):
            return {"error": f"Menu item with ID {item_id} not found"}

    orders.append({"id": order_id, "items": items, "status": "Pending"})
    return {"message": "Order created", "order": {"id": order_id, "items": items, "status": "Pending"}}

def list_orders():
    return orders

def update_order_status(order_id, new_status):
    for order in orders:
        if order["id"] == order_id:
            order["status"] = new_status
            return {"message": "Order status updated", "order": order}
    return {"error": "Order not found"}
