import random

students = {"michelle": ("michelle", 98)}
for i in range(3):
    name = f"student {i}"
    grade = random.randint(0, 100)
    student = (name, grade)
    if name not in students:
        students[name] = student
    else:
        print(f"\"{name}\" already exists")
    
if "student 6" in students:
    print(students["student 6"])
else:
    print("\"student 6\" is not a recognised tag/key")
        
for i, (name, student) in enumerate(students.items()):
    print(f"{i} {name}: {student}")
    