"""Create a program that stores a list of words. Then, use list comprehension to create a new\n
 list that contains only the words that have an odd number of characters."""

def list_of_words():
    word_list = []
    while True:
        user_input = input("enter a or words (or type 'done' to finish: )")
        if user_input.lower() == 'done':
            break
        word_list.append(user_input)
    return word_list
   


list_of_word = list_of_words()
print(list_of_word)
#i use list comprehension to return the list of new word
new_word_list = [word for word in list_of_word if len(word) % 2 != 0]
print(new_word_list)


        
