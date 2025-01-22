class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if not self.grades:
            return "No grades available."
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        avg = self.calculate_average()
        return f"Student: {self.name}, Average Grade: {avg}"


# Example usage
student = Student("Alice")
student.add_grade(85)
student.add_grade(90)
student.add_grade(78)

print(student.display_info())
