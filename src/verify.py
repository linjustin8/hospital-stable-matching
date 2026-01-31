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

        if sorted(hospitals) != list(range(1, self.n + 1)) or sorted(students) != list(range(1, self.n + 1)):
            print("participant IDs should be 1 to n")
            return False

        student_to_hospital = {s: h for h, s in self.matching}
        hospital_to_student = {h: s for h, s in self.matching}

        for h in range(1, self.n + 1):
            for s in range(1, self.n + 1):
                current_s = hospital_to_student[h]
                current_h = student_to_hospital[s]

                if current_s == s:
                    continue

                h_pref = self.hospital_prefs[h - 1]
                s_pref = self.student_prefs[s - 1]

                prefers_s = h_pref.index(s - 1) < h_pref.index(current_s - 1)
                prefers_h = s_pref.index(h - 1) < s_pref.index(current_h - 1)

                if prefers_s and prefers_h:
                    print("Unstable Pair:", h, "and", s)
                    return False
        return True