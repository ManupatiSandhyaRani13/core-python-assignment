def menu_management():
    while (True):
        print("1.Add item\n2.Remove item\n3.Check item\n4.Exit")
        choice = int(input("Enter your choice : "))
        if choice == 1:
            add_item(initial_menu)
        elif choice == 2:
            remove_item(initial_menu)
        elif choice == 3:
            check_item(initial_menu)
        else:
            exit(0)


def add_item(initial_menu):
    new_item = input("Enter the new item : ")
    if new_item in initial_menu:
        print(f"{new_item} already present in the menu")
    else:
        initial_menu.append(new_item)
    print("Updated Menu = ", initial_menu)


def remove_item(initial_menu):
    rem_item = input('Enter an item to be removed : ')
    if rem_item not in initial_menu:
        print(f"{rem_item} does not present in the menu")
    else:
        initial_menu.remove(rem_item)
    print("Updated menu = ", initial_menu)


def check_item(initial_menu):
    item_check = input("Enter the item to be checked : ")
    if item_check in initial_menu:
        print(f'"{item_check} is available" ')
    else:
        print(f'"{item_check}" is not available ')


initial_menu = []
while True:
    item = input("Enter the menu items ( or type exit to stop) : ")
    if item.lower() == 'exit':
        break
    initial_menu.append(item)
print(f"cart_items = {initial_menu}")
while True:
    menu_management()

