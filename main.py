# main.py
from src.match import Match
from src.verify import Verify


def main():
    # initialize matcher and verifier
    matcher = None
    verifier = None
    hospital_prefs = []
    student_prefs = []
    
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

    # create matcher and verifier
    matcher = Match(n, hospital_prefs, student_prefs)
    
    
    # verifier = Verify(matcher)

    # # verify the matching
    # is_stable = verifier.verify()
    # print("Stable" if is_stable else "Unstable")


if __name__ == "__main__":
    main()