# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# AGibbs,24MAY2020, Modified code to complete assignment 6, Used functions to clean code. Added else if user does
# choose from menu
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "C:\_PythonClass\Assignment06\ToDoFile.txt"  # The name of the data file
objFile = None  # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
list_of_rows = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions
strRemove = "" # Capture Task to be removed


# Processing  --------------------------------------------------------------- #
class Processor:

    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(strFileName, list_of_rows):
        """ Reads data from a file into a list of dictionary rows
            :param strFileName: (string) with name of file:
            :param list_of_rows: (list) you want filled with file data:
            :return: list_of_rows: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(strFileName, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(strTask, strPriority, list_of_rows):
        """ Adds data to list of dictionary rows
            :param strTask: (string) from user input:
            :param strPrioity: (string) from user input:
            :param list_of_rows: (list) you want appended with file data:
            :return: list_of_rows: (list) of dictionary rows
        """
        row = {'Task': strTask, 'Priority':strPriority}
        list_of_rows.append(row)  # appends lstTable with new entries
        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(strRemove, list_of_rows):
        """ removes dictionary row from list of dictionary rows
            :param strRemove: (string) from user input:
            :param list_of_rows: (list) you want appended with file data:
            :return: list_of_rows: (list) of dictionary rows
        """
        for row in list_of_rows:
            if row['Task'].lower() == strRemove.lower():  # .lower in care user input wrong case
                list_of_rows.remove(row)  # list.remove(element)
        return list_of_rows, 'Success'

    @staticmethod
    def write_data_to_file(strFileName, list_of_rows):
        """ writes list of dictionary rows to .txt file
            :param strFileName: (string) with name of file:
            :param list_of_rows: (list) you want appended with file data:
            :return: list_of_rows: (list) of dictionary rows
        """
        global objFile
        objFile = open(strFileName, 'w')
        for row in list_of_rows:
            objFile.write(row['Task'] + ',' + row['Priority'] + '\n')  # \n important for newline in txt file
        objFile.close()
        return list_of_rows, 'Success'


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """ Gets user input for new task and priority

            :return: strTask, strPriority
        """
        global strTask
        strTask = input("Enter task needed to complete: ")
        global strPriority
        strPriority = (input('Enter priority number from 1(low) to 10(high): '))
        print('Task and Priority added!')
        return strTask, strPriority

    @staticmethod
    def input_task_to_remove():
        """ Gets user input for task to remove

            :return: strRemove
        """
        print('Task  (Priority)')
        for row in list_of_rows:
            print(row['Task'] + "(" + row['Priority'] + ")")
        global strRemove
        strRemove = input('Type in the Task you want to remove: ')
        print('Task (' + strRemove + ') removed from list')
        return strRemove


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, list_of_rows)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(list_of_rows)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        IO.input_new_task_and_priority()
        Processor.add_data_to_list(strTask, strPriority, list_of_rows)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        IO.input_task_to_remove()
        Processor.remove_data_from_list(strRemove, list_of_rows)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            Processor.write_data_to_file(strFileName, list_of_rows)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            Processor.read_data_from_file(strFileName, list_of_rows)
            IO.print_current_Tasks_in_list(list_of_rows)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        print("Goodbye!")
        break  # and Exit
    else:
        print('Please select only from the menu of options')  # in case user makes a choice other than 1,2,3,4,5

