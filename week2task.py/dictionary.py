"""Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary.\\n
 Then, print the dictionary to the console."""

def Personnal_Infor():
    dict = {}
    dict["name"] = input("Enter your name: ")
    dict["age"] = input("Enter your age: ")
    dict["favourite_color"] = input("Enter your favourite_color: ")
    return dict


Person = Personnal_Infor()
print("person")
for key, value in Person.items():
    print(key, value)
