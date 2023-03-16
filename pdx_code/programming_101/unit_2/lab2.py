'''After all the jacks are in their boxes
And the clowns have all gone to bed
You can hear happiness staggering on down the street
Footprints dressed in red

And the wind whispers, "Mary."'''

name = input("What is your name? ")

while True:
    bool = input(f"Do you want to play a game, {name}? yes/no ")

    if bool == "yes":
        nouns = input("Give me 3 nouns separated by commas: ")
        noun_list = nouns.split(",")
        color = input("What is your favorite color? ")
        print(f"\n\nAfter all the jacks are in their {noun_list[0].lstrip()}\nAnd the clowns have all gone to {noun_list[1].lstrip()}\nYou can hear happiness staggering on down the {noun_list[2].lstrip()}\nFootprints dressed in {color}\nAnd the wind whispers, \"{name}.\"\n\n")

    if bool == "no":
        print(f"Goodbye, {name}")
        break