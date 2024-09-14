
def float_input(text : str):
    """
    Get input.
    
    Gets float incase user wants to be specific

    If it is not an float, then it asks for input again.
    """
    while True:
        inp : str = input(text)
        try:
            inp : float = float(inp)
        # except with only ValueError so Keyboard Interupts like Ctrl+C do not get caught
        except ValueError:
            print("Input value must be an int")
            continue
        return inp

def average_age():
    # Get User Input
    friend_1 : float = float_input("Friend 1 age: ")
    friend_2 : float = float_input("Friend 2 age: ")
    friend_3 : float = float_input("Friend 3 age: ")
    friend_4 : float = float_input("Friend 4 age: ")
    friend_5 : float = float_input("Friend 5 age: ")

    # Sum ages
    friend_ages_summed : float = friend_1 + friend_2 + friend_3 + friend_4 + friend_5

    # Average the ages
    friend_age_average : float = friend_ages_summed / 5
    
    # Print the results
    # '.2f' rounds integer to 2 decimal places, to account for floating point precision errors
    print(f"The average friend age is: {friend_age_average:.2f}")

# Line which calls the above function.
average_age()