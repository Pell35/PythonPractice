contacts = {
    "number" : 4,
    "Students":
        [
            {"name": "Sarah Holderness", "email": "sarah@example.com"},
            {"name": "Harry Potter", "email": "harry@example.com"},
            {"name": "Hermoine Granger", "email": "hermoine@example.com"},
            {"name": "Ron Weasley", "email": "ron@example.com"}
        ]
}

print("Student emails:")
for student in contacts["Students"]:
    print(student["email"])