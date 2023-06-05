WAND = 0
FNAME = 1
LNAME = 2

students = {
    "G1": ["Unicorn Cherry Wood", "Neville", "Longbotton"],
    "S1": ["Elder Wand", "Tom", "Riddle"],
}

looking_for = 'G1'
if looking_for in students:
    print(f"{looking_for} is a student.")
else:
    print(f"{looking_for} is not a student.")

print(f"{'-' * 20}")

for student_id in students:
    student= students[student_id]
    print(f"{student[FNAME]} {student[LNAME]} {student[WAND]}.")