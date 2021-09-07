#Q1) Write a program that calculates and prints the value according to the given formula: Q= Square root of [(2*C*D)/H]

import math
class Formula:
    def __init__(self):
        self.c = 50
        self.h = 30
        self.d = int(input("Enter your value: "))

    def calculate(self):
        result = math.sqrt((2*self.c*self.d)/self.h)
        print(result)

ob = Formula()
ob.calculate()




#Q2) Define a class named Shape and its subclass Square. The Square class has an init function which takes length as argument. Both classes have an area function which can print the area of the shape where Shape’s area is 0 by default.

class Shape:
    def __init__(self, length):
        self.length = length
        area = 0
        print(area)

class Square(Shape):
    def calculate(self):
        area = self.length ** 2
        print(area)

ob1 = Shape(4)
ob2 = Square(4)
ob2.calculate()




#Q3) Create a class to find three elements that sum to zero from a set of n real numbers

class SumToZero:
    def __init__(self, list1):
        self.x = list1
        self.l = []

    def sum(self):
        n = len(self.x)
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j + 1, n):
                    if self.x[i] +self.x[j] + self.x[k] == 0:
                        result = [self.x[i], self.x[j], self.x[k]]
                        self.l.append(result)
        print(self.l)

obj = SumToZero([-25,-10,-7,-3,2,4,8,10])
obj.sum()




#Q4) Create a Time class and initialize it with hours and minutes.

class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, hrs, mins):
        self.hrs = hrs
        self.mins = mins
        self.hrs += self.hours
        self.mins += self.minutes
        if self.mins >= 60:
            self.hrs += 1
            self.mins -= 60

        return self.hrs, self.mins

    def displayTime(self):
        print(f"{self.hrs} hours and {self.mins} minutes")

    def displayMinutes(self, hour, minute):
        self.hrs = hour
        self.mins = minute
        total = 0
        if self.hrs >0:
            total += self.hrs*60
            total += self.mins

        print(f"{total} minutes")


ob1 = Time(2, 50)
ob1.addTime(1, 20)
ob1.displayTime()
ob1.displayMinutes(1,2)




#Q5) 5. Write a Person class with an instance variable “age” and a constructor that takes an integer as a
#parameter. The constructor must assign the integer value to the age variable after confirming the
#argument passed is not negative; if a negative argument is passed then the constructor should set
#age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance
#methods:

class Person:
    def __init__(self, age):
        if age > 0:
            self.age = age
        else:
            self.age = 0
            print (“Age is not valid, setting age to 0”)

    def yearPasses(self, yrs):
        result = self.age + yrs
        print(result)

    def amIOld(self):
        if self.age>=0 and self.age < 13:
            print("You Are Young!")
        elif self.age >= 13 and self.age <= 19:
            print("You Are A Teenager!")
        else:
            print("You Are Old!")

ob = Person(-1)
ob.yearPasses(4)
ob.amIOld()
