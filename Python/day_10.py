#prints from 0 to 5
count = 0
while count <= 5:
    print(count)
    count = count + 1
    print("Inside the loop")
print("Outside the loop")
print("Depends on indentation level")

#prints from 0 to 4 and then prints 5 after the loop
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

#prints from 0 to 2 and then breaks out of the loop
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
#prints from 0 to 4 but skips 3
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count = count + 1

#infinite loop example (commented out to prevent execution)
# while True:
#     print("This is an infinite loop")

#for loop example a list
numbers = [0, 1, 2, 3, 4, 5]
for n in numbers: # n is temporary name to refer to the list's items, valid only inside this loop
    print(n)       # the numbers will be printed line by line, from 0 to 5

#for loop with continue and shorthand if-else
    numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements

#Range function in for loops
lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,13,3))
print(lst) # [0, 3, 6, 9, 12]
st = set(range(0,13,3))
print(st) #  {0, 3, 6, 9, 12}

# for backward from start to end 
lst = list(range(11,0,-2))
print(lst) # [11,9,7,5,3,1]

#prints from 0 to 10
count = 0
while count <=10:
    print(count)
    count += 1
#backwards from 10 to 0
count = 10
while count >=0:
    print(count)
    count -= 1

#Write a loop that makes seven calls to print(), so we get a triangle of asterisks.
for i in range(1,7):
    print('*' * i)
#nested loops to print a square of asterisks
for i in range(1,7):
    for j in range(1,7):
        print('*', end='') # end='' prevents moving to the next line after each print
    print() # moves to the next line after inner loop completes
#print the multiplication table from 1 to 10
for i in range(1,11):
    for j in range(1,11):
        print(f'{i*j:4}', end='') # formatted to take up 4 spaces
    print() # moves to the next line after inner loop completes
#FizzBuzz from 1 to 100
for i in range(101):
    if i % 2 == 0:
        print(i)
    else:
        print("odd")