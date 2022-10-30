"""
Number of occurence of characters in a string
"""

# character mapping {character: character_count}
character = {
    "a":0,
    "b":0,
    "c":0,
    "d":0,
    "e":0,
    "f":0,
    "g":0,
    "h":0,
    "i":0,
    "j":0,
    "k":0,
    "l":0,
    "m":0,
    "n":0,
    "o":0,
    "p":0,
    "q":0,
    "r":0,
    "s":0,
    "t":0,
    "u":0,
    "v":0,
    "w":0,
    "x":0,
    "y":0,
    "z":0
}

# list of characters to consider
character_list = character.keys()

input_string = "aayush is my name"

# iterate over input string
for char in input_string:
    if char in character_list:
        character[char] += 1
    else:
        continue

occurence_count = list(character.values())
occurence_count.sort()
highest_occurence = occurence_count[-1] # highest occurence character

# find the character corresponding to highest occurence
for key,value in character.items():
    if value == highest_occurence:
        print(key)
