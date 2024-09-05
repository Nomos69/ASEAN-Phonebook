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
        
def receiveContactInfo() -> Contact:
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
            return Contact(stdn, fname, lname, occupation, gender, cc, area, number)
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
            pass

        elif opt == 2: # Edit Option
            showMenu("edit")
            edit_opt = int(input("Select edit option: "))
            if edit_opt == 1:
                stdn = prompt("Enter student number to edit: ")
                pb.editContact(stdn, "Student Number", prompt("Enter new student number: ")) # Edit Student Number
            elif edit_opt == 2:
                stdn = prompt("Enter student number to edit: ")
                pb.editContact(stdn, "Surname", prompt("Enter new surname: ")) # Edit Student's Surname
            elif edit_opt == 3:
                stdn = prompt("Enter student number to edit: ")
                pb.editContact(stdn, "Gender", prompt("Enter new gender (M for male, F for female): ")) # Edit Student's Gender
            elif edit_opt == 4:
                stdn = prompt("Enter student number to edit: ")
                pb.editContact(stdn, "Occupation", prompt("Enter new occupation: ")) # Edit Student's Occupation

        elif opt == 3: # Delete Option 
            showMenu("views")
            del_opt = int(input("Select delete option: "))
            if del_opt == 1: # Delete by Student Number
                stdn = prompt("Enter student number to delete: ")
                pb.deleteContact(stdn)
                print("Contact deleted successfully!")
                

            elif del_opt == 2: # Delete by Surname
                lname = prompt("Enter surname to delete: ")
                pb.deleteContactBySurname(lname)
                print("Contacts deleted successfully!")

            elif del_opt == 3: # Delete by Country
                country = prompt("Enter country to delete: ")
                pb.deleteContactByCountry(country)
                print("Contacts deleted successfully!")

            elif del_opt == 4:
                pass
        elif opt == 4:
            view_opt = int(input("Select view option: "))
            if view_opt == 1:
               pass

            elif view_opt == 2:
                pass

            elif view_opt == 3:
                pass
            
            elif view_opt == 4:
                continue
        elif opt == 5:
            break