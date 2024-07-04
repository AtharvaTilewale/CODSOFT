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

        self.btn_add = tk.Button(self.root, text="Add New Contact", command=self.setup_add_contact_ui)
        self.btn_add.pack(pady=5)

        self.btn_search = tk.Button(self.root, text="Search Contact", command=self.search_contact)
        self.btn_search.pack(pady=5)

        self.btn_delete = tk.Button(self.root, text="Remove Contact", command=self.remove_contact)
        self.btn_delete.pack(pady=5)

        self.lst_contacts = tk.Listbox(self.root)
        self.lst_contacts.pack(pady=20, fill=tk.BOTH, expand=True)

        self.display_contacts()

    def setup_add_contact_ui(self):
        self.clear_home_screen()

        self.btn_back = tk.Button(self.root, text="Back", command=self.display_home_screen)
        self.btn_back.pack(pady=5)

        self.entry_name = tk.Entry(self.root, width=30)
        self.entry_name.pack(pady=5, padx=10, ipady=3, fill=tk.X)
        self.label_name = tk.Label(self.root, text="Name:")
        self.label_name.pack(pady=(0,5), padx=10, anchor=tk.W)

        self.entry_phone = tk.Entry(self.root, width=30)
        self.entry_phone.pack(pady=5, padx=10, ipady=3, fill=tk.X)
        self.label_phone = tk.Label(self.root, text="Phone:")
        self.label_phone.pack(pady=(0,5), padx=10, anchor=tk.W)

        self.entry_email = tk.Entry(self.root, width=30)
        self.entry_email.pack(pady=5, padx=10, ipady=3, fill=tk.X)
        self.label_email = tk.Label(self.root, text="Email:")
        self.label_email.pack(pady=(0,5), padx=10, anchor=tk.W)

        self.entry_address = tk.Entry(self.root, width=30)
        self.entry_address.pack(pady=5, padx=10, ipady=3, fill=tk.X)
        self.label_address = tk.Label(self.root, text="Address:")
        self.label_address.pack(pady=(0,10), padx=10, anchor=tk.W)

        self.btn_save = tk.Button(self.root, text="Save Contact", command=self.save_contact)
        self.btn_save.pack(pady=5)

        # Re-add the buttons for Search and Remove
        self.btn_search = tk.Button(self.root, text="Search Contact", command=self.search_contact)
        self.btn_search.pack(pady=5)

        self.btn_delete = tk.Button(self.root, text="Remove Contact", command=self.remove_contact)
        self.btn_delete.pack(pady=5)

        # Re-add the listbox for displaying contacts
        self.lst_contacts = tk.Listbox(self.root)
        self.lst_contacts.pack(pady=20, fill=tk.BOTH, expand=True)

    def display_home_screen(self):
        self.clear_add_contact_ui()
        self.setup_add_contact_ui()  # Re-setup add contact UI
        self.display_contacts()  # Re-display contacts list

    def clear_home_screen(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Entry) or isinstance(widget, tk.Label) or isinstance(widget, tk.Button) or isinstance(widget, tk.Listbox):
                widget.pack_forget()

    def clear_add_contact_ui(self):
        if hasattr(self, 'btn_back'):
            self.btn_back.pack_forget()

        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Entry) or isinstance(widget, tk.Label) or isinstance(widget, tk.Button):
                widget.pack_forget()

    def save_contact(self):
        contact_name = self.entry_name.get()
        contact_phone = self.entry_phone.get()
        contact_email = self.entry_email.get()
        contact_address = self.entry_address.get()

        if contact_name and contact_phone:
            new_contact = ContactEntry(contact_name, contact_phone, contact_email, contact_address)
            self.contacts_db[contact_phone] = new_contact
            messagebox.showinfo("Success", "Contact added successfully!")
            self.display_home_screen()  # Go back to home screen after saving
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

    def remove_contact(self):
        search_term = simpledialog.askstring("Remove", "Enter phone number of the contact to remove:")
        if search_term in self.contacts_db:
            del self.contacts_db[search_term]
            messagebox.showinfo("Success", "Contact removed successfully!")
            self.display_home_screen()  # Update contact list after removal
        else:
            messagebox.showerror("Error", "Contact not found!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactKeeper(root)
    root.mainloop()
