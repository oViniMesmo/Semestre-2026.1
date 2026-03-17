# Check if a number is positive or negative
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
# Check if a number is positive, negative, or zero
    b = 0
if b > 0:
    print('B is a positive number')
elif b < 0:
    print('B is a negative number')
else:
    print('B is zero')
# Check if a number is positive, negative, or zero and if it's even or odd
    c = 10
if c > 0:
    if c % 2 == 0:
        print('C is a positive and even integer')
    else:
        print('C is a positive number')
elif c == 0:
    print('C is zero')
else:
    print('C is a negative number')
# Check if a person is allowed to access a resource
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
        print('Access denied!')
# Check if a person is old enough to drive (18 years old)
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive")
else:
    years_to_wait = 18 - age
    print(f"You need to wait {years_to_wait} more years to drive")

# Compare two ages and determine who is older
my_age = int(input("Enter your age: "))
your_age = int(input("Enter your age: "))

if my_age > your_age:
    age_difference = my_age - your_age
    if age_difference == 1:
        print(f"I am older than you by {age_difference} year")
    else:
        print(f"I am older than you by {age_difference} years")
elif your_age > my_age:
    age_difference = your_age - my_age
    if age_difference == 1:
        print(f"You are older than me by {age_difference} year")
    else:
        print(f"You are older than me by {age_difference} years")
else:
    print("We are the same age!")