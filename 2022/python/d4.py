#Every section has an unique ID

#Find the pairs that fully contain the other.
#Elf1 need to clean ['85', '85']
#85
#Elf2 need to clean ['2', '84']
#23456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384
# this is contained
# got this error because 5859 these numbre "create" 85 as string

data = open('./inputs/d4.txt', 'r').read().split("\n")
data.pop()
print(data)

overlaps = 0

for section in data:
    sections = section.split(",")
    elf1 = sections[0].split("-")
    elf2 = sections[1].split("-")

    # Sections range
    sec_list1 = ""
    for i in range(int(elf1[0]),int(elf1[1])+1):
        sec_list1 = sec_list1 + str(i)

    sec_list2 = ""
    for j in range(int(elf2[0]),int(elf2[1])+1):
        sec_list2 = sec_list2 + str(j)


    print(f"Elf1 need to clean {elf1}")
    print(sec_list1)
    print(f"Elf2 need to clean {elf2}")
    print(sec_list2)

    #Check if the list are contained on each other
    # first what is the smallest list
    if (sec_list1 in sec_list2) or (sec_list2 in sec_list1):
        overlaps += 1
        print("this one is contained")
    
    print("---")

# 601 first try, is lower
print(f"total overlaps: {overlaps}")
