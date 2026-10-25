# Student Performance Analytics System

## Project Overview
This is a beginner-friendly Python data analysis project that reads student data from a CSV file and performs useful performance analysis.

The project uses:
- Python
- NumPy
- Pandas
- Functions
- Loops
- Conditions
- CSV data handling

## Main Features
- Loads student records using Pandas
- Calculates total and average marks
- Assigns grades
- Checks pass/fail status
- Finds highest, lowest and overall class average
- Performs subject-wise analysis
- Shows top-performing students
- Shows department-wise average performance
- Uses a simple menu so every analysis can be viewed separately

## Pass / Fail Rule
A student is marked **Pass** when:
1. Marks in every subject are at least 33
2. Overall average is at least 40
3. Attendance is at least 60%

Otherwise, the student is marked **Fail**.

## Grading Rule
| Average | Grade |
|---|---|
| 90 and above | A+ |
| 80-89.99 | A |
| 70-79.99 | B |
| 60-69.99 | C |
| 50-59.99 | D |
| 40-49.99 | E |
| Below 40 | F |

## Project Files
- `main.py` - Runs the project and menu
- `functions.py` - Contains reusable functions
- `students.csv` - Student dataset
- `Project_Documentation.md` - Project explanation
- `requirements.txt` - Required Python libraries

## How to Run
1. Install Python.
2. Open terminal inside the project folder.
3. Install libraries:

```bash
pip install -r requirements.txt
```

4. Run:

```bash
python main.py
```

## Learning Outcome
This project helped in understanding how Python fundamentals can be combined with NumPy and Pandas for real data analysis. It also helped in practicing functions, loops, conditions, DataFrames and simple statistical calculations.
