"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 4
---------------------------------------------------------------------------------
- File Name: lab4.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Implement the ContactManager class and perform CRUD operations.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# 1. Import the ContactManager class here.
from contact_manager import ContactManager


# 2. Go to the 'contact_manager.py' file and implement the TODO in the display_contacts method.



# 3. Create two contacts using the ContactManager.

cm = ContactManager()

cm.add_contact("biden", "biden69@gaymail", "69")
cm.add_contact("jkeee", "jkee420@sciggelymail", "420")

# 4. Display all contacts.
cm.display_contacts()


# 5. Update the email address of one contact.

cm.update_contact("jkeee", "jkeee420@sciggelymail", "421")


# 6. Remove one of the contacts.

cm.remove_contact("biden")

# 7. Display all contacts again.

cm.display_contacts()
