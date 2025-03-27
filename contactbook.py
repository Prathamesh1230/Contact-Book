# Contact Book

import os


CONTACT_FILE = "contacts.txt"

def load_contacts():

    if not os.path.exists(CONTACT_FILE):
        return {}
    with open(CONTACT_FILE, "r") as file:
        contacts = {}
        for line in file:
            name, number = line.strip().split(",")
            contacts[name] = number
        return contacts

def save_contacts(contacts):
    # Save contacts to the file
    with open(CONTACT_FILE, "w") as file:
        for name, number in contacts.items():
            file.write(f"{name},{number}\n")

def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    number = input("Enter contact number: ").strip()
    if name in contacts:
        print("Contact already exists.")
    else:
        contacts[name] = number
        print(f"Contact '{name}' added successfully!")

def search_contact(contacts):
    name = input("Enter the name of the contact to search for: ").strip()
    if name in contacts:
        print(f"Name: {name}, Number: {contacts[name]}")
    else:
        print("Contact not found.")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ").strip()
    if name in contacts:
        number = input("Enter the new contact number: ").strip()
        contacts[name] = number
        print(f"Contact '{name}' updated successfully!")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print("Contact not found.")

def main():
    print("Welcome to the Contact Book!")
    contacts = load_contacts()
    
    while True:
        print("\nChoose an option:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display All Contacts")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            if contacts:
                print("\nAll Contacts:")
                for name, number in contacts.items():
                    print(f"Name: {name}, Number: {number}")
            else:
                print("No contacts available.")
        elif choice == "6":
            save_contacts(contacts)
            print("Contacts saved successfully. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the Contact Book application
main()
