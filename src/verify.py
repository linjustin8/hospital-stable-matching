# verify.py

class Verify:
    
    def __init__(self, n: int, hospital_prefs: list[list[int]], student_prefs: list[list[int]], matching: list[tuple[int, int]]):
        self.n = n
        self.hospital_prefs = hospital_prefs
        self.student_prefs = student_prefs
        self.matching = matching

    def verify(self):
        hospitals = [h for h, _ in self.matching]
        students = [s for _, s in self.matching]

        if len(set(hospitals)) != self.n or len(set(students)) != self.n:
            print("hospital and student count mismatched")
            return False

        if sorted(hospitals) != list(range(self.n)) or sorted(students) != list(range(self.n)):
            print("participant IDs should be 1 to n")
            return False

        student_to_hospital = {s: h for h, s in self.matching}
        hospital_to_student = {h: s for h, s in self.matching}

        for h in range(self.n):
            for s in range(self.n):
                current_s = hospital_to_student[h]
                current_h = student_to_hospital[s]

                if current_s == s:
                    continue

                h_pref = self.hospital_prefs[h]
                s_pref = self.student_prefs[s]

                prefers_s = h_pref.index(s) < h_pref.index(current_s)
                prefers_h = s_pref.index(h) < s_pref.index(current_h)

                if prefers_s and prefers_h:
                    print("Unstable Pair:", h, "and", s)
                    return False
        return True