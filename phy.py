hour = input("Enter Hours: ")
rate = input("Enter Rate: ")
hp = int(hour)
try:
    rate
except:
    print("Erro, Please enter numeric input")
print(hp, rate)
if hp > 40:
    xp = rate * hp
    dp = (hp - 40.0) * (rate * 0.5)
    xtp = xp + dp
else:
    xtp = hp * rate
print("Pay: ", xtp)

import math
print(math)
