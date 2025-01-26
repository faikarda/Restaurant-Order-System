menu = []

def add_menu_item(item_id, name, price):
    menu.append({"id": item_id, "name": name, "price": price})
    return {"message": "Item added to menu", "item": {"id": item_id, "name": name, "price": price}}

def list_menu():
    return menu
