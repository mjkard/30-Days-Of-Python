# Day 2: 30 days of Python Programming
# Exercise - 1
#Declaring variables
first_name = 'Muhammad'
last_name = 'Gulma'
full_name = 'Muhammad Gulma'
country = 'Nigeria'
city = 'Kebbi'
age = 26
year = 1999
is_married = False
is_true = True
is_light_on = True
education = {'primary school' : 'Vital years', 'Sec_school': 'Zaria Academy', 'College' : 'Ruhr University'}
# Or anothe method of declarying multiple variables in a single line is:
name, age, country, city, house_no = "Muhammad", 330, "Nigeria", "Kebbi", 26
print(name, age, country, city, house_no)
#Exercise -2
print(education)
>>> #Exercise -2
>>> # Proceeding to check all date types of the above
>>> print(type(last_name))
<class 'str'>
>>> print(type(first_name))
<class 'str'>
>>> print(type(full_name))
<class 'str'>
>>> print(type(country))
<class 'str'>
>>> print(type(age))
<class 'int'>
>>> print(type(year))
<class 'int'>
>>> print(type(is_married))
<class 'bool'>
>>> print(type(is_true))
<class 'bool'>
>>> print(type(is_light_on))
<class 'bool'>
>>> print(type(education))
<class 'dict'>
>>> print(len(first_name))
8
>>> print(len(last_name))
5
print(len(last_name)>len(first_name))
False
>>> print(num_two, num_one)
4 5
>>> reminder = num_one % num_two
>>> print('reminder: ', reminder)
#exercise 2 task 
#calculating area of a circle
>>> circle_radius = 30
>>> area_circle = 3.14 * circle_radius**2
>>> print('area of the circle is: ', area_circle)
area of the circle is:  2826.0
#calculating circumference of a circle
>>> circum_of_circle = 2*3.14*circule_radius
circum_of_circle = 2*3.14*circle_radius
>>> print("circumference is: ", circum_of_circle)
circumference is:  188.4
#calculating area of a circle from user prompted data
>>> radius = input("What's the radius: ")
What's the radius: 20
>>> area= 3.14 * radius **2
radius=float(radius)
>>> area= 3.14 * radius **2
>>> print('your circle area is: ', area)
your circle area is:  1256.0
#Collecting user data
first_name = input("Type your first name please: ")
last_name = input("Type your last name please: ")
country = input("Country of origin: ")
age = input('Your age please: ')
print('your info is: ', first_name,last_name,country, age ,  "Thank you for using our services!"   )
#code executed successfully!!
#Day two of Python completed
