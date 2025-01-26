notifications = []

def create_notification(order_id, message):
    notifications.append({"order_id": order_id, "message": message})
    return {"message": "Notification created", "notification": {"order_id": order_id, "message": message}}

def list_notifications():
    return notifications
