#Q1) Create a list of given structure and get the Access list as provided below:
x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]

#Access list: [1, 2, 3, 4]
print(x[5][:4])

#Access list: [600, 700]
print(x[6:8])

#Access list: [100, 300, 500, 600, 800]
print(x[0:9:2])

#Access list: [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
print(x[::-1])

#Access list: [10]
print(x[5][5][0])

#Access list: [ ]
del x[:]
print(x)




#Q2)Create a list of thousand numbers using range and xrange and see the difference between each other.
r = range(1, 1000, 1)
a= []
xr = xrange(1, 1000, 1)
b=[]
for r1 in r:
    a.append(r1)
for r2 in r:
    b.append(r2)

#print(a)
#print(b)




#Q3) How Tuple is beneficial as compared to the list?

#Tuples are faster than list.




#Q4) Write a program in Python to iterate through the list of numbers in the range of 1,100 and print the number which is divisible by 3 and is a multiple of 2.

num = list(range(1, 1101))
for i in num:
    if i%2 == 0 and i%3 == 0:
        print(i)




#Q5) Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the string with their index.

s = 'abcdefghijklmnopqrstuv'
sr = s[::-1]
vowels = ['a', 'e', 'i', 'o', 'u']
for i in range(len(sr)):
    if s[i] in vowels:
        print(f'{i} --> {s[i]}')




#Q6) Write a program in Python to iterate through the string “hello my name is abcde” and print the string which is having an even length.

s = “hello my name is abcde”
words = s.split()
string = []
for word in words:
    if len(word)%2 == 0:
        string.append(word)

print(" ".join(string))




#Q7) Write a program in python to print the pair of numbers whose sum is equal to the result number that is let's say 8.

x = [1,2,3,4,5,6,7,8,9,-1]
n = len(x)
for i in range(n-1):
    for j in range(i+1, n):
        if x[i] +x[j] == 8:
            print(f"({x[i]}, {x[j]})")




#Q8) Write a program in Python to complete the following task:

even_list = []
odd_list = []
count = 0
while count < 5:
    num = int(input("Enter a num in range 1 to 50: "))
    if num in range(1, 50):
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
        count += 1
    else:
        print("Please enter in range of 1 to 50")

sum1 = sum(even_list)
sum2 = sum(odd_list)
if sum1 > sum2:
    print(f'{sum1} have maximum sum')
else:
    print(f'{sum2} have maximum sum')




#Q9) Write a program to find out the occurrence of a specific character from an alphanumeric string.

s1 = "12abcbacbaba344ab"
s2 = set(s1)
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for char in s2:
    if char not in num:
        cnt = s1.count(char)
        print(f'{char} = {cnt}')




#Q10) Generate and print another tuple whose values are even numbers in the given tuple

t1 = (1,2,3,4,5,6,7,8,9,10)
t2 = list()
for i in t1:
    if i%2 == 0:
        t2.append(i)

print(tuple(t2))
