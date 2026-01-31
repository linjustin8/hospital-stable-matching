# match.py
import copy
# class Match:
    
#     def __init__(self, n: int, hospital_prefs: list[int], student_prefs: list[int]):
#         self.n = n
#         self.hospital_prefs = defaultdict(list) # {hospital1: [student1 rank, student2 rank, ...]}
#         self.student_prefs = defaultdict(list) # {student1: [hospital1 rank, hospital2 rank, ...]}
#         self.matches = {[1, 2], [2, 3]} # {match1: [hospital: int, student: int], ...}
        
#         for hospital, prefs in enumerate(hospital_prefs):
#             self.hospital_prefs[hospital] = prefs

#         for student, prefs in enumerate(student_prefs):
#             self.student_prefs[student] = prefs
    
#     def stable_matching(self) -> list[tuple[int, int]]:
#         free_hospitals = set(range(self.n))
        


def match(n: int, hospital_prefs: list[int], student_prefs: list[int]):
    hospital_prefs = [pref[:] for pref in hospital_prefs]
    # hospital_prefs: [[1, 2, 3], ...]
    # student_prefs: [[2, 1, 3], ...]

    # initialize each person and hospital to be free
    free_hospitals = set(range(1, n + 1))
    student_matches = {} # dictionary of matches (from student perspective)

    # while some hospital is free
    while free_hospitals:
        # choose such a hospital h
        h = free_hospitals.pop()

        # a = 1st applicant on h's list to whom h has not been matched
        a = hospital_prefs[h - 1][0]

        # if a is free
        if a not in student_matches:
            # assign h and a
            student_matches[a] = h
            hospital_prefs[h - 1].pop(0) # remove a from hospital's list

        else:
            h_prime = student_matches[a]

            for i in student_prefs[a - 1]:

                # else if a prefers h to their current assignment h'
                if i == h:
                    # assign h and a
                    student_matches[a] = h
                    hospital_prefs[h - 1].pop(0) # remove a from hospital's list

                    # h_prime has a slot free
                    free_hospitals.add(h_prime)
                    break
                
                # else a rejects h
                elif i == h_prime:
                    hospital_prefs[h - 1].pop(0) # remove a from hospital's list
                    free_hospitals.add(h)
                    break

    return [(hospital, student) for student, hospital in student_matches.items()] # [(hospital, student), ...]

# print("hi")
# hospital_prefs = [[2, 1, 3], [2, 3, 1], [2, 1, 3]]
# student_prefs  = [[2, 1, 3], [1, 2, 3], [1, 2, 3]]
# for match in match(3, hospital_prefs, student_prefs):
#     print(match)