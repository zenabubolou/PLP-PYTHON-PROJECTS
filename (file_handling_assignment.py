with open("my_file.txt", "w") as file:
    file.write("I am happy.\n")
    file.write("2345\n")
    file.write("I will be there by 5pm.\n")


# Reading from the file and displaying contents
with open("my_file.txt", "r") as file:
    contents = file.read()
    print(contents)

#appending to file
with open("my_file.txt", "a") as file:
    file.write("I at your gate, waiting.\n")
    file.write("Open and come in.\n")
    file.write("your are welcome to my home.\n")


try:
    with open("my_file.txt", "w") as file:
      file.write("I am happy.\n")
      file.write("2345\n")
      file.write("I will be there by 5pm.\n")


    # Reading from the file and displaying contents
    with open("my_file.txt", "r") as file:
      contents = file.read()
      print(contents)

     #appending to file
    with open("my_file.txt", "a") as file:
      file.write("I at your gate, waiting.\n")
      file.write("Open and come in.\n")
      file.write("your are welcome to my home.\n")

except FileNotFoundError:
   print("file not found")

except PermissionError:
   print("Permission denied to accesss the file. ")

finally:
   print("Execution completed.")



