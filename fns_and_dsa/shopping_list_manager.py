def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            
            item_to_add = input("Enter the item name to add: ").strip()
            if item_to_add:
              
                shopping_list.append(item_to_add.capitalize())
                print(f"'{item_to_add.capitalize()}' added to the list.")
            else:
                print("Cannot add an empty item.")
        elif choice == '2':
            
            if not shopping_list:
                print("The shopping list is already empty. Nothing to remove.")
                continue

            item_to_remove = input("Enter the item name to remove: ").strip().capitalize()
            
            if not item_to_remove:
                print("Please enter a valid item name.")
                continue
        elif choice == '3':
            
            print("\n--- CURRENT SHOPPING LIST ---")
            if not shopping_list:
                print("Your list is empty!")
        elif choice == '4':
            
            print("Thank you for using the Shopping List Manager. Goodbye!")
            break
        
        else:
            
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()