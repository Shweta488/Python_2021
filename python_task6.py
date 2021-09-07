#Q1) Write a program in Python to find out the character in a string which is uppercase using list comprehension.

str1 = "I LoVe PytHon"
str2 = str1.upper()
str = str2.replace(" ", "")
newlist = [word for word in str1 if word in str]

print(newlist)




#Q2) Write a program to construct a dictionary from the two lists containing the names of students and their corresponding subjects.

students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']
dictionary = dict(zip(students, subjects))
print(dictionary)




#Q4) Write a program in Python using generators to reverse the string.

def reverse_string(my_str):
    length = len(my_str)
    for i in range(length-1, -1, -1):
        yield my_str[i]

reverse_list= list(reverse_string(“Consultadd Training”))
print(''.join(reverse_list))




#Q5) Write an example on decorators.

def is_called():
    def is_returned():
        print("Hello There!")
    return is_returned

new = is_called()
new()
