from aocd import get_data
from utils.functions import *
import time
import re

data = get_data(day=2, year=2025)

def is_invalid_p1(id: int):
    length = len(str(id))
    if not is_even(length):
        return False
    
    half = int(length / 2)
    str_id = str(id)
    
    first_half = str_id[:half]
    second_half = str_id[half:]

    if first_half == second_half:
        #print(f"For id {id} the first half is {first_half} and second is {second_half}")
        return True

def is_invalid_p2(id: int):
    str_id = str(id)
    match = re.match(r'^(.+?)\1+$', str_id)
    if match:
        #pat = match.group(1)
        #print(f"For id {id} contains the pattern {pat}")
        return True

def check_range(id_range: str, invalid_id_sum: int, invalid_id_sum_p2: int):
    start = int(id_range.split("-")[0])
    end = int(id_range.split("-")[1]) + 1
    #print(start,end)
    for id in range(start, end):
        #print(id)
        if is_invalid_p1(id):
            invalid_id_sum = invalid_id_sum + id
        if is_invalid_p2(id):
            invalid_id_sum_p2 = invalid_id_sum_p2 + id
        
    return invalid_id_sum, invalid_id_sum_p2


def main():
    ranges = data.split(",")
    invalid_id_sum = 0
    invalid_id_sum_p2 = 0
    for i, id_range in enumerate(ranges):
        invalid_id_sum, invalid_id_sum_p2 = check_range(id_range, invalid_id_sum, invalid_id_sum_p2)
        #print("---")

    print(f"Part 1: {invalid_id_sum}")
    print(f"Part 2: {invalid_id_sum_p2}")


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print("Finished")
    print(f"Elapsed time: {t2 - t1:0.2f}s")