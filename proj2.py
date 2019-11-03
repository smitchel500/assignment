# proj2.py
# Assignment #2
# CMSC 291, Fall 2019

import cashRegister

ONES = 0
FIVES = 1
TENS = 2
TWENTIES = 3
options = ['A', 'R', 'T', 'L', 'U', 'S', 'C']

def open_store(register1, register2):
    # get initial amount to put into registers
    print("Good morning! Initializing registers:")
    money = get_bills()

    # Unlock both registers and initialize contents
    register1.unlock()
    register1.add_money(money)
    register2.unlock()
    register2.add_money(money)

def add_money():
    register_num = which_register()
    money = get_bills()
    if register_num == 1:
        register1.add_money(money)
    else:
        register2.add_money(money)

def remove_money():
    register_num = which_register()
    money = get_bills()
    if register_num == 1:
        register1.remove_money(money)
    else:
        register2.remove_money(money)

def transfer_money():

    print("Enter register to transfer money from.")
    register_num = which_register()
    money = get_bills()
    if register_num == 1:
        register1.transfer_money(register2, money)
    else:
        register2.transfer_money(register1, money)

def lock():
    if which_register() == 1:
        register1.lock()
    else:
        register2.lock()

def unlock():
    if which_register() == 1:
        register1.unlock()
    else:
        register2.unlock()

def status():
    if which_register() == 1:
        print(register1.status())
    else:
        print(register2.status())

def close_store(register1, register2):

    # Remove money from the registers
    amount1 = register1.clear_register()
    amount2 = register2.clear_register()

    # Display total amount removed
    print("Total amount removed: $" + str(amount1 + amount2))

    # Lock the registers
    register1.lock()
    register2.lock()

    # Display register states
    print("\nRegister 1\n" + register1.status())
    print("\nRegister 2\n" + register2.status())

    # Exit program
    print("\nGoodnight!")

def display_menu():
    print()
    print("Menu Options:")
    print("  A - Add money")
    print("  R - Remove money")
    print("  T - Transfer money")
    print("  L - Lock register")
    print("  U - Unlock register")
    print("  S - Display register state")
    print("  C - Close the store and quit")
    print()

def get_menu_option():
    option = input("Enter option (A, R, T, L, U, S, C): ")
    while option.upper() not in options:
        print("Invalid option")
        option = input("Enter option (A, R, T, L, U, S, C): ")

    return option.upper()

def which_register():
    register_num = 0
    done = False
    while not done:
        register_num = int(input("Register number (1 or 2)?: "))
        print()
        if register_num != 1 and register_num != 2:
            print("Invalid register number.")
        else:
            done = True

    return (register_num)

def get_bills():
    money = []

    ones = int(input("Number of 1s: "))
    while ones < 0:
        print("Quantity must be >= 0")
        ones = int(input("Number of 1s: "))
    fives = int(input("Number of 5s: "))
    while fives < 0:
        print("Quantity must be >= 0")
        fives = int(input("Number of 5s: "))
    tens = int(input("Number of 10s: "))
    while tens < 0:
        print("Quantity must be >= 0")
        tens = int(input("Number of 10s: "))
    twenties = int(input("Number of 20s: "))
    while twenties < 0:
        print("Quantity must be >= 0")
        twenties = int(input("Number of 20s: "))

    money.append(ones)
    money.append(fives)
    money.append(tens)
    money.append(twenties)

    return money

if __name__ == '__main__':
    # Open store
    register1 = cashRegister.CashRegister()
    register2 = cashRegister.CashRegister()
    open_store(register1, register2)

    option = 'START'
    while option != 'C':
        # Display menu
        display_menu()
        # Get menu option
        option = get_menu_option()

        # Process menu option
        if option == 'A':  # Add money
            add_money()
        elif option == 'R':  # Remove money
            remove_money()
        elif option == 'T':  # Transfer money
            transfer_money()
        elif option == 'L':  # Lock register:
            lock()
        elif option == 'U':  # Unlock register
            unlock()
        elif option == 'S':  # Display register state
            status()
        elif option == 'C':  # Close store and quit program
            close_store(register1, register2)
