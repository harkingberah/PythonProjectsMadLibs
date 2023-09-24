name = input("Enter a name: ")
adjective = input("Enter an adjective: ")
verb =  input("Enter a verb: ")
place = input("Enter a place: ")

gender = input("Enter a gender: ")
gender2 = ""
if (gender == "male" or gender == "m" or gender == "M" or gender == "Male"):
    gender = "boy"
    gender2 = "He"
elif (gender == "female" or gender == "Female" or gender == "f" or gender == "F"):
    gender = "girl"
    gender2 = "She"
    
story = ("In a town, there was a "+ gender + " named " + name + ". " + gender2 + "\nlikes to "+ verb +" " + gender + " who likes to go to "+ place + ". He also had a "+ adjective + " pet." )
print(story)