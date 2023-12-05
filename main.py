"""
This module contains utility functions for calculating.

Author: Maryam Alavi
"""


def add():
    """This is for adding two numbers."""
    answer = float(first_number) + float(second_number)
    print(str(first_number) + " + " + str(second_number) + " = " + str(answer))


def sub():
    """This is for subbing two numbers."""
    answer = float(first_number) - float(second_number)
    print(str(first_number) + " - " + str(second_number) + " = " + str(answer))


def mul():
    """This is for multiplying two numbers."""
    answer = float(first_number) * float(second_number)
    print(str(first_number) + " * " + str(second_number) + " = " + str(answer))


def div():
    """his is for diving two numbers."""
    answer = float(first_number) / float(second_number)
    print(str(first_number) + " / " + str(second_number) + " = " + str(answer))


def rem():
    """This is for remaining two numbers."""
    answer = float(first_number) % float(second_number)
    print(str(first_number) + " %" + str(second_number) + " = " + str(answer))


def pow():
    """This is for powering two numbers"""
    answer = float(first_number) ** float(second_number)
    print(str(first_number) + " ** " + str(second_number) + " = " + str(answer))


print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Divided")
print("F. Remainder")
print("P. Power")

choice = input("input your choice: ")
if choice in ("a", "A"):
    first_number = input("input the first number:")
    second_number = input("input the second number:")
    print("Addition")
    add()


elif choice in ("b", "B"):
    first_number = input("input the first number:")
    second_number = input("input the second number:")
    print("Subtraction")
    sub()

elif choice in ("c", "C"):
    first_number = input("input the first number:")
    second_number = input("input the second number:")
    print("Multiplication")
    mul()

elif choice in ("d", "D"):
    first_number = input("input the first number:")
    second_number = input("input the second number:")
    print("Divided")
    div()

elif choice in ("f", "F"):
    first_number = input("input the first number:")
    second_number = input("input the second number:")
    print("Remainder")
    rem()

elif choice in ("p", "P"):
    first_number = input("input the first number:")
    second_number = input("input the second number:")
    print("Power")
    pow()
