#Q1) Write a program to reverse a string.
s = “1234abcd”
print(s[::-1])




#Q2) Write a function that accepts a string and prints the number of uppercase letters and #lowercase letters.
def count(s):
    upper = 0
    lower = 0
    for i in s:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
    print(f"No. of Uppercase characters : {upper} No. of Lower case Characters : {lower}")

count(“abcSdefPghijQkl”)




#Q3) Create a function that takes a list and returns a new list with unique elements of the first list.
def unique(l1):
    l2 = list(set(l1))
    return(l2)

print(unique([1, 2, 5, 2, 7, 10, 7, 1]))




#Q4) Write a program that accepts a hyphen-separated sequence of words as input and #prints the words in a hyphen-separated sequence after sorting them alphabetically.
seq = input("Enter your sequence of words: ")
seq1 = seq.split('-')
seq1.sort()
print("-".join(seq1))





#Q5) Write a program that accepts a sequence of lines as input and prints the lines after #making all characters in the sentence capitalized.
sentence = input("Enter a sentence: ")
print(sentence.upper())




#Q6) Define a function that can receive two integral numbers in string form and compute #their sum and print it in the console.
def sum(a, b):
    print(int(a) + int(b))

num1 = "12"
num2 = "2"
sum(num1, num2)




#Q7) Define a function that can accept two strings as input and print the string with the #maximum length in the console. If two strings have the same length, then the function #should print both the strings line by line.
def length(str1, str2):
    if len(str1) > len(str2):
        print(f'{str1} has maximum length')
    elif len(str1) < len(str2):
        print(f'{str2} has maximum length')
    elif len(str1) == len(str2):
        print(f'{str1} is the first string')
        print(f'{str2} is the second string')

length('abc' , 'pqrs')




#Q8) Define a function which can generate and print a tuple where the values are square of #numbers between 1 and 20 (both 1 and 20 included).
def sqr():
    l=[]
    for num in range(1, 21):
        l.append(num**2)

    print(tuple(l))

sqr()




#Q9) Write a function called showNumbers that takes a parameter called limit. It should print #all the numbers between 0 and limit with a label to identify the even and odd numbers.
def showNumbers(limit):
    for num in range(0, limit+1):
        if num % 2 == 0:
            print(f'{num} EVEN')
        else:
            print(f'{num} ODD')

showNumbers(3)




#Q10) Write a program which uses filter() to make a list whose elements are even numbers #between 1 and 20 (both included)
result = filter(lambda x: x%2 == 0, range(1, 21))
print(list(result))




#Q11) Write a program which uses map() and filter() to make a list whose elements are #squares of even numbers in [1,2,3,4,5,6,7,8,9,10].
l = [1,2,3,4,5,6,7,8,9,10]
result = filter(lambda x: x%2 == 0, l)
result2 = map(lambda x: x**2, result)
print(list(result2))




 #Q12) Write a function to compute 5/0 and use try/except to catch the exceptions
a=5
b=0
try:
    print(a/b)
except Exception:
    print("Error")




#Q13) Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().
from functools import reduce
a = reduce(lambda a,b: 10*a+b, [1,2,3,4,5,6,7])
print(a)




#Q14) Write a program in Python to find the values which are not divisible by 3 but are a #multiple of 7. Make sure to use only higher order functions.
l = [12, 33, 76, 27, 21, 70, 35, 53]
div = filter(lambda x: x%3 != 0 and x%7 == 0, l)
print(list(div))




#Q15) Write a program in Python to multiply the elements of a list by itself using a traditional #function and pass the function to map() to complete the operation.
def mul(l):
    return l**2

l = [1, 2, 3, 4, 5]
result = map(mul, l)
print(list(result))




#Q16)What is the output of the following codes: (i) def foo():

#(i) 2

#(ii)
#after f after f?
#name ‘f’ is not found
