
    #Pay Computation

hour = input("Enter Hours: ")
rate = input("Enter Rate: ")
try:
   hp = float(hour)
   rp = float(rate)
except:
    print("Erro, Please enter numeric input")
print(hp, rp)
if hp > 40:
    xp - rp * hp
    dp = (hp - 40.0) * (rp * 0.5)
    xtp = xp + dp
else:
    xtp = hp * rp
print("Pay: ", xtp)

#def statement

def greet(*names):
    print("Hello ", names[0], ",", names[1], ",", names[2], ",", "and ", names[3], ".")
greet("Sikiru", "Amina", "Maryam", "Fatima")

def gret(name:str):
    print("Hello", name)
gret("1")


#function with return value

def sum(a,b):
    return a + b
total =sum(1,2)
print(total)

total = sum(3, sum(1,2))
print(total)

for x in range(1,4):
    for y in range(1,3):
        print("x = ", x, "y = ", y)

for x in range(1,5):
    if x > 3:
            break
    print(x)
for p in "Abdullah":
    print(p)

dic = {"Abdullah":"Boy", "Maryam":"Girl"}
for m in dic.items():
    print(m)

for z in range(1):
    print(z)
else:
    print("End Of Loop!")

num = 0
while num < 10:
    num = num + 1
print("Num = ", num)

def thing():
    print("Hello")
    print("fun")
thing()
print("Zip")

i = 3
print(i)
type(i)

Childrens = ["Abdullah", "Maryam", "Fatima", "Amina", "Aisha", "Sadeeq", "Sabriya", "Fakriya"]
for child in Childrens:
    print("Happy Islamic New Year: ", child)
    print("Done")

it = 0
print("Before", it)
for item in [3,7,4,9,40,80,97]:
    it = it + 1
    print(it, item)
print("After", it)

count = 0
sum = 0
print("Before ", count, sum)
for value in [2, 4, 6, 7, 9, 5, 30]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print("After ", count, sum, sum/count )

cnt = 0
sm = 0
print("Before ", cnt, sm)
for val in [3, 45, 6, 75, 9, 19, 10]:
    cnt = cnt + 1
    sm = sm + val
    print(cnt,":", sm,",", val)
print("After ", cnt, sm, sm/cnt)

c = 0
for v in [2,3,4,5,6,7]:
    c = c + 1
    v = v + c
    print(c, v)

print("Before")
for va in [2,4,16,45,70,60]:
    if va > 20:
        print('Large Number: ', va)
print('After')

big = max('Hello world')
print(big)

tiny = min('Hello')
print(tiny)

name = max("Sikiru Badamasi")
print(name)

x = min(5,10)
print(x)

y = ("Zebra", "Ostrich", "Chicken")
p = min(y)
print(p)


def sex(person):
    if person == 'man':
        print('It is an adult male person')
    elif person == 'female':
        print('It is an adult female person')
    else:
        print('It is just a child')
sex('boy')
sex('man')
sex('female')


#Python program to count words

name = input('Enter file name: ')
handle = open(name, 'r')
counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)

me = "Sikiru Badamasi"
sme = me.split()
print(sme)

x = 3
x = x + 1
print(x)

4
y = 4
y + 1

pupil = input('Enter Your Name: ')
print('Hello', pupil, 'Welcome')

#convert celsius to Fahrent

h = input('Enter Hours Work: ')
r = input('Enter rate: ')
hour = float(h)
rate = float(r)
pay = hour * rate
print('Pay: ', pay)

temper = input('Enter Celsius: ')
temp = float(temper)
fahr = 32 + (temp * 1.8)
print('Temrature in Fahrent = ', fahr)

#If the remainder when x is divided by 2 is 0,
x = 9
if x%2 == 0:
    print('It is an Even Number')
else:
    print('It is an Odd number')

#elif statement

choice = input('Enter Your choices: ')
if choice == 'a':
    print('Bad guess')
elif choice == 'b':
    print('Good guess')
elif choice == 'c':
    print('Close, but not correct')

#pay rate greater than 40 program

hour = input("Enter Hours: ")
rate = input("Enter Rate: ")
try:
   hp = float(hour)
   rp = float(rate)
except:
    print("Erro, Please enter numeric input")
print(hp, rp)
if hp > 40:
    xp = rp * hp
    dp = (hp - 40.0) * (rp * 0.5)
    xtp = xp + dp
else:
    xtp = hp * rp
print("Pay: ", xtp)

in_scores = input('Enter Scores: ')
score = int(in_scores)
for score in range(0.0,1.0):
    print()


#pay with try and except methods-1

hour = input('Enter Hour: ')
rate = input('Enter Rate: ')
try:
    xh = int(hour)
    xr = int(rate)
except:
    print('Erro, Please Enter Numric input')

    #pay with try and except methods-2

    hour = input('Enter Hour: ')
    try:
        xh = int(hour)
    except:
        print('Erro, Please Enter Numeric input')



#scores and grade program

score_in = input('Enter Scores: ')
scores = float(score_in)
if scores >= 0.9:
    print('Grade = A')
elif scores >= 0.8:
    print('Grade = B')
elif scores >= 0.7:
    print('Grade = C')
elif scores >= 0.6:
    print('Grade = D')
elif scores < 0.6:
    print('Grade = F')
else:
    print('Done')


#import random

import random
for i in range(1):
    x = random.random()
    print(x)



#def statement


def print_twice(Bruce):
    print(Bruce)
    print(Bruce)
print_twice('Spam')
import math
print_twice(math.pi)
print_twice('Alhamdulillah')
print_twice(20)
print_twice('ok' * 5)

name = 'Amina Bello'
print_twice(name )



# Rewrite your pay computation with time-and-a-half for over-
#time & create a function called computepay which takes two parameters
#(hours & rate).


def computepay(hour,rate):
    if hour <= 40:
        pay = hour * rate
    elif hour > 40:
        xh = (hour - 40) * (rate * 1.5)
        xr = hour * rate
        pay = xh + xr
    return pay

x_inp = input('Enter Hour: ')
hour = float(x_inp)
y_inp = input('Enter Rate: ')
rate = float(y_inp)
payment = computepay(hour,rate)
print('Pay:', payment)



# Rewrite the grade program from the previous chapter using
# a function called computegrade that takes a score as its parameter and
# returns a grade as a string.


def computegrade(score):
    if score >= 0.9:
        return 'A'
    elif score >= 0.8:
        return 'B'
    elif score >= 0.7:
        return 'C'
    elif score >= 0.6:
        return 'D'
    elif score < 0.6:
        return 'F'
    else:
        return 'Error'

x_inp = input('Enter Scores: ')
score = float(x_inp)
scoring = computegrade(score)
print('Result = ', scoring)
