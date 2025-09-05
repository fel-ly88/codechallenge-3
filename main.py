# main.py
from models import Student, Teacher, Course

# Create instances
alice = Student("Alice Johnson", 12)
bob = Student("Bob Smith", 14)

mr_smith = Teacher("Mr. Smith")

math = Course("Math")
science = Course("Science")

# Assign teacher
mr_smith.assign_course(math)
mr_smith.assign_course(science)

# Enroll students
alice.enroll(math)
alice.enroll(science)
bob.enroll(math)

# Output aggregates
print(alice.total_courses())  # 2
print(math.student_count())   # 2
