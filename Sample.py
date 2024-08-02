# This is a simple Python program that greets the user and checks their voting eligibility.

def greet_user(name, age):
    """
    Function to greet the user and check voting eligibility.
    
    Parameters:
    name (str): The user's name
    age (int): The user's age
    """
    # Greet the user
    print(f"Hello, {name}!")
    
    # Check if the user is eligible to vote
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote yet.")

def main():
    """
    Main function to execute the program.
    """
    # Ask the user for their name
    user_name = input("Enter your name: ")
    
    # Ask the user for their age and ensure it's an integer
    while True:
        try:
            user_age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Please enter a valid number for age.")
    
    # Call the greet_user function with the user's name and age
    greet_user(user_name, user_age)

# Execute the main function
if __name__ == "__main__":
    main()
