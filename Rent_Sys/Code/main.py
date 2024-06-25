
from read import available_land
from operation import  return_land
from operation import rent_land

# the main running section of the program
def main():
    while True:
        print("\n===========================================")
        print("      Welcome to Land Management System")
        print("===========================================") 
        print("1. View all Available and Non-Available Lands")
        print("2. Rent a Land")
        print("3. Return a Rented Land")
        print("4. Exit\n")
        print("===========================================\n")
        try:
            user_choice = input("Enter your choice: ")
            if user_choice == "":
                raise ValueError
            user_choice = int(user_choice)
            if user_choice < 0 or user_choice > 9:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a single digit positive number only.")
            continue
        if (user_choice == 1):
            available_land('Land_field.txt')
        elif (user_choice == 2):
            rent_land()

        elif (user_choice == 3):
            return_land()
        elif (user_choice)== 4:
            break   # Exit the program
        else:
            print("Invalid choice please enter numbers correctly")
        print("Do you want to perform another operation?")
        print("1. Yes")
        print("2. No")
        user_choice = input("Enter your choice: ")
        if user_choice == "2":
            break # Exit the program
main()          



