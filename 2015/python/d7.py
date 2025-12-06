from aocd import get_data
import time

data = get_data(day=7, year=2015)


def main():
    print(data)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print("Finished")
    print(f"Elapsed time: {t2 - t1:0.2f}s")



