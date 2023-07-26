def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif 80 <= marks < 90:
        return "A"
    elif 70 <= marks < 80:
        return "B"
    elif 60 <= marks < 70:
        return "C"
    elif 50 <= marks < 60:
        return "D"
    else:
        return "Fail"


def get_valid_marks():
    while True:
        try:
            marks = int(input("Enter the marks obtained by the student: "))
            if marks < 0 or marks > 100:
                raise ValueError("Invalid marks. Marks should be between 0 and 100.")
            return marks
        except ValueError as e:
            print(e)


def main():
    while True:
        marks = get_valid_marks()
        grade = calculate_grade(marks)
        print(f"The grade for the student is: {grade}")

        choice = input("Do you want to calculate the grade for another student? (y/n): ")
        if choice.lower() != 'y':
            break


if __name__ == "__main__":
    main()
