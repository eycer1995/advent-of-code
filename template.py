import time
day_input = "2023/inputs/d.txt"
data = open(day_input, "r").read().split("\n")


def main():
    print(data)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print("Finished")
    print(f"Elapsed time: {t2 - t1:0.2f}s")



