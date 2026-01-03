def classify_career_readiness(students):
    results = []

    for i in range(len(students)):
    student = students[i]
    name = student["name"]
    gpa = student["gpa"]

        if gpa >= 3.0:
            readiness = "High"
        elif gpa >= 2.0:
            readiness = "Medium"
        else:
            readiness = "Low"

        results.append({
            "name": name,
            "gpa": gpa,
            "readiness": readiness
        })

    return results
students_data = [
    {"name": "Student A", "gpa": 3.5},
    {"name": "Student B", "gpa": 2.4},
    {"name": "Student C", "gpa": 1.8}
]
output = classify_career_readiness(students_data)

for student in output:
    print(
        f"Name: {student['name']}, "
        f"GPA: {student['gpa']}, "
        f"Career Readiness: {student['readiness']}"
    )
