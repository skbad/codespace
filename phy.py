# Write a program which repeatedly reads numbers until the
#user enters “done”. Once “done” is entered, print out the total, count,
#and average of the numbers. If the user enters anything other than a
#number, detect their mistake using try and except and print an error
#message and skip to the next number.
num = 0
tot = 0.0
while True:
    sval = input('Enter Number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid Input')
        continue
        num = num + 1
        tot = tot + fval
print(tot, num, tot/num)

fruit = 'Banana'
letter = fruit[-2]
print(letter)
len(fruit)
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)
