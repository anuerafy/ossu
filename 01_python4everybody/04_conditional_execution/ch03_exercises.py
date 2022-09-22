# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours 
# worked above 40 hours.

def exercise_one():
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))

    if hours > 40:
        pay = 40*rate + (hours-40)*rate*1.5
    else:
        pay = hours*rate

    print(f"Pay: {pay}")


# Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input 
# gracefully by printing a message and exiting the program. The following shows two executions of the 
# program:

def exercise_two():
    try:
        hours = float(input("Enter Hours: "))
        rate = float(input("Enter Rate: "))
        
        if hours > 40:
            pay = 40*rate + (hours-40)*rate*1.5
        else:
            pay = hours*rate

        print(f"Pay: {pay}")

    except:
        print("Error, please enter numeric input")


# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. 
# If the score is out of range, print an error message. 
# If the score is between 0.0 and 1.0, print a grade using the following table:

    #  Score   Grade
    # >= 0.9     A
    # >= 0.8     B
    # >= 0.7     C
    # >= 0.6     D
    #  < 0.6     F

def exercise_three():
    try:
        score = float(input("Enter score: "))
        if score > 1 or score < 0:
            print("Out of Range")
        if score < 0.6:
            print("F")
        elif score < 0.7:
            print("D")
        elif score < 0.8:
            print("C")
        elif score < 0.9:
            print("B")
        else:
            print("A")

    except:
        print("Invalid input")
