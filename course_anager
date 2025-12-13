def get_average(scores):
    total = 0
    for score in scores:
        total += score
    return total / len(scores)


courses = {}

course_count = int(input("How many courses would you like to enter: "))

for _ in range(course_count):
    course_name = input("Course name: ")
    student_count = int(input("How many students are in this course? "))
    print()

    students = []

    for _ in range(student_count):
        name = input("Student name: ")
        scores = []

        for i in range(3):
            score = int(input(f"Enter score #{i + 1}: "))
            scores.append(score)

        student = {
            "name": name,
            "scores": scores,
            "average": get_average(scores)
        }

        students.append(student)
        print()

    courses[course_name] = students


print("Summary")
for course, students in courses.items():
    print(course)
    for student in students:
        print(student["name"], student["average"])
