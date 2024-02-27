# Methods are function that belongs to Object

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print("Welcome to class,", self.name)
    
#     def marks_get(self):
#         return self.marks

# s1 = Student("Ansh", 90)
# s1.welcome()
# print(s1.marks_get())

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    @staticmethod
    def hello():
        print("here i have used static method by decorator -->")
        
    def get_avg(self):
        ans = 0
        for i in self.marks:
            ans += i
        print("Hey, ", self.name, "avg of your marks are", ans/3)


s1 = Student("Ansh", [98,96,97])
print(s1.name, "your marks are",s1.marks)
s1.get_avg()
s1.hello()