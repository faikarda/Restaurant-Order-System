inventory = {}

def add_inventory_item(item_id, quantity):
    if item_id in inventory:
        inventory[item_id] += quantity
    else:
        inventory[item_id] = quantity
    return {"message": "Inventory updated", "item_id": item_id, "quantity": inventory[item_id]}

def check_inventory(item_id):
    return inventory.get(item_id, 0)

def list_inventory():
    return inventory