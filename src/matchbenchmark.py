import time
import random
from match import Match
from verify import Verify

def main():
    inputs = [2 ** p for p in range(1, 15)]
    times = []

    for n in inputs:

        hospital_prefs = []
        student_prefs = []

        n_list = list(range(0, n))

        for i in range(n):
            lst = n_list.copy()
            random.shuffle(lst)
            hospital_prefs.append(lst)
        for i in range(n):
            lst = n_list.copy()
            random.shuffle(lst)
            student_prefs.append(lst)

        matcher = Match(n, hospital_prefs, student_prefs)
        


        start_time = time.perf_counter()
         
        matcher.stable_matching()
        
        end_time = time.perf_counter()

        elapsed_time = end_time - start_time
        times.append(elapsed_time)

        print(f"Elapsed time for n = {n}: {elapsed_time}")

    with open("tests_out/match_benchmark.csv", "w") as file:
        for i in range(len(inputs)):
            file.write(f"{inputs[i]}, {times[i]}\n")



if __name__ == "__main__":
    main()