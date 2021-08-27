#Q1) Create three variables in a single line and assign values to them in such a manner that #each one of them belongs to a different data type.
a , b, c = 'shweta', 24, True




#Q2) Create a variable of type complex and swap it with another variable of type integer.
a = 10 + 4j
b = 10
a, b = b, a




#Q3) Swap two numbers using a third variable and do the same task without using any third #variable.
#With 3 variables-
a = 10
b= 20
temp = a
a=b
b = temp

#With 2 variables-
a= 10
b= 20
a, b = b, a




#Q4) Write a program that takes input from the user and prints it using both Python 2.x and #Python 3.x Version.
inp = input(“Please enter you name:”)
print (inp) #Python 3
print inp # Python 2




#Q5) Write a program to complete the task given below:
#Ask users to enter any 2 numbers in between 1-10 , add the two numbers and keep the #sum in another variable called z. Add 30 to z and store the output in variable result and #print result as the final output.
num1 = int(input('1st Num:'))
num2 = int(input('2ns Num:'))
if (num1 and num2) in range(1, 11):
    z = num1 +num2
    result = z + 30
    print(result)
else:
    print("Both number should be in range of 1 to 10")




#Q6) Write a program to check the data type of the entered values.
#HINT: Printed output should say - The data type of the input value is : int/float/string/etc
check = eval(input(“Enter a data to check: ”))
print(type(check))




#Q7) Create Variables using formats such as Upper CamelCase, Lower CamelCase, #SnakeCase and UPPERCASE.
sentence = "i love Python"
sentence1 =list(sentence.split(" "))

UpperCamel="".join(sentence1[0].capitalize()+sentence1[1].capitalize()+sentence1[2] .capitalize())
LowerCamel="".join(sentence1[0].lower()+sentence1[1].capitalize()+sentence1[2] .capitalize())
SnakeCase = sentence.replace(" ", "_").lower()
UpperCase = sentence.upper()

print("Upper Camel Case: ",UpperCamel )
print("Lower Camel Case: ",LowerCamel)
print("Snake Case: ",SnakeCase)
print("Upper Case: ",UpperCase)




#Q8) If one data type value is assigned to ‘a’ variable and then a different data type value #is assigned to ‘a’ again. Will it change the value? If Yes then Why?


#Yes, it will change because Python is dynamically typed language. Dynamically typed language means if once a variable is assigned then it can be changed
#again. The interpreter assigns variable type at the run time based on the data type and value at that time.
