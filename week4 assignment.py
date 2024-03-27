class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hi, my name is {self.name}. I am {self.age}yrs old and I am {self.gender}.")

# Creating an instance of the Person class
        
person1 = Person("Jane", 40, "Female")
# Calling the introduce method to display the person's information
person1.introduce()

