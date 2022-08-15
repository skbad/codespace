
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
