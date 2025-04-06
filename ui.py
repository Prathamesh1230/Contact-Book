from contact import *
from utils import *

def menu():
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            if is_valid_phone(phone) and is_valid_email(email):
                add_contact(name, phone, email)
                print("✅ Contact added.")
            else:
                print("❌ Invalid phone or email.")
        elif choice == '2':
            contacts = get_all_contacts()
            for contact in contacts:
                print(contact)
        elif choice == '3':
            name = input("Enter name to search: ")
            results = search_contact(name)
            for contact in results:
                print(contact)
        elif choice == '4':
            contact_id = int(input("Enter ID to update: "))
            name = input("New Name: ")
            phone = input("New Phone: ")
            email = input("New Email: ")
            update_contact(contact_id, name, phone, email)
            print("✅ Contact updated.")
        elif choice == '5':
            contact_id = int(input("Enter ID to delete: "))
            delete_contact(contact_id)
            print("🗑️ Contact deleted.")
        elif choice == '6':
            print("👋 Exiting Contact Book...")
            break
        else:
            print("⚠️ Invalid choice.")
