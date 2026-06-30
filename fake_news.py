
#  Using python to create a fake news headline generator 

# 1 - import the random modules
import random
# 2 - create a subjects
subjects= [
    "Prime minister modi",
    "virat kohali",
    "Pankaj udas",
    "A group of monkey",
    "Ola car driver in uttar pradesh",
    "Amit shah",
    "A collage professor"
]

actions = [
    "eats",
    "dancing with",
    "declares war on",
    "launches",
    "cancels",
    "orders",
    "celebrates"
]

places_or_things = [
    "in delhi metro",
    "at tajmahel",
    "a plate of maggi",
    "during IPL match",
    "at manikarnika ghat",
    "inside parliament",
    "a red fort"
]

# 3 - start the headline generation loop
while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    place_or_thing=random.choice(places_or_things)

    headline = f" BREAKING NEWS: {subject} {action} {place_or_thing} "
    print("\n"+ headline)


    ayush_input = input("\n Do you want another headline? (yes/no)").strip().lower()
    if ayush_input == "no":
        break 


# print goodbye message
print("\n Thank you for using the fake news headline generator. have a fun day")
