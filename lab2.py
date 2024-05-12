"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 2
---------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create a class for a contact in a contact management system.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Create a class named Contact that represents a contact in a contact management system. 
# This class should have an initialiser with attributes for name, phone_number, and email.
# Add a class attribute to keep track of the total number of contacts.
class Employee:
    def __init__(self, name, idno):
        self.name=name
        self.idno=idno
        


# Create at least two instances of the Contact class with different data.
slave1=Employee("mike", 69)
slave2=Employee("oxlong", 420)


# Write code that prints out the details of each contact you have created.
print("am", slave1.name, slave1.idno)
print("me", slave2.name, slave2.idno)


