"""Create a method that tests whether the result of taking the power of one number to another number\n
 provides an answer which is greater than 5000. We will use a conditional statement to return True if the result\n
 is greater than 5000 or return False if it is not."""

def large_power(base, exponent):
    cal = base ** exponent
    if cal > 5000:
        return True
    else:
        return False
    

result = large_power(20, 2)
print(result)
    