def calculate_average(scores):
    total = 0
    for score in scores:
        total += score
    return total / len(scores)


students = {}

count = int(input("How many students? "))

for _ in range(count):
    name = input("Student name: ")
    scores = []

    for i in range(3):
        score = int(input(f"Enter score #{i + 1}: "))
        scores.append(score)

    students[name] = {
        "scores": scores,
        "average": calculate_average(scores)
    }


print("Results")
for name, data in students.items():
    print(name, data["average"])
