import numpy as np
import pandas as pd


SUBJECT_COLUMNS = ["Python_Marks", "Maths_Marks", "Statistics_Marks"]


def load_student_data(file_name):
    """Read student data from CSV file."""
    try:
        student_data = pd.read_csv(file_name)
        return student_data
    except FileNotFoundError:
        print("Error: students.csv file was not found.")
        return None


def calculate_student_result(student_data):
    """Calculate total, average, grade and pass/fail status."""
    totals = []
    averages = []
    grades = []
    results = []

    # Loop is used here so the calculation is easy to understand.
    for _, student in student_data.iterrows():
        marks = student[SUBJECT_COLUMNS].to_numpy(dtype=float)

        total_marks = np.sum(marks)
        average_marks = np.mean(marks)

        totals.append(int(total_marks))
        averages.append(round(float(average_marks), 2))
        grades.append(assign_grade(average_marks))
        results.append(check_pass_fail(marks, average_marks, student["Attendance"]))

    student_data["Total_Marks"] = totals
    student_data["Average_Marks"] = averages
    student_data["Grade"] = grades
    student_data["Result"] = results

    return student_data


def assign_grade(average_marks):
    """Return grade according to average marks."""
    if average_marks >= 90:
        return "A+"
    elif average_marks >= 80:
        return "A"
    elif average_marks >= 70:
        return "B"
    elif average_marks >= 60:
        return "C"
    elif average_marks >= 50:
        return "D"
    elif average_marks >= 40:
        return "E"
    else:
        return "F"


def check_pass_fail(marks, average_marks, attendance):
    """
    Pass condition:
    1. At least 33 marks in every subject
    2. Overall average at least 40
    3. Attendance at least 60%
    """
    passed_all_subjects = np.all(marks >= 33)

    if passed_all_subjects and average_marks >= 40 and attendance >= 60:
        return "Pass"
    return "Fail"


def show_class_summary(student_data):
    """Display highest, lowest and class-average performance."""
    highest_index = student_data["Average_Marks"].idxmax()
    lowest_index = student_data["Average_Marks"].idxmin()

    highest_student = student_data.loc[highest_index]
    lowest_student = student_data.loc[lowest_index]
    class_average = np.mean(student_data["Average_Marks"].to_numpy())

    print("\n--- CLASS PERFORMANCE SUMMARY ---")
    print(f"Highest Average : {highest_student['Name']} ({highest_student['Average_Marks']}%)")
    print(f"Lowest Average  : {lowest_student['Name']} ({lowest_student['Average_Marks']}%)")
    print(f"Class Average   : {class_average:.2f}%")


def show_pass_fail_statistics(student_data):
    """Display pass/fail count and pass percentage."""
    result_count = student_data["Result"].value_counts()

    passed_students = int(result_count.get("Pass", 0))
    failed_students = int(result_count.get("Fail", 0))
    total_students = len(student_data)

    pass_percentage = np.round((passed_students / total_students) * 100, 2)

    print("\n--- PASS / FAIL STATISTICS ---")
    print(f"Total Students : {total_students}")
    print(f"Passed         : {passed_students}")
    print(f"Failed         : {failed_students}")
    print(f"Pass Percentage: {pass_percentage}%")


def show_subject_analysis(student_data):
    """Display average, highest and lowest marks for every subject."""
    print("\n--- SUBJECT-WISE PERFORMANCE ---")

    for subject in SUBJECT_COLUMNS:
        clean_name = subject.replace("_Marks", "")
        marks = student_data[subject].to_numpy()

        average_marks = np.mean(marks)
        highest_marks = np.max(marks)
        lowest_marks = np.min(marks)

        print(
            f"{clean_name:10} -> "
            f"Average: {average_marks:.2f}, "
            f"Highest: {highest_marks}, "
            f"Lowest: {lowest_marks}"
        )


def show_top_performers(student_data, number_of_students=5):
    """Display top students according to average marks."""
    top_students = student_data.nlargest(
        number_of_students, "Average_Marks"
    )[["Student_ID", "Name", "Department", "Average_Marks", "Grade"]]

    print(f"\n--- TOP {number_of_students} PERFORMERS ---")
    print(top_students.to_string(index=False))


def show_department_analysis(student_data):
    """Extra useful Pandas analysis: department-wise average marks."""
    department_average = (
        student_data.groupby("Department")["Average_Marks"]
        .mean()
        .round(2)
        .sort_values(ascending=False)
    )

    print("\n--- DEPARTMENT-WISE AVERAGE ---")
    print(department_average.to_string())


def show_student_report(student_data):
    """Display the final student result table."""
    report_columns = [
        "Student_ID", "Name", "Department", "Total_Marks",
        "Average_Marks", "Grade", "Result", "Attendance"
    ]

    print("\n--- COMPLETE STUDENT REPORT ---")
    print(student_data[report_columns].to_string(index=False))
