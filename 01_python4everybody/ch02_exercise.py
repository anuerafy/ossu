
# Exercise 2: Write a program that uses input to prompt a user for their name and then welcomes them.
def exercise_two():
    name = input("your name?:")
    print(f"hi, {name}")

exercise_two()


# Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.

    # Enter Hours: 35
    # Enter Rate: 2.75
    # Pay: 96.25

def exercise_three():
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    print(hours*rate)

exercise_three()


#Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, 
# and print out the converted temperature.
# C = (F-32) *5 /9
def exercise_five():
    fahrenheit = float(input("Enter ° Fahrenheit: "))
    print((fahrenheit-32) * 5 / 9)

exercise_five()