# match.py
import typing
from collections import defaultdict

class Match:
    
    def __init__(self, n: int, hospital_prefs: list[int], student_prefs: list[int]):
        self.n = n
        self.hospital_prefs = defaultdict(list) # {hospital1: [student1 rank, student2 rank, ...]}
        self.student_prefs = defaultdict(list) # {student1: [hospital1 rank, hospital2 rank, ...]}
        self.matches = {}  
        
        for hospital, prefs in enumerate(hospital_prefs):
            self.hospital_prefs[hospital] = prefs

        for student, prefs in enumerate(student_prefs):
            self.student_prefs[student] = prefs
    
    def stable_matching(self) -> list[tuple[int, int]]:
        free_hospitals = set(range(self.n))
        




