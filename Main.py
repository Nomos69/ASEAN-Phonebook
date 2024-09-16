# Main Python File to run from
from ContactArray import ContactList
from Contact import Contact

MENUS = {
    "main": {
        1: "Store to ASEAN Phonebook",
        2: "Edit entry in ASEAN Phonebook",
        3: "Delete entry from ASEAN Phonebook",
        4: "View/Search ASEAN Phonebook",
        5: "Exit"
    },
    "views": {
        1: "Search by country",
        2: "Search by surname",
        3: "View all",
        4: "Go back to main menu"
    },
    "edit": {
        1: "Student Number",
        2: "Surname",
        3: "Gender",
        4: "Occupation",
        5: "Country Code",
        6: "Area Code",
        7: "Phone Number",
        8: "None - Go back to main menu"
    },
    "cc": {
        1: "Burma", # 856
        2: "Cambodia", # 855
        3: "Thailand", # 66
        4: "Vietnam", # 84
        5: "Malaysia", # 60
        6: "Philippines", # 63
        7: "Indonesia", # 62
        8: "Timor Leste", # 670
        9: "Laos", # 95
        10: "Brunei", # 673
        11: "Singapore", #65
        12: "All",
        0: "No More"
    }
}

def showMenu(target: str, inline :int = None):
    """Shows the target menu in the ASEAN Phonebook program.
    
    Args:
        target (str): Target menu to show. Refer to MENUS dictionary.
        inline (int): If not none, then will create an inline menu with n items each.
    """
    print("\n<-----Menu----->")
    i = 1 if inline != None else None
    for menu in MENUS[target]:
        out = "[{}]".format(menu)
        if inline != None and i == inline:
            out = "\n[{}]".format(menu)
        print("{} {}".format(out, MENUS[target][menu]), end= "\t" if inline != None else "\n")
        if i != None:
            i = 1 if i == inline else i + 1
        
def receiveContactInfo(pb: ContactList) -> None:
    """Cast several prompts for user to input about the
    contact's data.

    Returns:
       Contact: Contact object created based from data.
    """
    while True:
        try:
            stdn = prompt("Enter student number: ")    
            lname = prompt("Enter surname: ")
            fname = prompt("Enter first name: ")
            occupation = prompt("Enter occupation: ")
            gender = prompt("Enter gender (M for male, F for female): ")
            if gender.upper() not in ['M', 'F']:
                print("Invalid gender. Please enter M for male or F for female.")
                continue
            showMenu("cc", 4)
            cc_choice = int(prompt("Enter country code choice: "))
            cc = convertChoices([cc_choice])[0]
            area = int(prompt("Enter area code: "))
            number = int(prompt("Enter number: "))
            contact = Contact(stdn, fname, lname, occupation, gender, cc, area, number)
            pb.insert(contact)  # Insert contact into the phonebook
            print("Contact added successfully!")
            return
        except ValueError:
            print("Invalid input. Please enter a valid value.")
        """        
        cc = int(prompt("Enter country code: "))
        area = int(prompt("Enter area code: "))
        number = int(prompt("Enter number: "))
        return Contact(stdn,fname,lname,occupation,gender,cc,area,number)
        """

def prompt(phrase: str) -> str:
    """Prompts an input to the user

    Args:
        phrase (str): Input phrase.

    Returns:
        str : Returns a string type of inputted value.
    """
    """
    return input(phrase)
    """

    while True:
        user_input = input(phrase)
        if user_input.strip() != "":  # Check if the input is not empty
            return user_input
        else:
            print("Invalid input. Please enter a valid value.")
def convertChoices(choices: list) -> list:
    """Converts choices from the phonebook menu
    into proper country code value for accuracy purposes.

    Args:
        choices (list): Choices selected by user during prompt.

    Returns:
        list: Converted values of choices.
    """
    for i in range(0, len(choices)):
        match choices[i]:
            case 1:
                choices[i] = 856 #Burma
            case 2:
                choices[i] = 855 #Cambodia
            case 3:
                choices[i] = 66 #Thailand
            case 4: 
                choices[i] = 84 #Vietnam
            case 5:
                choices[i] = 60 #Malaysia
            case 6:
                choices[i] = 63 #Philipines
            case 7:
                choices[i] = 62 #Indonesia
            case 8:
                choices[i] = 670 #Timor Leste
            case 9:
                choices[i] = 95 #Laos
            case 10:
                choices[i] = 673 #Brunei
            case 11:
                choices[i] = 65 #Singapore
    return choices

if __name__ == "__main__":
    pb = ContactList()
    while True:
        showMenu("main")
        opt = int(input("Select Operation: "))
        # Complete your code here please
        if opt == 1: 
            receiveContactInfo(pb)  # Pass the ContactList instance
            print("Contact added successfully!")
        elif opt == 2: # Edit Option
            showMenu("edit")
            edit_opt = int(input("Select edit option: "))
            stdn = prompt("Enter student number to edit: ")
            contact = pb.getContact(stdn)
            if contact:
                if edit_opt == 1:
                    new_stdn = prompt("Enter new student number: ")
                    contact.student_num = new_stdn
                elif edit_opt == 2:
                    new_surname = prompt("Enter new surname: ")
                    contact.surname = new_surname
                elif edit_opt == 3:
                    while True:
                        new_gender = prompt("Enter new gender (M for male, F for female): ")
                        if new_gender.upper() in ['M', 'F']:
                            contact.gender = new_gender
                            break
                        else:
                            print("Invalid gender. Please enter M for male or F for female.")
                elif edit_opt == 4:
                    new_occupation = prompt("Enter new occupation: ")
                    contact.occupation = new_occupation
                elif edit_opt == 5:
                    showMenu("cc", 4)
                    while True:
                        try:
                            cc_choice = int(prompt("Enter country code choice: "))
                            if cc_choice in range(1, 12):
                                cc = convertChoices([cc_choice])[0]
                                contact.country_code = cc
                                break
                            else:
                                print("Invalid country code choice. Please choose a number between 1 and 11.")
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                elif edit_opt == 6:
                    while True:
                        try:
                            new_area_code = int(prompt("Enter new area code: "))
                            contact.area_code = new_area_code
                            break
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                elif edit_opt == 7:
                    while True:
                        try:
                            new_phone_number = int(prompt("Enter new phone number: "))
                            contact.phone_number = new_phone_number
                            break
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                elif edit_opt == 8:
                    continue
                print("Contact updated successfully!")
            else:
                print("Contact not found")

        elif opt == 3: # Delete option
            stdn = prompt("Enter student number to delete: ")
            contact = pb.getContact(stdn)
            if contact:
                pb.deleteContact(stdn)
                print("Contact deleted successfully!")
            else:
                print("Contact not found")

        
        elif opt == 4: #View Option
            showMenu("views")
            view_opt = int(input("Select view option: "))
            if view_opt == 1: # View by Country
                country = prompt("Enter country to view: ")
                contacts = pb.viewContactsByCountry(country)
                if contacts:
                    for contact in contacts:
                        print(f"Student Number: {contact.student_num}, Surname: {contact.surname}, First Name: {contact.first_name}, Occupation: {contact.occupation}, Gender: {contact.gender}, Country Code: {contact.country_code}, Area Code: {contact.area_code}, Phone Number: {contact.phone_number}")
                else:
                    print("No contacts found for the specified country.")
            elif view_opt == 2: # View by Surname
                lname = prompt("Enter surname to view: ")
                contacts = pb.viewContactsBySurname(lname)
                if contacts:
                    for contact in contacts:
                        print(f"Student Number: {contact.student_num}, Surname: {contact.surname}, First Name: {contact.first_name}, Occupation: {contact.occupation}, Gender: {contact.gender}, Country Code: {contact.country_code}, Area Code: {contact.area_code}, Phone Number: {contact.phone_number}")
                else:
                    print("No contacts found for the specified surname.")
            elif view_opt == 3: #View all Contacts
                print(pb)  # Call the __str__ method directly
            elif view_opt == 4:
                continue
        elif opt == 5:
            print("Shutting down...")
            break