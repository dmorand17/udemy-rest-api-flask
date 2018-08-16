should_continue = True
if should_continue:
    print("Hey buddy")

known_people = ["John","Mary","Anna"]
person = input("Enter the person you know: ")

if person in known_people:
    print("You know {}".format(person))
else:
    print("Sorry I don't know {}".format(person))

def who_do_you_know():
    # Ask the user for a list of people they know
    # Split the string into a list
    # Returns the list
    known_people = input("Enter a list of people you know: ").split()
    return known_people

def ask_user():
    # Ask user for their name
    # See if their name is in the list of known people
    # Print out if they know that person
    person = input("Enter a person you know: ")

    if person in who_do_you_know():
        print("You know {}".format(person))
    else:
        print("Sorry I don't know {}".format(person))
