students = [
    {"name": "Hermione", "house": "Griffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Griffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Griffindor", "patronus": "Jack Russel Terrier"},
    {"name": "Draco", "house": "slitherin", "patronus": "Some value"},

]
for student in students:
    if student["house"] == "slitherin":
        print(student["name"], student["house"], student["patronus"], sep=", ")

"""


|#     |   name   |   house   |   patronus   |
--------------------------------------------------
|0     | Hermoione | Griffindor | Otter |
|1     | Harry     | Griffindor |Stag




"""




# students = ["Hermione", "Harry", "Ron"]
# houses = ["Griffindor", "Griffindor", "Griffindor", Slythierin]

# for i in range(len(students)):
#     print(students[i])