import time
import random
from match import Match

def main():
    inputs = [2 ** p for p in range(1, 15)]


    for n in inputs:

        hospital_prefs = []
        student_prefs = []

        n_list = list(range(0, n))

        for i in range(n):
            random.shuffle(n_list)
            hospital_prefs.append(n_list)
        for i in range(n):
            random.shuffle(n_list)
            student_prefs.append(n_list)

        matcher = Match(n, hospital_prefs, student_prefs)

        start_time = time.perf_counter()
        
        matcher.stable_matching()

        end_time = time.perf_counter()

        elapsed_time = end_time - start_time

        print(f"Elapsed time for n = {n}: {elapsed_time}")




if __name__ == "__main__":
    main()