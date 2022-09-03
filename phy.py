biggest_num = None
for i in [4,8,12,25,65,19,80]:
    if biggest_num is None or i > biggest_num:
        biggest_num = i
    print('Loop:', i, biggest_num)
print('Biggest Number:', biggest_num)
