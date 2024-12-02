import time
day_input = "2023/inputs/d1.txt"
data = open(day_input, "r").read().split("\n")
count = 0

numbers_dic = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def process_data(data, count):
    for i in range(len(data)):
        digits = []

        for j in data[i]:
            if j.isdigit():
                digits.append(j)
        count = count + get_double(digits)
    return count

def process_part2(data,count,numbers_dic):
    for i in range(len(data)):
        digits = []
        for number in numbers_dic.keys():
            if  number in data[i]:
                digits.append(numbers_dic[number])

        print(data[i])
        print(digits)
        print()



def get_double(digits):
    if len(digits) == 1:
        return (int(digits[0]) * 11)

    else:
        dd = digits[0] + digits[-1]
        return int(dd)





def main():
    print(str(len(data)) + " lines")
    #part1 = process_data(data,count)
    #print(f"Sum of calibration values in part 1 is {part1}")
    process_part2(data,count,numbers_dic)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print("Finished")
    print(f"Elapsed time: {t2 - t1:0.2f}s")
