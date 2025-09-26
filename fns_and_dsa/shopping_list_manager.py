def display_menu():
    print("Welcome to the Shopping List Manager!")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")


def main():
    shopping_list_manager = []
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()
        if choice == '1':
            item = input("Enter item to add: ").strip()
            shopping_list_manager.append(item)
            print(f"{item} added to the list.")
        elif choice == '2':
            item = input("Enter item to remove: ").strip()
            if item in shopping_list_manager:
                shopping_list_manager.remove(item)
                print(f"{item} removed from the list.")
            else:
                print(f"{item} not found in the list.")
        elif choice == '3':
            print("Shopping List:")
            for idx, item in enumerate(shopping_list_manager, start=1):
                print(f"{idx}. {item}")
        elif choice == '4':
            print("Exiting the Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

        print(f"Current Shopping List: {shopping_list_manager}")

if __name__ == "__main__":
    main()
