###############################################################################
# DONE: 1. (3 pts)
#
#   Write a function called color_picker() that prints out a message to a user.
#
#   This function should do the following:
#     1. Prompt the user to enter the name of a color.
#     2. Using case statements, if it matches the color that they picked, it should print out a success message like so:
#           "Success! You picked red."
#        Do NOT use f-strings here. Just use regular strings and use the case statement to pick which string to print.
#     3. You should have a case for at least 5 colors of your choosing.
#     3. If the user picks a color that you do not have a case for, it should print:
#           "Unknown Color!"
#
#   Make sure you call your function to start things off.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

def color_picker():
    color = input("Enter a color: ")
    match color:
        case "red":
            print("Success! You picked red.")
        case "orange":
            print("Success! You picked orange.")
        case "yellow":
            print("Success! You picked yellow.")
        case "green":
            print("Success! You picked green.")
        case "blue":
            print("Success! You picked blue.")
        case "purple":
            print("Success! You picked purple.")
        case "pink":
            print("Success! You picked pink.")
        case "grey":
            print("Success! You picked grey.")
        case _:
            print("Unknown color.")

color_picker()

###############################################################################
# TODO: 2. (3 pts)
#
#   Write a function called grade() that tells a student what letter grade they
#   got on an assignment based on the percentage they indicate.
#
#   This function should do the following:
#     1. Prompt the user to enter a percentage. They should enter the
#        percentage as a decimal (so an 85% should be entered as 0.85)
#     2. Using case statements, check which range the percentage is in and print a statement telling the user what grade they got on the assignment. It should look something like:
#           "You received a(n) A."
#     3. Your ranges should match a standard grading scale where greater than or equal to 90% is an A, etc.
#     4. If the user enters an invalid percentage, the function should print:
#           "Invalid Score!"
#
#   Make sure you call your function to start things off.
#
#   Once you have done this, then change the above _TODO_ to DONE.
##############################################################################

def grade():
    gradevalue = float(input("Enter your grade as a decimal value between 0-1: "))
    match gradevalue:
        case _ if 0.9 <= gradevalue <= 1:
            print("You received an A.")
        case _ if 0.8 <= gradevalue <= .89:
            print("You received a B.")
        case _ if 0.7 <= gradevalue <= 0.79:
            print("You received a C.")
        case _ if 0.6 <= gradevalue <= 0.69:
            print("You received a D.")
        case _:
            print("You received an F.")

grade()