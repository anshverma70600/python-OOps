# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("Car start")
# c1 = Car()
# c1.start()

# ques-->

# class Account:
#     def __init__(self, balance, acc_no):
#         self.balance = balance
#         self.acc_no = acc_no

    
#     def credit(self, amt):
#         self.balance += amt
#         print(amt, "Credited")
#         print("total", self.bal())

#     def debit(self, amt):
#         self.balance -= amt
#         print(amt, "Debited")
#         print("total", self.bal())

#     def bal(self):
#         return self.balance


# a1 = Account(9000, 657894973)
# a1.debit(1000)
# a1.credit(500)

class Account:
    def __init__(self, acc_no, acc_pwd):
        self.no = acc_no
        self.__pwd = acc_pwd

a1 = Account(123443,"afe198327")
print(a1.no)
print(a1.__pwd)