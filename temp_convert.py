#!/usr/bin/env python3

# Created by: Hertz Antonella
# Created on: May, 6, 2022.
# This program asks the user to enter a temperature in celsius.and
# converts it to the fahrenheit using a function.


def calculate_farenheit():
    # get celsius from the user
    user_cel = input("Enter the temperature(°C): ")
    print("")

    try:
        # convert user_cel into a float.
        user_cel = float(user_cel)

        # calculates and displays the celsius is equal in fahrenheit.
        farenheit_temp = (9 / 5) * user_cel + 32
        print("{}°C is equal to {:,.2f}°F.".format(user_cel, farenheit_temp))

    # handles error case.
    except Exception:
        print("Invalid celsius value.Please enter numbers.")


def main():
    # calls function
    calculate_farenheit()


if __name__ == "__main__":
    main()
