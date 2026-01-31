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
        prefs = list(map(lambda x: int(x) - 1, input().split())) # convert to 0-indexed
        hospital_prefs.append(prefs)

    # student preferences
    for i in range(n):
        prefs = list(map(lambda x: int(x) - 1, input().split())) # convert to 0-indexed
        student_prefs.append(prefs)

    # create matcher and verifier
    matcher = Match(n, hospital_prefs, student_prefs)
    matches = matcher.stable_matching()
    
    print("Matches (Hospital, Student):")
    for hospital, student in matches:
        print(f"{hospital + 1} {student + 1}") # convert back to 1-indexed
        
    
    # verifier = Verify(matcher)

    # # verify the matching
    # is_stable = verifier.verify()
    # print("Stable" if is_stable else "Unstable")


if __name__ == "__main__":
    main()