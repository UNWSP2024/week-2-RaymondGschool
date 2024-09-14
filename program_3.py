# items in the store
items : dict[str, float] = {"water": 2.31, "milk": 3.50, "chips": 4.25, "chocolate": 1.20, "chicken": 10.99}

def valid_input(text: str):
    """
    Get input.

    Validates whether the input is an item or not.
    """
    while True:
        # lower case to maximize flexability
        inp : str = input(text).lower()
        try:
            inp : float = items[inp]
        # except with only KeyError so Keyboard Interupts like Ctrl+C do not get caught
        except KeyError:
            print("Input value must be a valid item")
            # if invalid re-ask
            continue
        # if valid item then return
        return inp

def calculate_total_purchase():
    # A customer in a store is purchasing five items.  
    # Write a program that asks for each item, 
    # then displays the subtotal of the sale, 
    # the amount of sales tax, and the total.  
    # Assume the sales tax is 7 percent.

    # print all of the available items
    print("Available items: ", end="")
    i : int = 0
    for item_name in items.keys():
        # doesn't put comma before "water"
        if i > 0: print(", ", end="")
        i+=1
        item_price : float = items[item_name]
        print(f"{item_name}: ${item_price}", end="")
    # add linefeed character
    print()

    # get wanted items
    item_1 : float = valid_input("Item 1: ")
    item_2 : float = valid_input("Item 2: ")
    item_3 : float = valid_input("Item 3: ")
    item_4 : float = valid_input("Item 4: ")
    item_5 : float = valid_input("Item 5: ")

    subtotal : float = item_1 + item_2 + item_3 + item_4 + item_5
    sales_tax : float = subtotal * 0.07 # 7% sales tab
    # display totals
    # '.2f' rounds to 2 decimal places
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Sales tax: ${sales_tax:.2f}")
    print(f"Total: ${subtotal + sales_tax:.2f}")

calculate_total_purchase()