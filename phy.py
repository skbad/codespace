# Write a program which repeatedly reads numbers until the
#user enters “done”. Once “done” is entered, print out the total, count,
#and average of the numbers. If the user enters anything other than a
#number, detect their mistake using try and except and print an error
#message and skip to the next number.
try:
    inp_i = input('Enter Number: ')
    inp = int(inp_i)
except:
    print('Error')
count = 0
total = 0
for i in inp:
    count = count + 1
    total = total + i
    print(count, total, i)
    average = total/count
print('After',count, total, average)
