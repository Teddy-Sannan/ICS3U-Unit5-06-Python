#!/usr/bin/env python3

# Created by: Teddy Sannan
# Created on: November 2019
# This program goes to a certain decimal place

import math


def roundOff(variable):
    # calculates decimal place
    variable[0] = variable[0] * 10**variable[1] + 0.5
    variable[0] = int(variable[0])
    variable[0] = float(variable[0])
    variable[0] = variable[0]/(10**variable[1])


def main():
    # calls other functions and get inputs
    variable = []
    while True:
        number_string = input("Enter the number you would like to round: ")
        decimal_string = input("Enter the decimals you would like to have: ")
        print()

        try:
            number = float(number_string)
            decimal = int(decimal_string)

            variable.append(number)
            variable.append(decimal)

            roundOff(variable)

            print(variable[0])
            break

        except(ValueError):
            print("Not a valid number inputted")
            print()
            continue

        else:
            break


if __name__ == "__main__":
    main()