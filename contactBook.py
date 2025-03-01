contacts = {}

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    choice = input("Choose an option: ")
    
    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        contacts[name] = phone
        print(f"Contact '{name}' added successfully.")
    elif choice == "2":
        if not contacts:
            print("No contacts available.")
        else:
            for name, phone in contacts.items():
                print(f"Name: {name}, Phone: {phone}")
    elif choice == "3":
        name = input("Enter Name to search: ")
        if name in contacts:
            print(f"Name: {name}, Phone: {contacts[name]}")
        else:
            print("Contact not found.")
    elif choice == "4":
        name = input("Enter Name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print("Contact not found.")
    elif choice == "5":
        break
    else:
        print("Invalid choice, please try again.")