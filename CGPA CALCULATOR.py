# PERSONAL POCKET CGPA CALCULATOR (PPC)

print("=" * 50)
print("     PERSONAL POCKET CGPA CALCULATOR")
print("=" * 50)

num_courses = int(input("Enter the number of courses: "))

total_quality_points = 0
total_credit_units = 0

for i in range(1, num_courses + 1):
    print(f"\nCourse {i}")

    course_code = input("Enter Course Code: ").upper()
    score = float(input("Enter Score (0 - 100): "))
    credit_unit = int(input("Enter Credit Unit: "))

    # Determine Grade and Grade Point
    if score >= 70:
        grade = "A"
        grade_point = 5
    elif score >= 60:
        grade = "B"
        grade_point = 4
    elif score >= 50:
        grade = "C"
        grade_point = 3
    elif score >= 45:
        grade = "D"
        grade_point = 2
    elif score >= 40:
        grade = "E"
        grade_point = 1
    else:
        grade = "F"
        grade_point = 0

    quality_point = grade_point * credit_unit

    total_quality_points += quality_point
    total_credit_units += credit_unit

    print("\nCourse Result")
    print("Course Code :", course_code)
    print("Grade       :", grade)
    print("Grade Point :", grade_point)
    print("Quality Pt. :", quality_point)

# Calculate CGPA
cgpa = total_quality_points / total_credit_units

print("\n" + "=" * 50)
print("              FINAL RESULT")
print("=" * 50)
print("Total Credit Units :", total_credit_units)
print("Total Quality Points:", total_quality_points)
print("CGPA :", round(cgpa, 2))

# CGPA Classification
if cgpa >= 4.50:
    classification = "First Class"
elif cgpa >= 3.50:
    classification = "Second Class Upper"
elif cgpa >= 2.40:
    classification = "Second Class Lower"
elif cgpa >= 1.50:
    classification = "Third Class"
elif cgpa >= 1.00:
    classification = "Pass"
else:
    classification = "Fail"

print("Class of Degree :", classification)
print("=" * 50)
print("Thank you for using PPC.")