from menu_agent import add_menu_item, list_menu
from order_agent import create_order, list_orders, update_order_status
from notification_agent import create_notification, list_notifications
from inventory_agent import add_inventory_item, check_inventory, list_inventory
from payment_agent import process_payment, list_payments
from menu_agent import menu

def order_process_flow(order_id, items):
    
    create_response = create_order(order_id, items)
    if "error" in create_response:
        print(create_response["error"])
        return
    print(f"Order placed: {', '.join([item['name'] for item in menu if item['id'] in items])}")

    update_response = update_order_status(order_id, "Confirmed")
    print(update_response["message"])  

    update_response = update_order_status(order_id, "Preparing")
    print(update_response["message"])  

    update_response = update_order_status(order_id, "Ready")
    print(update_response["message"])  

    total_price = sum(item['price'] for item in menu if item['id'] in items)
    payment_response = process_payment(order_id, total_price)
    print(f"{payment_response['message']}: ${total_price:.2f}")

if __name__ == "__main__":
    add_menu_item(1, "Pizza", 15.0)
    add_menu_item(2, "Burger", 10.0)

    order_process_flow(101, [1, 2])



