#env!/usr/bin/env python3

#mad libs game
#story_template contains placeholders like 'adjective', 'noun', 'verb'
with open("story_template.txt", "r") as file:
    story_template = file.read()#call on the file to read
    
#prompt user for input words 
abjective = input("Enter an adjective: ")
Noun = input("Enter a noun: ")
Verb = input("Enter a verb: ")

mad_lib = story_template.format(adjective=abjective,noun=Noun,verb=Verb)

print(mad_lib)
