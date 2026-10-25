from functions import (
    load_student_data,
    calculate_student_result,
    show_student_report,
    show_class_summary,
    show_pass_fail_statistics,
    show_subject_analysis,
    show_top_performers,
    show_department_analysis,
)


def show_menu():
    print("\n========== STUDENT PERFORMANCE ANALYTICS ==========")
    print("1. Show complete student report")
    print("2. Show class performance summary")
    print("3. Show pass/fail statistics")
    print("4. Show subject-wise analysis")
    print("5. Show top performers")
    print("6. Show department-wise analysis")
    print("7. Show complete analysis")
    print("8. Exit")


def show_complete_analysis(student_data):
    show_student_report(student_data)
    show_class_summary(student_data)
    show_pass_fail_statistics(student_data)
    show_subject_analysis(student_data)
    show_top_performers(student_data)
    show_department_analysis(student_data)


def main():
    student_data = load_student_data("students.csv")

    if student_data is None:
        return

    student_data = calculate_student_result(student_data)

    print("Student data loaded successfully.")
    print(f"Total records: {len(student_data)}")
    print("Columns:", ", ".join(student_data.columns))

    while True:
        show_menu()
        user_choice = input("Enter your choice (1-8): ").strip()

        if user_choice == "1":
            show_student_report(student_data)
        elif user_choice == "2":
            show_class_summary(student_data)
        elif user_choice == "3":
            show_pass_fail_statistics(student_data)
        elif user_choice == "4":
            show_subject_analysis(student_data)
        elif user_choice == "5":
            show_top_performers(student_data)
        elif user_choice == "6":
            show_department_analysis(student_data)
        elif user_choice == "7":
            show_complete_analysis(student_data)
        elif user_choice == "8":
            print("Project closed successfully.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()
