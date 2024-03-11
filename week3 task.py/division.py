"""Create a function that determines whether or not a number is divisible by ten. A number is divisible by \n
ten if the remainder of the number divided by 10 is 0. """
def divisible_by_10(num):
    result = num % 10
    if result == 0:
        return True
    else:
        return False
    

value = divisible_by_10(20)
print(value)