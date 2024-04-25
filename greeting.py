
def generate_greeting(name, grade):
    if grade >= 1 and grade <= 5:
        return f"Hello {name}! Welcome to elementary school."
    elif grade >= 6 and grade <= 8:
        return f"Hey {name}! Enjoy your time in middle school."
    elif grade >= 9 and grade <= 12:
        return f"Hi {name}! Make the most of your high school experience."
    else:
        return f"Hello {name}! Keep up the good work in your studies."

# Test the function
student_name = input("Enter student's name: ")
student_grade = int(input("Enter student's grade: "))
greeting_message = generate_greeting(student_name, student_grade)
print(greeting_message)

