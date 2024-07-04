import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# ContactEntry class to hold contact details
class ContactEntry:
    def __init__(self, contact_name, contact_phone, contact_email, contact_address):
        self.contact_name = contact_name
        self.contact_phone = contact_phone
        self.contact_email = contact_email
        self.contact_address = contact_address

# Main ContactKeeper class
class ContactKeeper:
    def __init__(self, root):
        self.root = root
        self.contacts_db = {}
        
        self.root.title("Contact Keeper")
        self.root.geometry("400x600")

        self.title_label = tk.Label(self.root, text="Contact Keeper", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        self.btn_add = tk.Button(self.root, text="Add New Contact", command=self.add_new_contact)
        self.btn_add.pack(pady=5)

        self.btn_search = tk.Button(self.root, text="Search Contact", command=self.search_contact)
        self.btn_search.pack(pady=5)

        self.btn_update = tk.Button(self.root, text="Update Contact", command=self.update_contact)
        self.btn_update.pack(pady=5)

        self.btn_delete = tk.Button(self.root, text="Remove Contact", command=self.remove_contact)
        self.btn_delete.pack(pady=5)

        self.lst_contacts = tk.Listbox(self.root)
        self.lst_contacts.pack(pady=20, fill=tk.BOTH, expand=True)

        self.display_contacts()

    def add_new_contact(self):
        contact_name = simpledialog.askstring("Input", "Enter contact name:")
        contact_phone = simpledialog.askstring("Input", "Enter contact phone number:")
        contact_email = simpledialog.askstring("Input", "Enter contact email:")
        contact_address = simpledialog.askstring("Input", "Enter contact address:")

        if contact_name and contact_phone:
            new_contact = ContactEntry(contact_name, contact_phone, contact_email, contact_address)
            self.contacts_db[contact_phone] = new_contact
            messagebox.showinfo("Success", "Contact added successfully!")
            self.display_contacts()
        else:
            messagebox.showwarning("Input Error", "Name and phone number are required!")

    def display_contacts(self):
        self.lst_contacts.delete(0, tk.END)
        if not self.contacts_db:
            self.lst_contacts.insert(tk.END, "No contact found.")
        else:
            for contact_phone, contact in self.contacts_db.items():
                self.lst_contacts.insert(tk.END, f"{contact.contact_name} - {contact.contact_phone}")

    def search_contact(self):
        search_term = simpledialog.askstring("Search", "Enter name or phone number to search:")
        self.lst_contacts.delete(0, tk.END)
        found = False
        for contact_phone, contact in self.contacts_db.items():
            if search_term in contact.contact_name or search_term in contact_phone:
                self.lst_contacts.insert(tk.END, f"{contact.contact_name} - {contact.contact_phone}")
                found = True
        if not found:
            self.lst_contacts.insert(tk.END, "No contact found.")

    def update_contact(self):
        search_term = simpledialog.askstring("Search", "Enter phone number of the contact to update:")
        if search_term in self.contacts_db:
            contact = self.contacts_db[search_term]
            new_name = simpledialog.askstring("Input", "Enter new contact name:", initialvalue=contact.contact_name)
            new_phone = simpledialog.askstring("Input", "Enter new contact phone number:", initialvalue=contact.contact_phone)
            new_email = simpledialog.askstring("Input", "Enter new contact email:", initialvalue=contact.contact_email)
            new_address = simpledialog.askstring("Input", "Enter new contact address:", initialvalue=contact.contact_address)

            if new_name and new_phone:
                del self.contacts_db[search_term]
                updated_contact = ContactEntry(new_name, new_phone, new_email, new_address)
                self.contacts_db[new_phone] = updated_contact
                messagebox.showinfo("Success", "Contact updated successfully!")
                self.display_contacts()
            else:
                messagebox.showwarning("Input Error", "Name and phone number are required!")
        else:
            messagebox.showerror("Error", "Contact not found!")

    def remove_contact(self):
        search_term = simpledialog.askstring("Search", "Enter phone number of the contact to remove:")
        if search_term in self.contacts_db:
            del self.contacts_db[search_term]
            messagebox.showinfo("Success", "Contact removed successfully!")
            self.display_contacts()
        else:
            messagebox.showerror("Error", "Contact not found!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactKeeper(root)
    root.mainloop()
