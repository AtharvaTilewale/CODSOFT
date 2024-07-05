import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# ContactEntry class to hold contact details
class ContactEntry:
    def __init__(self, contact_name, contact_phone, contact_email, contact_address):
        """
        Initialize a ContactEntry object with name, phone, email, and address.

        Args:
        - contact_name (str): Name of the contact.
        - contact_phone (str): Phone number of the contact.
        - contact_email (str): Email address of the contact.
        - contact_address (str): Physical address of the contact.
        """
        self.contact_name = contact_name
        self.contact_phone = contact_phone
        self.contact_email = contact_email
        self.contact_address = contact_address

# Main ContactKeeper class
class ContactKeeper:
    def __init__(self, root):
        """
        Initialize the ContactKeeper application.

        Args:
        - root (tk.Tk): The main tkinter root window.
        """
        self.root = root
        self.contacts_db = {}

        self.root.title("Contact Keeper")
        self.root.geometry("400x600")
        self.root.configure(bg="white")  # Set background color

        self.title_label = tk.Label(self.root, text="Contact Keeper", font=("Helvetica", 16), bg="white")
        self.title_label.pack(pady=10)

        # Entry style configuration
        entry_style = {
            "bg": "white",
            "bd": 1,
            "relief": "solid",
            "font": ("Helvetica", 10)
        }

        # Search entry setup
        self.entry_search = tk.Entry(self.root, width=30, **entry_style)
        self.entry_search.pack(pady=10, padx=10, ipady=3, fill=tk.X)
        self.entry_search.insert(0, "Search Contact")
        self.entry_search.bind('<FocusIn>', self.on_entry_click)
        self.entry_search.bind('<FocusOut>', self.on_focus_out)
        self.entry_search.bind('<Return>', self.search_contact)

        # Frame for buttons
        self.frame_buttons = tk.Frame(self.root, bg="white")
        self.frame_buttons.pack(pady=5)

        # Button style configuration for home screen
        button_style = {
            "bg": "white",
            "font": ("Helvetica", 10),
            "bd": 1,
            "relief": "solid",
            "highlightthickness": 0,
            "borderwidth": 1,
            "highlightbackground": "navy",
            "highlightcolor": "navy",
            "activebackground": "white",
            "activeforeground": "black"
        }

        # Add New Contact button
        self.btn_add = tk.Button(self.frame_buttons, text="Add New Contact", command=self.setup_add_contact_ui, **button_style)
        self.btn_add.pack(side=tk.LEFT, padx=(10, 5))

        # Remove Contact button
        self.btn_delete = tk.Button(self.frame_buttons, text="Remove Contact", command=self.remove_contact, **button_style)
        self.btn_delete.pack(side=tk.LEFT, padx=(5, 10))

        # Listbox to display contacts
        self.lst_contacts = tk.Listbox(self.root, bg="white")
        self.lst_contacts.pack(pady=20, fill=tk.BOTH, expand=True)
        self.lst_contacts.bind('<Double-Button-1>', self.update_contact_ui)  # Double-click to update contact

        # Display initial list of contacts
        self.display_contacts()

    def setup_add_contact_ui(self):
        """
        Set up the UI for adding a new contact.
        """
        self.clear_home_screen()

        # Button and entry style configuration for add contact UI
        button_style = {
            "bg": "white",
            "font": ("Helvetica", 10),
            "bd": 1,
            "relief": "solid",
            "highlightthickness": 0,
            "borderwidth": 1,
            "highlightbackground": "navy",
            "highlightcolor": "navy",
            "activebackground": "white",
            "activeforeground": "black"
        }

        entry_style = {
            "bg": "white",
            "bd": 1,
            "relief": "solid",
            "font": ("Helvetica", 10)
        }

        # Back button to return to home screen
        self.btn_back = tk.Button(self.root, text="Back", command=self.display_home_screen, **button_style)
        self.btn_back.pack(pady=5)

        # Labels and entry fields for name, phone, email, and address
        self.label_name = tk.Label(self.root, text="Name:", bg="white")
        self.label_name.pack(pady=(0, 5), padx=10, anchor=tk.W)
        self.entry_name = tk.Entry(self.root, width=30, **entry_style)
        self.entry_name.pack(pady=5, padx=10, ipady=3, fill=tk.X)

        self.label_phone = tk.Label(self.root, text="Phone:", bg="white")
        self.label_phone.pack(pady=(0, 5), padx=10, anchor=tk.W)
        self.entry_phone = tk.Entry(self.root, width=30, **entry_style)
        self.entry_phone.pack(pady=5, padx=10, ipady=3, fill=tk.X)

        self.label_email = tk.Label(self.root, text="Email:", bg="white")
        self.label_email.pack(pady=(0, 5), padx=10, anchor=tk.W)
        self.entry_email = tk.Entry(self.root, width=30, **entry_style)
        self.entry_email.pack(pady=5, padx=10, ipady=3, fill=tk.X)

        self.label_address = tk.Label(self.root, text="Address:", bg="white")
        self.label_address.pack(pady=(0, 10), padx=10, anchor=tk.W)
        self.entry_address = tk.Entry(self.root, width=30, **entry_style)
        self.entry_address.pack(pady=5, padx=10, ipady=3, fill=tk.X)

        # Save contact button
        self.btn_save = tk.Button(self.root, text="Save Contact", command=self.save_contact, **button_style)
        self.btn_save.pack(pady=5)

    def display_home_screen(self):
        """
        Display the home screen with search, add, and remove contact options.
        """
        self.clear_add_contact_ui()

        # Show title label when back to home screen
        self.title_label.pack(pady=10)

        # Entry style configuration for home screen
        entry_style = {
            "bg": "white",
            "bd": 1,
            "relief": "solid",
            "font": ("Helvetica", 10)
        }

        # Search entry setup
        self.entry_search = tk.Entry(self.root, width=30, **entry_style)
        self.entry_search.pack(pady=10, padx=10, ipady=3, fill=tk.X)
        self.entry_search.insert(0, "Search Contact")
        self.entry_search.bind('<FocusIn>', self.on_entry_click)
        self.entry_search.bind('<FocusOut>', self.on_focus_out)
        self.entry_search.bind('<Return>', self.search_contact)

        # Frame for buttons
        self.frame_buttons = tk.Frame(self.root, bg="white")
        self.frame_buttons.pack(pady=5)

        # Button style configuration for home screen
        button_style = {
            "bg": "white",
            "font": ("Helvetica", 10),
            "bd": 1,
            "relief": "solid",
            "highlightthickness": 0,
            "borderwidth": 1,
            "highlightbackground": "navy",
            "highlightcolor": "navy",
            "activebackground": "white",
            "activeforeground": "black"
        }

        # Add New Contact button
        self.btn_add = tk.Button(self.frame_buttons, text="Add New Contact", command=self.setup_add_contact_ui, **button_style)
        self.btn_add.pack(side=tk.LEFT, padx=(10, 5))

        # Remove Contact button
        self.btn_delete = tk.Button(self.frame_buttons, text="Remove Contact", command=self.remove_contact, **button_style)
        self.btn_delete.pack(side=tk.LEFT, padx=(5, 10))

        # Listbox to display contacts
        self.lst_contacts = tk.Listbox(self.root, bg="white")
        self.lst_contacts.pack(pady=20, fill=tk.BOTH, expand=True)
        self.lst_contacts.bind('<Double-Button-1>', self.update_contact_ui)  # Double-click to update contact

        # Display initial list of contacts
        self.display_contacts()

    def clear_home_screen(self):
        """
        Clear the home screen UI elements.
        """
        self.title_label.pack_forget()

        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Entry) or isinstance(widget, tk.Label) or isinstance(widget, tk.Button) or isinstance(widget, tk.Listbox) or isinstance(widget, tk.Frame):
                widget.pack_forget()

    def clear_add_contact_ui(self):
        """
        Clear the add contact UI elements.
        """
        if hasattr(self, 'btn_back'):
            self.btn_back.pack_forget()

        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Entry) or isinstance(widget, tk.Label) or isinstance(widget, tk.Button):
                widget.pack_forget()

    def save_contact(self):
        """
        Save the contact details entered into the database.
        """
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
        """
        Display the list of contacts in the listbox.
        """
        self.lst_contacts.delete(0, tk.END)
        if not self.contacts_db:
            self.lst_contacts.insert(tk.END, "No contact found.")
        else:
            for contact_phone, contact in self.contacts_db.items():
                self.lst_contacts.insert(tk.END, f"{contact.contact_name} - {contact.contact_phone}")

    def search_contact(self, event=None):
        """
        Search contacts based on the search term entered.
        """
        search_term = self.entry_search.get()
        self.lst_contacts.delete(0, tk.END)
        found = False
        for contact_phone, contact in self.contacts_db.items():
            if search_term.lower() in contact.contact_name.lower() or search_term in contact_phone:
                self.lst_contacts.insert(tk.END, f"{contact.contact_name} - {contact.contact_phone}")
                found = True
        if not found:
            self.lst_contacts.insert(tk.END, "No contact found.")

    def remove_contact(self):
        """
        Remove a contact based on the phone number entered.
        """
        search_term = simpledialog.askstring("Remove", "Enter phone number of the contact to remove:")
        if search_term is None:
            return  # User cancelled, do nothing
        if search_term in self.contacts_db:
            del self.contacts_db[search_term]
            messagebox.showinfo("Success", "Contact removed successfully!")
            self.display_contacts()  # Update contact list after removal
        else:
            messagebox.showerror("Error", "Contact not found!")

    def update_contact(self, phone_number):
        """
        Update an existing contact's details.

        Args:
        - phone_number (str): The phone number of the contact to update.
        """
        contact_name = self.entry_name.get()
        contact_phone = self.entry_phone.get()
        contact_email = self.entry_email.get()
        contact_address = self.entry_address.get()

        if contact_name and contact_phone:
            updated_contact = ContactEntry(contact_name, contact_phone, contact_email, contact_address)
            self.contacts_db[phone_number] = updated_contact
            messagebox.showinfo("Success", "Contact updated successfully!")
            self.display_home_screen()  # Go back to home screen after updating
        else:
            messagebox.showwarning("Input Error", "Name and phone number are required!")

    def on_entry_click(self, event):
        """
        Handle behavior when the search entry is clicked (to remove default text).
        """
        if self.entry_search.get() == "Search Contact":
            self.entry_search.delete(0, tk.END)
            self.entry_search.config(fg='black')

    def on_focus_out(self, event):
        """
        Handle behavior when the search entry loses focus (to restore default text if empty).
        """
        if self.entry_search.get() == "":
            self.entry_search.insert(0, "Search Contact")
            self.entry_search.config(fg='grey')

    def update_contact_ui(self, event=None):
        """
        Update UI when a contact is double-clicked in the listbox for updating.
        """
        selected_index = self.lst_contacts.curselection()
        if selected_index:
            self.setup_update_contact_ui()

    def setup_update_contact_ui(self):
        """
        Set up the UI for updating an existing contact.
        """
        selected_index = self.lst_contacts.curselection()
        if not selected_index:
            return

        selected_contact = self.lst_contacts.get(selected_index)
        selected_phone = selected_contact.split(" - ")[1]

        if selected_phone in self.contacts_db:
            contact = self.contacts_db[selected_phone]
            self.setup_add_contact_ui()  # Reuse add contact UI setup
            self.entry_name.insert(0, contact.contact_name)
            self.entry_phone.insert(0, contact.contact_phone)
            self.entry_email.insert(0, contact.contact_email)
            self.entry_address.insert(0, contact.contact_address)
            self.btn_save.configure(command=lambda: self.update_contact(selected_phone))
            self.btn_back.configure(command=self.display_home_screen)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactKeeper(root)
    root.mainloop()
