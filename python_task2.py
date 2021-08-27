#Q1) Write a program in Python to perform the following operation:
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Consultadd- Python Training")
elif num % 5 == 0:
    print("Python Training")
elif num % 3 == 0:
    print("Consultadd")
else:
    print("Please enter a number again")




#Q2) Write a program in Python to perform the following operator based task:
choice = int(input("Press 1 for Addition\n Press 2 for Subraction\n Press 3 for Divison\n Press 4 for Multiplication\n Press 5 for Average\n"))
num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number: "))
if choice == 1:
    add = num1 + num2
    print(f"Addition of {num1} and {num2} is {add}")
    if add < 0:
        print("NEGATIVE!")
elif choice == 2:
    sub = num1 - num2
    print(f"Subtraction of {num1} and {num2} is {sub}")
    if sub < 0:
        print("NEGATIVE!")
elif choice == 3:
    div = num1 / num2
    print(f"Division of {num1} and {num2} is {div}")
    if div < 0:
        print("NEGATIVE!")
elif choice == 4:
    mul = num1 * num2
    print(f"Multiplication of {num1} and {num2} is {mul}")
    if mul < 0:
        print("NEGATIVE!")
elif choice == 5:
    avg = (num1 + num2)/ 2
    print(f"Average of {num1} and {num2} is {avg}")
    if avg < 0:
        print("NEGATIVE!")
else:
    print("Please select choice from number 1 to 5")




#Q3) Write a program in Python to implement the given flowchart:
a = 10
b = 20
c = 30
avg = (a + b + c)/3
print("Average is ", avg)
if avg>a and avg>b and avg>c:
    print("Average is higher than a, b, c")
elif avg>a and avg>b:
    print("Average is higher than a, b")
elif avg>a and avg>c:
    print("Average is higher than a,c")
elif avg>b and avg>c:
    print("Average is higher than b,c")
elif avg>a:
    print("Average is just higher than a")
elif avg>b:
    print("Average is just higher than b")
elif avg>c:
    print("Average is just higher than c")




 #Q4) Write a program in Python to break and continue if the following cases occurs:
x=1
while x > 0:
    x = int(input("Enter a number: "))
    if x < 0:
        print("It's Over")
        break
    else:
        print("Good Going")
        continue




#Q5) Write a program in Python which will find all such numbers which are divisible by 7 but #are not a multiple of 5, between 2000 and 3200.
for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        print(num)




#Q6) What is the output of the following code examples?
#i) Error as int object is not iterable
#ii)
#0
#error
#1
#error
#2
#iii) Error as Break is not a keyword




#Q7) Write a program that prints all the numbers from 0 to 6 except 3 and 6.
for num in range(7):
    if num == 3 or num == 6:
        continue
    print(num)




#Q8) Write a program that accepts a string as an input from the user and calculate the number of digits and letters.
string = input("Please enter a string").lower()

d1 = ['a', 'b', 'c', 'd','e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
d2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letter = 0
digit = 0
for i in string:
    if i in d2:
        digit += 1
    elif i in d1:
        letter += 1
    else:
        print("Please enter a combination of letter and digit")

print("Digits:", digit)
print("Letter", letter)




#Q9) Write a program such that it asks users to “guess the lucky number”.
num = 0
luckyNum = 777
while num == 0:
    num1 = int(input("Guess your lucky number:"))
    if num1 == luckyNum:
        break

num = 0
luckyNum = 777
while num == 0:
    number = int(input("Guess your lucky number:"))
    if number == luckyNum:
        break
    else:
        answer= input("Do you want to continue?")
        if answer == 'no':
            break




#Q10) Write a program that asks five times to guess the lucky number. Use a while loop and #a counter
counter = 1
while counter <= 5:
    lucky_number = int(input("Enter your guess:"))
    if lucky_number == 8:
        print("Good Guess")
    else:
        print("Try Again!")
        counter += 1

print("Game Over!")




#Q11) In the previous question, insert break after the “Good guess!” print statement.
counter = 1
while counter <= 5:
    lucky_number = int(input("Enter your guess:"))
    if lucky_number == 8:
        print("Good Guess")
        break
    else:
        print("Sorry but that was not very successful")
        counter += 1

print("Game Over!")
