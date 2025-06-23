from aocd import get_data
import time

data = get_data(day=1, year=2024)


def main():
    location_ids = data.split('\n')
    
    left_numbers = []
    right_numbers = []

    for i in range(len(location_ids)):
        id_pair = location_ids[i].split()
        left_numbers.append(id_pair[0])
        right_numbers.append(id_pair[1])

        print(id_pair)

    print(sorted(left_numbers))

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print("Finished")
    print(f"Elapsed time: {t2 - t1:0.2f}s")



