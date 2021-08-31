#Q1) Write a program in Python to allow the error of syntax to be handled using exception handling.

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    sum = num1 + num2
    print(sum)

except:
    print("Error Found !!")




#Q2) Write a program in Python to allow the user to open a file by using the argv module. If the entered name is incorrect throw an exception and ask them to enter the name again. Make sure to use read only mode.

import sys

try:
    with open(sys.argv[1], 'r') as my_file:
        print(my_file.read())
except:
    print("Error opening file. Please the name of the file.")



#Q3)Write a program to handle an error if the user entered a number more than four digits it should return “The length is too short/long !!! Please provide only four digits”

try:
    num = int(input("Please enter a number: "))
except Exception:
    print("Uh Oh! Please enter an integer")

finally:

    temp = num
    count = 0
    while num > 0:
        digit = num % 10
        count += 1
        num = num//10

    if count > 4:
        print(“The length is too long !!! Please provide only four digits”)
    else:
       print(f"Your number is: {temp}")




#Q4)Create a login page backend to ask users to enter the username and password. Make sure to ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it should not be more than 3 times.

username = input("User name: ")
password1 = input("Password: ")
password2 = input("Re-enter your password: ")
count = 1
while count < 3:
    count += 1
    if password1 == password2:
        print("Access Granted !")
        break
    else:
        print("Incorrect Password.")
        password2 = input("Re-enter your password: ")

    print("Access Denied")




#Q5) Read doc.txt file using Python File handling concept and return only the even length string from the file. Consider the content of doc.txt as given below:

try:
    f = open("doc.txt", 'r')
    content = f.read()
    f_list = content.split(" ")
    print(f_list)
    for words in f_list:
        if len(words) % 2 == 0:
            print(words)

except:
    print("Error while opening file")

finally:
    f.close()
