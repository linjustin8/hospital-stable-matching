# main.py
import sys
from pathlib import Path
from match import Match
from verify import Verify

'''
Usage:
    python3 src/main.py [input_file]
    (e.g. [python3 src/main.py ./tests_in/example1.in])

If no input_file is provided, the program will read from standard input.

'''


def main():
    # remove old output files
    out_dir = Path("../tests_out/")
    for file in out_dir.glob("*.out"):
        file.unlink()

    
    # initialize matcher and verifier
    matcher = None
    verifier = None
    n = 0
    hospital_prefs = []
    student_prefs = []
    
    if len(sys.argv) > 1:
        # file input

        with open(sys.argv[1], 'r') as file:
            # input number of hospitals & students (n)
            n = int(file.readline())

            # hospital preferences
            for i in range(n):
                prefs = list(map(lambda x: int(x) - 1, file.readline().split())) # convert to 0-indexed
                hospital_prefs.append(prefs)

            # student preferences
            for i in range(n):
                prefs = list(map(lambda x: int(x) - 1, file.readline().split())) # convert to 0-indexed
                student_prefs.append(prefs)

    else:
        # typed input

        # input number of hospitals & students (n)
        n = int(input())
        
        # hospital preferences
        for i in range(n):
            prefs = list(map(lambda x: int(x) - 1, input().split())) # convert to 0-indexed
            hospital_prefs.append(prefs)

        # student preferences
        for i in range(n):
            prefs = list(map(lambda x: int(x) - 1, input().split())) # convert to 0-indexed
            student_prefs.append(prefs)


    matcher = Match(n, hospital_prefs, student_prefs)
    matches = matcher.stable_matching()

    verifier = Verify(matcher)
    verifier.verify()
    

    # print results
    print(str(len(matches)) + " matches made: ")
    for pair in matches:
        print(str(pair[0] + 1) + ' ' + str(pair[1] + 1)) # convert back to 1-indexed


    # if file was given write to output file
    if len(sys.argv) > 1:
        new_file = sys.argv[1].split("/")[-1].split(".")[0]
        out_path = Path("../tests_out/" + new_file + ".out")
        
        with open(out_path, 'w') as file:
            for pair in matches:
                file.write(str(pair[0] + 1) + ' ' + str(pair[1] + 1) + '\n') # convert back to 1-indexed
        print("Output successfully written to: " + str(out_path))


    # create matcher and verifier

    # # verify the matching
    # is_stable = verifier.verify()
    # print("Stable" if is_stable else "Unstable")


if __name__ == "__main__":
    main()