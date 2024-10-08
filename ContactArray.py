# Array List implementation of Contacts
from Contact import Contact
#Sample comment
class ContactList:
    """Contact List class that creates an array list of the phonebook.
    """

    def __init__(self, size: int = 50):
        """
            Create an array list of contacts with default storage size of 50.
            
            Args:
                size (int): The initial size of the contact list. Defaults to 50.
    
        """
        self.phonebook = [None] * size
        self.size = 0
        self._get_contact_list = []
        

    def getSize(self):
        """
            Get the size of this contact list.
            
            Returns:
                int: The number of contacts in the contact list
        """
        return self.size
    
    def first(self) -> Contact:
        """
            Get the first contact in this contact list.
            Returns none if the list is empty.

            Returns:
                Contact: The first contact in the contact list, or None if the list is empty
        """
        # Complete this Method
        if self.isEmpty():
            return None
        return self.phonebook[0]
    
    def getLast(self) -> Contact:
        """
            Get the last contact in this contact list.
            Returns none if the list is empty.

            Returns:
                Contact: The last contact in the contact list, or None if the list is empty
        """
        # Complete this Method
        if self.isEmpty():
            return None
        return self.phonebook[self.size - 1]


    def getContactAtIndex(self, index: int) -> Contact:
        """Gets the contact at given index in the contact linked list.
        Returns None if index is not found in the list.

        Args:
            index (int): Index to get in the contact linked list.

        Returns:
            Contact: Contact at index at the specified index, or None if the index is out of range
        """
        # Complete this Method
        if index < 0 or index >= self.size:
            return None
        return self.phonebook[index]
    
    def getContact(self, student_num: str) -> Contact:
        """Gets the contact based on given student number. Will return None
        if contact is not found.

        Args:
            student_num (str): Student number to base search from.

        Returns:
            Contact:  Returns:
                Contact: The contact with the specified student number, or None if not found
        """
        # Complete this Method
        for contact in self.phonebook[:self.size]:
            if contact.student_num == student_num:
                return contact
        return None
    
    def getContactBySurname(self, surname: str) -> list:
        """Gets the contact based on surname. Will return None if contact is not found.

            Args:
                surname (str): The surname of the contact to retrieve.

            Returns:
                Contact: The contact with the specified surname, or None if not found
        """
        # Complete this Method
        contacts = []
        for i in range(self.size):
            if self.phonebook[i].surname == surname:
                contacts.append(self.phonebook[i])
        return contacts
    
    def isEmpty(self) -> bool:
        """
            Checks if contact list has no contacts.

            Returns:
                bool: True if the contact list is empty, False otherwise
        """
        return self.getSize() == 0
    
    def incrSize(self) -> None:
        """
            Increase the size of this contact list.
        """
        # Complete this Method
        self.size += 1

    def decrSize(self) -> None:
        """
            Decrease the size of this contact list
        """
        self.size -= 1

    def __increasePhonebookSize(self) -> None:
        """
            Increases the size of this phonebook by two times.
        """
        # Complete this Method
        new_phonebook = [None] * (len(self.phonebook) * 2)
        for i in range(self.size):
            new_phonebook[i] = self.phonebook[i]
        self.phonebook = new_phonebook 

    def insert(self, c : Contact) -> None:
        """Inserts new contact at index point.

        Args:
            c (Contact): Contact to be inserted.
        """
        # Complete this Method
        if self.size == len(self.phonebook):
            self.__increasePhonebookSize()
        index = self.__findIndexInsertion(c)
        self.__adjustPhonebook(index, self.size, "b")
        self.phonebook[index] = c
        self.incrSize()
        if self.size == 1:
            self._get_contact_list = [None] * len(self.phonebook)
        self._get_contact_list[index] = c 

    def __findIndexInsertion(self, c: Contact) -> int:
        """Finds the index to insert from based on contact's
        last name, and first name if both have the same first names.

        Args:
            c (Contact): Contact to compare and to be inserted.

        Returns:
            int: Node insertion point for new contact.
        """
        # Complete this Method
        for i in range(self.size):
            if c.surname < self.phonebook[i].surname:
                return i
            elif c.surname == self.phonebook[i].surname and c.firstname < self.phonebook[i].firstname:
                return i
        return self.size
    
    
    def __adjustPhonebook(self, start: int, end = int, dir: str = "f") -> None:
        """
        Adjusts the arrangement of this phonebook from start to end.

        Args:
            index (int): Index for adjustment.
            dir (str): Direction of adjustment:
                "f" -> Forward indexing adjustment. For example, element at index 0 takes the value of the element at index 1.
                "b" -> Backward indexing adjustment. For example, elemet at index 1 takes the value of the element at index 0.
        """
        # Complete this Method
        if dir == "f":
            for i in range(start, end):
                self.phonebook[i] = self.phonebook[i + 1]
        elif dir == "b":
            for i in range(start + 1 , end):
                self.phonebook[i] = self.phonebook[i - 1]
    
    def deleteContact(self, stdn: str) -> Contact:
        """Finds the contact based on their student number.
        Returns the deleted contact. Otherwise, returns -1 if not found.

        Args:
            stdn (str): Student number of contact to be deleted.

        Returns:
            Contact: Deleted contact, if found.
        """
        # Complete this Method
        for contact in self.phonebook[:self.size]:
            if contact.student_num == stdn:
                self.phonebook.remove(contact)
                print("Contact deleted successfully!")
                return
        print("Contact not found")
        
    def __sort(self, by: str) -> list:
        """
            Sorts the phonebook based on the contact's attribute value.
        
            Args:
                by (str): Attribute value to sort the phonebook from.
            
            Returns:
                list: A copy of this phonebook list sorted based on the attribute value given.
        """
        # Complete this method optionally
        # Correctly completing this method will reward up to 4 bonus points in your MTE.

        sorted_phonebook = self.phonebook[:self.size]
        if by == 'lname':
            sorted_phonebook.sort(key=lambda x: x.surname)
        elif by == 'fname':
            sorted_phonebook.sort(key=lambda x: x.firstname)
        elif by == 'stdn':
            sorted_phonebook.sort(key=lambda x: x.student_num)
        return sorted_phonebook
        
    def __str__(self, by: str = 'lname', surname: str = None) -> str:
        '''
        Prints every contact in this contact list.

        Args:
            by (str): Condition whether to print contact on a particular order based from some attribute.
            surname (str, optional): If provided, only contacts with this surname will be printed.

        Returns:
            str: Every contact in this contact list in a particular order.
        '''
        s = "<----Phonebook---->"
        if not self.isEmpty():
            sorted_phonebook = self.__sort(by)
            for contact in sorted_phonebook:
                if surname is not None and contact.surname == surname:
                    s += str(contact) + "\n"
                elif surname is None:
                    s += str(contact) + "\n"
        else:
            s += "\nThis phonebook is currently empty..."
        s += "\n<----End---->"
        return s