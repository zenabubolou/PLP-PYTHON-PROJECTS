"""Write a program that accepts user input to create two sets of integers. Then, create a new set \n
that contains only the elements that are common to both sets."""


def create_integer_set():
    integer_set = set()
    while True:
        user_input = input("enter an integer (or type 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        integer = int(user_input)
        integer_set.add(integer)
    return integer_set


set1 = create_integer_set()
print(set1)
set2 = create_integer_set()
print(set2)
new_set = set1.intersection(set2)
print(new_set)
     




