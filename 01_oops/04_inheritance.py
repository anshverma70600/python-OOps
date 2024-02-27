class Car:
    color = "White"
    @staticmethod
    def start():
        print("Car started ... ")
    @staticmethod
    def stop():
        print("Car stopped ...")

class Tata(Car):
    def __init__(self, brand):
        self.name = brand
    
class Tiago(Tata):
    def __init__(self, type):
        self.type = type
        

c1 = Tiago("Petrol")
print(c1.type)
c1.start()