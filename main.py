class person:
    def getname(self):
        print("Sikiru")
    def getage(self):
        print("39")
p = person()
p.getname()
p.getage()

#rate payment
hour = input("Enter Hours: ")
rate = input("Enter Rate: ")
pay = int(hour) * int(rate)
print("Pay ", pay)

#if and elif statement
x = 0
if x < 2:
    print("Smaller")
elif x > 10:
    print("Bigger")
else:
    print("Non of the above")

for y in range(0,12,2):
    print(y)
while y in range(0,6,2):
    print("It is feasible")
else:
    print("It is not feasible")


    #Try and Except

    stra = "Hello Bob"
    try:
        istra = int(astra)
    except:
        istra = -1
    print("First", istra)

    astra = "123"
    try:
        istra = int(astra)
    except:
        istra = -1
    print("First", istra)

    #comparison statement
    x = 5
    if x == 5:
        print("x is equal to 5")
    if x > 4:
        print("x is greater than  4")
    if x >= 5:
        print("x is greater than or equal to 5")
    if x <= 5:
        print("x is less than or equal to 5")
    if x < 6:
        print("x is less than 5")
    if x != 6:
        print("x is not equal to 6")

    #One-Way Decision

    x = 5
    print('Before 5')
    if x == 5:
        print('Is 5')
        print('Is Still 5')
        print('Third  5')
    print('Afterward 5')
    print('Before  6')
    if x == 6:
        print('Is 6')
        print('Is Still 6')
        print('Third  6')
    print('Afterward 6')

     x = 4
    if x > 2 :
         print('Bigger')
    else:
        print('Smaller')

        x =  input("Enter Small Number: ")
        y = int(x)
        if y < 2 :
            print("Smaller")
        elif y > 10:
            print("Very Big")
        else:
            print("Not available")

x = 23
y = 15
ave = x/15
print("The Average =",ave)

def aver(num1, num2):
    print(num1 + num2)
aver(25, 12)
