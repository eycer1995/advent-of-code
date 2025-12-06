from aocd import get_data
import time

data = get_data(day=1, year=2025)

def move_left(dial, clicks, count_zero, count_rotation_zero):
    for i in range(clicks):
        dial = dial - 1

        if dial == -1:
            dial = 99

        if dial == 0:
            count_rotation_zero += 1
    
    if dial == 0:
        count_zero += 1

    return dial, count_zero, count_rotation_zero
    

def move_right(dial, clicks, count_zero, count_rotation_zero):
    for i in range(clicks):
        dial = dial + 1

        if dial == 100:
            dial = 0

        if dial == 0:
            count_rotation_zero += 1

    if dial == 0:
        count_zero += 1

    return dial, count_zero, count_rotation_zero


def main(data):
    dial = 50
    count_zero = 0
    count_rotation_zero = 0
    moves = data.split('\n')
    for i, move in enumerate(moves):
        clicks = int(move[1:])
        print(f"For move {i}, dial is {dial} and move is {move}")
        if move[0] == "L":
            dial, count_zero, count_rotation_zero = move_left(dial, clicks, count_zero, count_rotation_zero)

        elif move[0] == "R":
            dial, count_zero, count_rotation_zero = move_right(dial, clicks, count_zero, count_rotation_zero)
        
        print(count_zero)

        #if i == 5:
        #    break
    print("---")
    print(f"First part: {count_zero}")
    print(f"Second part: {count_rotation_zero}")


if __name__ == "__main__":
    t1 = time.perf_counter()
    main(data)
    t2 = time.perf_counter()
    print("Finished")
    print(f"Elapsed time: {t2 - t1:0.2f}s")



