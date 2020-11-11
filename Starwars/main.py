
input = input("Enter name: ")

def relation_to_luke(name):
    persons = ["Darth Vader", "Leia", "Han", "R2D2"]
    relations = ["father", "sister", "brother in law", "droid"]
    for i in range(len(persons)):
        if name == persons[i]:
            print(f"Luke, I am your {relations[i]}")

relation_to_luke(input)