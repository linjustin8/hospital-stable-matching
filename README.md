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

## Assumptions
- n != 0
- preferences for hospitals **`i`**: **`1 <= i <= n`**
- preferences for students **`j`**: **`1 <= j <= n`**


## Graph + Solution to Task C
<img width="598" height="362" alt="image" src="https://github.com/user-attachments/assets/abff1ce0-6b06-49a1-abdf-04969df0418e" />

<img width="598" height="356" alt="image" src="https://github.com/user-attachments/assets/7117ce74-4b30-4a0e-a7fc-b3eac17ca5f5" />


**`What is the trend that you notice?`**
We found that as the number of data points(n) increased, the matcher's runtime increased at a quadratic rate, exhibiting a time complexity of O(n^2). The same was true with the verifier as our algorithm for it also ran at a time complexity of O(n^2). 



## Functions + Extra Info
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
