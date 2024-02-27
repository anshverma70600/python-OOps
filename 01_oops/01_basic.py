# function --> OOPS
# class --> blue print to make --> objects 

# class Student:    #class
#     name = "Ansh Verma"
#     age = 12

# s1 = Student() #object --> instances of class 
# print(s1.age) 

# class Car:
#     color = "blue"

# car1 = Car()
# print(car1.color)

#Constructor-->. __init__ function
#.  1. default constructor
#.  2. Parameteric constructor

class Car:
    company = "TATA"
    def __init__(self, name): #self is point new object car1
        self.name = name
        print('Have my dream car')
    
car1 = Car("tiago")
print(car1.name)
print(Car.company)


