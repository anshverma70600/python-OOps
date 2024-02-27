# operator overloading 
# print(1+3)
# print("Ansh "+"Verma")
# print([1,2,4]+[7,6,8,3,2])

# 
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def solve(self):
        print(self.real,"i +",self.img,"j")

c1 = Complex(2,4)    
c1.solve()    