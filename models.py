class Student:
    def __init__(self, full_name, age):
        self.full_name = full_name
        self.age = age
        self.courses = []  # Many-to-many with Course

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.add_student(self)

    def total_courses(self):
        return len(self.courses)

class Teacher:
    def __init__(self, full_name):
        self.full_name = full_name
        self.courses = []  # One-to-many with Course

    def assign_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.teacher = self

class Course:
    def __init__(self, title):
        self.title = title
        self.students = []  # Many-to-many with Student
        self.teacher = None  # One-to-many relationship

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            if self not in student.courses:
                student.courses.append(self)

    def student_count(self):
        return len(self.students)
    
    
    
# Count how many courses a student is enrolled in
print(student.total_courses())

# Count how many students are in a course
print(course.student_count())

# List all courses a teacher teaches
for c in teacher.courses:
    print(c.title)
