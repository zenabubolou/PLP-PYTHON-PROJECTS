def create_integer_list():
    integer_list = []
    while True:
            user_input = input("Enter an integer (or type 'done' to finish): ")
            if user_input.lower() == 'done':
                break
            integer = int(user_input)
            integer_list.append(integer)
    return integer_list

if __name__ == "__main__":
    print("Enter integers to create a list. Type 'done' when finished.")
    integers = create_integer_list()
    print("Integer list:", integers)

sum_integer_list = 0
for integer in integers:
    sum_integer_list += integer
print(sum_integer_list)
