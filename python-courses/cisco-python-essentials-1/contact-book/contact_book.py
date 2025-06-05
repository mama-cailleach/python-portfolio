def display_menu():
    print("\nContact Book Menu:")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. List all contacts")
    print("5. Exit")

def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()
    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = {"phone": phone, "email": email}
        print("Contact added!")

def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    contact = contacts.get(name)
    if contact:
        print(f"Name: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

def list_contacts(contacts):
    if not contacts:
        print("No contacts to show.")
    else:
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def main():
    contacts = {}
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            delete_contact(contacts)
        elif choice == "4":
            list_contacts(contacts)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
