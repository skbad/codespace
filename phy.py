def computepay(hour,rate):
    if hour <= 40:
        pay = hour * rate
    elif hour > 40:
        x = (hour - 40) * (rate * 1.5)
        y = hour * rate
        pay = x + y
    return pay

hrs = input('Enter Hour:')
rte = input('Enter Rate:')
hour = float(hrs)
rate = float(rte)
p = computepay(hour, rate)
print('Pay:', p)
