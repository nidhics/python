# print("hello")
# print(2+3)
# print ("at last")
# print("o")
# print("hi")
# from random import shuffle

# arr=[34,343,5456,65,76878,99,425]
# shuffle(arr)
# print(arr)
# print(arr.pop())

class Car:

    def __init__(self,type,name, color,price) :
        self.type=type
        self.name=name
        self.color=color
        self.price=price

    def dream_car(self):
        # print(f"One day i will get {self.name}")
        print("One day i will buy {} of {} color".format(self.name,self.color))
        #format( function ) 

    def __add__(self,other):
        return self.type+ " " +other.type

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self,other):
        return self.price > other.price

c1=Car("Electric","Nano","white",300000)
print(dir(c1))#to get all dunder / magic method
c1.dream_car()#One day i will buy Nano of white color
c2=Car("Desiel","Nano","silver",200000)
print(c1+c2)#Electric Desiel
print(c1<c2)#False
print(c1>c2)#True
