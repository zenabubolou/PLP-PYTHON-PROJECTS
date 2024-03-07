""""
Create an empty list called my_list.
Append the following elements to my_list: 10, 20, 30, 40.
Insert the value 15 at the second position in the list.
Extend my_list with another list: [50, 60, 70].
Remove the last element from my_list.
Sort my_list in ascending order.
Find and print the index of the value 30 in my_list.
"""

value = 30
my_list = []
input_list = [10, 20, 30, 40]
for items in input_list:
    my_list.append(items)

#appending 15 at position 2
my_list.insert(2, 15)
second_list = [50, 60, 70]
my_list.extend(second_list) #returns a new list [10, 20, 15, 30, 40, 50, 60, 70]
my_list.pop() #removes the last number in the list
my_list.sort()
for number in my_list:
    if number == value:
        index = my_list.index(number)
        break
print(index)