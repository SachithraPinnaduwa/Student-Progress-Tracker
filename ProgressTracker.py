from student import Student
from staff_member import StaffMember


def check(pass_credits, defer_credits, fail_credits):
    arr_of_numbers = [0, 20, 40, 60, 80, 100, 120]
    if pass_credits in arr_of_numbers and defer_credits in arr_of_numbers and fail_credits in arr_of_numbers:
        return True
    return False


def main():
    val = True
    while val:
        user_type = input("Enter '1' if you are a staff member or '2' if you are a student: ")
        if user_type.lower() in ["1", "2"]:
            val = False
        student_id = ""
        pass_credits = 0
        defer_credits = 0
        fail_credits = 0
        if user_type == '1':
            staff_member = StaffMember(user_id="staff01")

            while True:

                try:
                    student_id = input('Student ID: ')
                    pass_credits = int(input('Please enter your credits at pass: '))
                    defer_credits = int(input('Please enter your credits at defer: '))
                    fail_credits = int(input('Please enter your credits at fail: '))
                except ValueError as e:
                    print(e)
                if (pass_credits+defer_credits + fail_credits == 120) and check(pass_credits, defer_credits, fail_credits):
                    student = Student(student_id, pass_credits, defer_credits, fail_credits)
                    staff_member.add_student(student)
                else:
                    print('Invalid')

                quit_option = input("Enter 'y' to continue or 'q' to quit: ").lower()
                if quit_option == 'q':
                    break

            staff_member.display_histogram()
            staff_member.display_student_outcomes()
            staff_member.save_to_file('data.txt')

        elif user_type == '2':
            val = True
            while val:
                try:
                    student_id = input('Student ID: ')
                    pass_credits = int(input('Please enter your credits at pass: '))
                    defer_credits = int(input('Please enter your credits at defer: '))
                    fail_credits = int(input('Please enter your credits at fail: '))
                except ValueError as e:
                    print(e)
                if (pass_credits+defer_credits + fail_credits == 120) and check(pass_credits, defer_credits, fail_credits):
                    student = Student(student_id, pass_credits, defer_credits, fail_credits)
                    student.display_outcome()
                    val = False
                else:
                    print('Invalid')


if __name__ == '__main__':
    main()
