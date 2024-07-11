from models.item import Item
from models.shop import Shop

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_new_item()
        elif choice == '2':
            list_items()
        elif choice == '3':
            delete_item()
        elif choice == '4':
            find_item_by_id()
        elif choice == '5':
            add_new_shop()
        elif choice == '6':
            delete_shop()
        elif choice == '7':
            find_shop_by_id()
        elif choice == '8':
            list_shops_and_items()
        elif choice == '9':
            exit_program()
            
        
def print_menu():
    print("\nWelcome the general stores of Gielinor!")
    print("1. Add New Item")
    print("2. List All Items")
    print("3. Delete Item")
    print("4. Find Item by ID")
    print("5. Add New Shop")
    print("6. Delete Shop")
    print("7. Find Shop by ID")
    print("8. List All Shops and Items")
    print("9. Exit")

def add_new_item():
    name = input("Enter Item Name: ")
    description = input("Enter Item Description: ")
    price = float(input("Enter Item Price: "))
    shop_id = int(input("Enter Shop ID: "))
    Item.create(name, description, price, shop_id)
    print(f"Item '{name}' added successfully")

def list_items():
    items = Item.all()
    if items:
        print("Listing all items:")
        for item in items:
            print(item)
    else:
        print("No items found.")

def delete_item():
    item_id = int(input("Enter Item ID to delete: "))
    Item.delete(item_id)
    print(f"Item with ID={item_id} deleted successfully.")

def find_item_by_id():
    item_id = int(input("Enter Item ID to find: "))
    item = Item.find_by_id(item_id)
    if item:
        print("Item found:")
        print(item)
    else:
        print(f"Item with ID={item_id} not found.")

def add_new_shop():
    name = input("Enter Shop Name: ")
    location = input("Enter Shop Location: ")
    owner = input("Enter Shop Owner: ")

    shop = Shop.create(name, location, owner)
    print(f"Shop '{name}' added successfully with id={shop.id}")

def delete_shop():
    shop_id = int(input("Enter Shop ID to delete: "))
    Shop.delete(shop_id)
    print(f"Shop with ID={shop_id} deleted successfully.")

def find_shop_by_id():
    shop_id = int(input("Enter Shop ID to find: "))
    shop = Shop.find_by_id(shop_id)
    if shop:
        print("Shop found:")
        print(shop)
    else:
        print(f"Shop with ID={shop_id} not found.")

def list_shops_and_items():
    shops = Shop.all()
    if shops:
        print("\nListing all shops and their items:")
        for shop in shops:
            print(f"\n{shop}")
            items = Item.find_by_shop_id(shop.id)
            if items:
                print("Items:")
                for item in items:
                    print(f"\t{item}")
            else:
                print("\tNo items found for this shop.")
    else:
        print("No shops found.")

def exit_program():
    print("Goodbye!")
    exit()

if __name__ == "__main__":
    main()