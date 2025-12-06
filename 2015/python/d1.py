data = open('./2015/inputs/d1.txt', 'r').read()
result = 0
flag = 0
bfloor = 0
# print(data)
for floor in range(len(data)):
    if data[floor] == "(":
        result += 1
    elif data[floor] == ")":
        result -= 1
    if result == -1 and flag == 0:
        bfloor = floor + 1
        flag = 1
print("2015 - Day 1 part 1 answer is: " + str(result))
print("2015 - Day 1 part 2 answer is: " + str(bfloor))
