def calculate_average(marks):
    return sum(marks) / len(marks)


def classify_result(average):
    if average >= 70:
        return "Distinction"
    elif average >= 50:
        return "Pass"
    else:
        return "Fail"


def main():
    print("STUDENT RESULT PROCESSOR")
    print("------------------------")

    student_name = input("Enter the student's name: ").strip()
    marks = []


    for unit_number in range(1, 4):
        while True:
            try:
                mark = float(input(f"Enter the mark for unit {unit_number}: "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break

                print("Please enter a mark between 0 and 100.")
            except ValueError:
                print("Please enter a number, such as 65 or 65.5.")

    average = calculate_average(marks)
    result = classify_result(average)

    print("\nSTUDENT RESULT REPORT")
    print("---------------------")
    print(f"Student: {student_name}")

    for unit_number, mark in enumerate(marks, start=1):
        print(f"Unit {unit_number}: {mark:g}")

    print(f"Average mark: {average:.2f}")
    print(f"Result: {result}")


main()

