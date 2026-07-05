# PERSONAL POCKET CGPA CALCULATOR (PPC)

print("=" * 55)
print("       PERSONAL POCKET CGPA CALCULATOR (PPC)")
print("=" * 55)

num_courses = int(input("Enter the number of courses: "))

courses = []
total_quality_points = 0
total_credit_units = 0

# Input all courses first
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

    # Backend calculations
    quality_point = grade_point * credit_unit
    total_quality_points += quality_point
    total_credit_units += credit_unit

    # Store course result
    courses.append([course_code, grade])

# Calculate CGPA
cgpa = total_quality_points / total_credit_units

# Determine Classification
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

# Display Results
print("\n" + "=" * 55)
print("                 COURSE RESULTS")
print("=" * 55)
print("{:<15}{}".format("COURSE CODE", "GRADE"))

for course in courses:
    print("{:<15}{}".format(course[0], course[1]))

print("=" * 55)
print(f"OVERALL CGPA   : {cgpa:.2f}")
print(f"CLASSIFICATION : {classification}")
print("=" * 55)
print("Thank you for using PPC.")