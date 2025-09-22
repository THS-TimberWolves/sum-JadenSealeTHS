#while summation code following directions from Readme
x = int(input())
stored_num = 0
while x != 0:
    if x < 0:
        stored_num = stored_num + x
        x += 1
    elif x > 0:
        stored_num = stored_num + x
        x -= 1
print(stored_num)
