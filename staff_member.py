from user import User


class StaffMember(User):
    def __init__(self, user_id):
        super().__init__(user_id)
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_histogram(self):
        outcomes = {'Progress': 0, 'Progress (module trailer)': 0, 'Module retriever': 0, 'Exclude': 0}
        check = ""
        for student in self.students:
            if student.outcome == 'Total credits incorrect':
                check = student.outcome
                print("Incorrect credits please try again")
                break
            outcomes[student.outcome] += 1
        if check != 'Total credits incorrect':
            print("Histogram")
            for outcome, count in outcomes.items():
                print(f"{outcome}: {count} {'*' * count}")

    def display_student_outcomes(self):
        for student in self.students:
            print(student)

    def save_to_file(self, filename):
        with open(filename, 'a') as file:
            for student in self.students:
                file.write(str(student) + '\n')
