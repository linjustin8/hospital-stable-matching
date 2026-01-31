# main.py
import sys
from pathlib import Path
from match import Match
from verify import Verify


def main():
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
                prefs = list(map(int, file.readline().split()))
                hospital_prefs.append(prefs)

            # student preferences
            for i in range(n):
                prefs = list(map(int, file.readline().split()))
                student_prefs.append(prefs)

    else:
        # typed input

        # input number of hospitals & students (n)
        n = int(input())
        
        # hospital preferences
        for i in range(n):
            prefs = list(map(int, input().split()))
            hospital_prefs.append(prefs)

        # student preferences
        for i in range(n):
            prefs = list(map(int, input().split()))
            student_prefs.append(prefs)


    matcher = Match(n, hospital_prefs, student_prefs)
    matches = matcher.stable_matching()

    verifier = Verify(matcher)
    verifier.verify()
    

    # print results
    print(str(len(matches)) + " matches made: ")
    for pair in matches:
        print(str(pair[0]) + ' ' + str(pair[1]))


    # if file was given write to output file
    if len(sys.argv) > 1:
        out_path = Path(sys.argv[1]).with_suffix(".out")
        with open(out_path, 'w') as file:
            for pair in matches:
                file.write(str(pair[0]) + ' ' + str(pair[1]) + '\n')
        print("Output successfully written to: " + str(out_path))


    # create matcher and verifier

    # # verify the matching
    # is_stable = verifier.verify()
    # print("Stable" if is_stable else "Unstable")


if __name__ == "__main__":
    main()