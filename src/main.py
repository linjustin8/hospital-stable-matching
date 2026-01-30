# main.py
import sys
from match import match
# from src.verify import Verify


def main():
    # initialize matcher and verifier
    # matcher = None
    # verifier = None
    n = 0
    hospital_prefs = []
    student_prefs = []
    
    if len(sys.argv) > 1:
        # file input

        with open(sys.argv[1], 'r') as file:
            # input number of hospitals & students (n)
            n = int(file.readline)

            # hospital preferences
            for i in range(n):
                prefs = list(map(int, file.readline().split()))
                student_prefs.append(prefs)

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

    for match1 in match(n, hospital_prefs, student_prefs):
        print(match1)

    # create matcher and verifier
    # matcher = Match(n, hospital_prefs, student_prefs)

    # verifier = Verify(matcher)

    # # verify the matching
    # is_stable = verifier.verify()
    # print("Stable" if is_stable else "Unstable")


if __name__ == "__main__":
    main()