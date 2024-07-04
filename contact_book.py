import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# Contact class to hold contact details
class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

# Main ContactBook class
class ContactBook:
    def __init__(self, root):
        self.root = root
        self.contacts = {}
        
        self.root.title("Contact Book")
        self.root.geometry("400x600")

        self.label = tk.Label(self.root, text="Contact Book", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.add_button.pack(pady=5)

        self.view_button = tk.Button(self.root, text="View Contacts", command=self.view_contacts)
        self.view_button.pack(pady=5)

        self.search_button = tk.Button(self.root, text="Search Contact", command=self.search_contact)
        self.search_button.pack(pady=5)

        self.update_button = tk.Button(self.root, text="Update Contact", command=self.update_contact)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(pady=5)

        self.contact_list = tk.Listbox(self.root)
        self.contact_list.pack(pady=20, fill=tk.BOTH, expand=True)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name:")
        phone = simpledialog.askstring("Input", "Enter contact phone number:")
        email = simpledialog.askstring("Input", "Enter contact email:")
        address = simpledialog.askstring("Input", "Enter contact address:")

        if name and phone:
            contact = Contact(name, phone, email, address)
            self.contacts[phone] = contact
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showwarning("Input Error", "Name and phone number are required!")

    def view_contacts(self):
        self.contact_list.delete(0, tk.END)
        for phone, contact in self.contacts.items():
            self.contact_list.insert(tk.END, f"{contact.name} - {contact.phone}")

    def search_contact(self):
        search_term = simpledialog.askstring("Search", "Enter name or phone number to search:")
        self.contact_list.delete(0, tk.END)
        for phone, contact in self.contacts.items():
            if search_term in contact.name or search_term in phone:
                self.contact_list.insert(tk.END, f"{contact.name} - {contact.phone}")

    def update_contact(self):
        search_term = simpledialog.askstring("Search", "Enter phone number of the contact to update:")
        if search_term in self.contacts:
            contact = self.contacts[search_term]
            new_name = simpledialog.askstring("Input", "Enter new contact name:", initialvalue=contact.name)
            new_phone = simpledialog.askstring("Input", "Enter new contact phone number:", initialvalue=contact.phone)
            new_email = simpledialog.askstring("Input", "Enter new contact email:", initialvalue=contact.email)
            new_address = simpledialog.askstring("Input", "Enter new contact address:", initialvalue=contact.address)

            if new_name and new_phone:
                del self.contacts[search_term]
                updated_contact = Contact(new_name, new_phone, new_email, new_address)
                self.contacts[new_phone] = updated_contact
                messagebox.showinfo("Success", "Contact updated successfully!")
            else:
                messagebox.showwarning("Input Error", "Name and phone number are required!")
        else:
            messagebox.showerror("Error", "Contact not found!")

    def delete_contact(self):
        search_term = simpledialog.askstring("Search", "Enter phone number of the contact to delete:")
        if search_term in self.contacts:
            del self.contacts[search_term]
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showerror("Error", "Contact not found!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
