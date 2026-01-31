# match.py
from collections import defaultdict

class Match:
    
    def __init__(self, n: int, hospital_prefs: list[list[int]], student_prefs: list[list[int]]):
        self.n = n
        self.hospital_prefs = {} # {hospital1: [student1 rank, student2 rank, ...]}
        self.student_prefs = {} # {student1: [hospital1 rank, hospital2 rank, ...]}
        self.matches = {}  # {student: hospital}
        
        for hospital, prefs in enumerate(hospital_prefs):
            self.hospital_prefs[hospital] = prefs

        for student, prefs in enumerate(student_prefs):
            self.student_prefs[student] = prefs
    
        # ranking map to allow for overall O(n^2) complexity as shown in lectures
        # [REF]: https://stackoverflow.com/questions/61002839/how-do-i-achieve-on2-complexity-for-the-gale-shapley-algorithm
        student_rankings = {}
        for student, prefs in self.student_prefs.items():
            ranking = {}
            for rank, hospital in enumerate(prefs):
                ranking[hospital] = rank
            student_rankings[student] = ranking
        self.student_rankings = student_rankings
    
    def stable_matching(self) -> list[tuple[int, int]]: # [n x 2]
        # [REF]: https://www.youtube.com/watch?v=0m_YW1zVs-Q
        
        free_hospitals = set(range(self.n))
        next_proposal_idx = [0 for i in range(self.n)]  # track next student to propose for each hospital to prevent re-proposals of previously rejected students
        
        while free_hospitals:
            hospital = free_hospitals.pop()
            curr_prefs = self.hospital_prefs[hospital]

            student_idx = next_proposal_idx[hospital]
            if student_idx >= self.n:
                continue
            
            student = curr_prefs[student_idx]
            next_proposal_idx[hospital] += 1
            
            if student not in self.matches: # a is free
                self.matches[student] = hospital
            elif self.student_rankings[student][hospital] < self.student_rankings[student][self.matches[student]]: # a prefers h to her/his current assignment h'
                curr_hospital = self.matches[student]
                self.matches[student] = hospital
                free_hospitals.add(curr_hospital)
            else:
                free_hospitals.add(hospital)
        
        
        result = [(hospital, student) for student, hospital in self.matches.items()]
        return result
