data = open('d1.txt', 'r').read().split('\n')
sub = increase = ingroup = window = group = oldgroup = 0
#print(data)
for x in range(len(data)-1):
    #print(data[x])
    sub = int(data[x + 1]) - int(data[x])
    #print(rest)
    if sub > 0:
        increase+=1
print("Day 1 part 1: " + str(increase))

for x in range(len(data)):
    #print(data[x])
    if (x >= 2):
        group = int(data[x -2]) + int(data[x -1]) + int(data[x])
        #print(group - oldgroup)
    if (group - oldgroup) > 0:
        ingroup+=1
    oldgroup = group
    #print(group)
print("Day 1 part 2: " + str(ingroup-1))
