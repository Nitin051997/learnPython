#if / elif / else, comparison operators in Python

a = 10
b = 10

#print(a == b)       #Equal to
#print(a != b)       #Not equal to
#print(a > b)        #Greater than
#print(a < b)        #Less than
#print(a >= b)       #Greater than or equal to
#print(a <= b)       #Less than or equal to

if(a > b):
    print("A is Greater")
elif(a == b):
    print("A is equal to B")
else:
    print("B is Greater")


#Practice Session

age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")

user_password = "1234"
password = input("Enter your password: ")

if user_password == password:
    print("Login Successfull")
else:
    print("Login Failed")

