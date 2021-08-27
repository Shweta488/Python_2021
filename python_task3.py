#Q1) Create a list of 10 elements of four different data types like int, string, complex and #float.
l1 = ['Shweta', 20, 3.6, True, 'Python', 10+1j, 70, 'mylist', False, 3.1423457878]




#Q2) Create a list of size 5 and execute the slicing structure
l1 = ['Shweta', 20, 3.6, True, 'Python']
print(l1[2:], '\n', l1[:], '\n',l1[:4],'\n', l1[-1], '\n',l1[::-1],'\n', l1[::2])




#Q3) Write a program to get the sum and multiply of all the items in a given list.
l1 = [1, 2, 3, 4]
add = 0
mul = 1
for num in l1:
    add += num
    mul *= num

print(add)
print(mul)




#Q4) Find the largest and smallest number from a given list.
l1=[18,52,23,5, 84]
print(max(l1))
print(min(l1))




#Q5) Create a new list which contains the specified numbers after removing the even #numbers from a predefined list.
l1=[18,52,23,5, 84,97,26,7,63]
odd = [ ]
for num in l1:
    if num%2 == 0:
        continue
    else:
        odd.append(num)

print(odd)




 #Q6) Create a list of elements such that it contains the squares of the first and last 5 #elements between 1 and30 (both included).
sqr = [ ]
for num in range(1, 6):
    sqr.append(num**2)
for num in range(25, 31):
    sqr.append(num**2)

print(sqr)




#Q7) Write a program to replace the last element in a list with another list.
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1[-1:] = l2
print(l1)




#Q8) Create a new dictionary by concatenating the following two dictionaries:
a={1:10,2:20}
b={3:30,4:40}
c = {}
for d in (a, b):
    c.update(d)

print(c)




#Q9) Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values #between 1 and n(both 1 and n included).
n = int(input("Enter a number: "))
d = dict()
for x in range(1,n+1):
    d[x]=x*x

print(d)




#Q10) Write a program which accepts a sequence of comma-separated numbers from #console and generates a list and a tuple which contains every number in the form of string.
num = input("Enter you numbers: ")
num1 = num.split(',')
print(num1)
print(tuple(num1))
