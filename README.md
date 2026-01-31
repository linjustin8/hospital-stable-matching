# COP4533 Programming Assignment 1: Matching and Verifying

## Justin Lin [36425312] and Yi Su [31833267]
An implementation of the Gale-Shapley Stable Matching Algorithm for assigning `n` hospitals to `n` students based on preference lists.

## Input
- First line: integer `n`.
- Next `n` lines: hospital preference lists.
- Next `n` lines: student preference lists.

#### Example
```text
3
1 2 3
2 3 1
2 1 3
2 1 3
1 2 3
1 2 3
```

## Usage
If you have an input file (e.g., `tests/example1.in`):
```bash
python main.py tests/examples1.in
```
The output matchings are written to `examples1.out` in the same directory.

If no file path is given, you can enter the data line by line.


## Functions
### `match(n, hospital_preference_lists, student_preference_lists)`

#### Input
- **`n`** - Number of hospitals (equal to the number of students).  
- **`hospital_preference_lists`** - A list of `n` hospital preference lists.  
  Each sublist contains all student IDs (1-indexed) in order of preference, e.g.  
  `[[1, 2, 3], [2, 3, 1], [2, 1, 3]]`.  
- **`student_preference_lists`** - A list of `n` student preference lists.  
  Each sublist contains all hospital IDs (1-indexed) in order of preference, e.g.  
  `[[2, 1, 3], [1, 2, 3], [1, 2, 3]]`.

#### Output
- Returns a **list of tuples** `(hospital, student)` representing the final stable matching.

#### Example
```python
n = 3
hospital_prefs = [[2, 1, 3], [2, 3, 1], [2, 1, 3]]
student_prefs  = [[2, 1, 3], [1, 2, 3], [1, 2, 3]]

match(n, hospital_prefs, student_prefs)
# Output: [(1, 2), (2, 3), (3, 1)]
```
---
### `verify(n, hospital_preference_lists, student_preference_lists, matches)`

#### Input
- **`n`** - Number of hospitals (equal to the number of students).  
- **`hospital_preference_lists`** - A list of `n` hospital preference lists.  
  Each sublist contains all student IDs (1-indexed) in order of preference, e.g.  
  `[[1, 2, 3], [2, 3, 1], [2, 1, 3]]`.  
- **`student_preference_lists`** - A list of `n` student preference lists.  
  Each sublist contains all hospital IDs (1-indexed) in order of preference, e.g.  
  `[[2, 1, 3], [1, 2, 3], [1, 2, 3]]`.
- **`matches`** - A **list of tuples** `(hospital, student)` representing the final stable matching (as returned from match()).

#### Output
- Returns a **bool** representing the validity of the matching provided, checking for duplicates and blocking pairs.
