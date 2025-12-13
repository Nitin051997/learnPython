#Learn printing, comments, variables, data types


print('Hello World')
print(30)
print(2+3)


name = 'Nitin'
age = 28
print(name, age)

height = 176.7
alive = True

print(type(name))
print(type(age))
print(type(height))
print(type(alive))


#Practice session 

name = "Nitin"                  #string
age = 28                        #int
role = "Frontend Developer"     #string
is_working = True               #boolean


print("Name: ", name)
print("Age: ", age)
print("Role: ", role)
print("Working: ", is_working)

#Can we store an array ??

data_object = {name: "nitin"}       #dict
data_array = [{name: "nitin"}]      #list

print(data_object)
print(data_array)

#Yes we can!
#What will be it's type?

print(type(data_object))
print(type(data_array))

#Take user input

user_name = input("Enter your Name: ")
user_age = int(input("Enter your Age: "))
user_height = float(input("Enter your Height: "))
print(user_height)

system_name, system_type = input("Enter System Name & Type: ").split()
print(system_name, system_type)


#Add Two Number
a, b = map(int, input("Enter Two Number: ").split())
print(a + b)
