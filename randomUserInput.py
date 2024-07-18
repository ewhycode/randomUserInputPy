import random

def get_user_input():
    """
    Prompt the user to enter their name and a range of numbers.
    Returns:
        tuple: A tuple containing the user's name, the start of the range, and the end of the range.
    """
    name = input("Enter your name: ")
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    return name, start, end

def randomize_number(start, end):
    """
    Generate a random number within the given range.
    Args:
        start (int): The start of the range.
        end (int): The end of the range.
    Returns:
        int: A random number within the specified range.
    """
    return random.randint(start, end)

def main():
    """
    The main function to execute the script.
    It gets user input, generates a random number, and prints the result.
    """
    name, start, end = get_user_input()  # Get input from the user
    random_number = randomize_number(start, end)  # Generate a random number
    print(f"Hello {name}, your random number between {start} and {end} is: {random_number}")  # Print the result

if __name__ == "__main__":
    main()  # Execute the main function if the script is run directly
