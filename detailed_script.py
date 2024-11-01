# detailed_script.py
"""
This script demonstrates basic Python functionalities:
- User input
- Conditional statements
- Looping
- Functions
"""

def get_user_input():
    """Function to get user input for their favorite color."""
    # Prompt the user for their favorite color
    color = input("Enter your favorite color: ")
    return color

def check_color(color):
    """Function to check if the entered color is in a predefined list.
    
    Args:
        color (str): The color to check.

    Returns:
        bool: True if the color is in the list, False otherwise.
    """
    # Predefined list of colors
    favorite_colors = ['red', 'blue', 'green', 'yellow', 'purple']
    
    # Check if the user's color is in the list
    if color.lower() in favorite_colors:
        return True
    else:
        return False

def main():
    """Main function to execute the script."""
    # Get user input
    user_color = get_user_input()
    
    # Check if the color is a favorite
    if check_color(user_color):
        print(f"{user_color.capitalize()} is one of my favorite colors too! 🎉")
    else:
        print(f"{user_color.capitalize()} is nice, but I prefer other colors. 😊")
    
    # Loop to ask the user for more colors
    while True:
        more_colors = input("Do you want to check another color? (yes/no): ")
        if more_colors.lower() == 'yes':
            user_color = get_user_input()
            if check_color(user_color):
                print(f"{user_color.capitalize()} is one of my favorite colors too! 🎉")
            else:
                print(f"{user_color.capitalize()} is nice, but I prefer other colors. 😊")
        elif more_colors.lower() == 'no':
            print("Thank you for playing! Goodbye! 👋")
            break
        else:
            print("Please enter 'yes' or 'no'.")

# Check if the script is being run directly
if __name__ == "__main__":
    main()
