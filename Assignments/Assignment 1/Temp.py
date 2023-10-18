class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, entered_password):
        # Implement login logic
        return self.password == entered_password

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.tutors = []
        self.receptionists = []

    def admin_menu(self):
        while True:
            print("Admin Menu:")
            print("1. Register Tutor")
            print("2. Delete Tutor")
            print("3. Assign Tutor to Level and Subject")
            print("4. Register Receptionist")
            print("5. Delete Receptionist")
            print("6. View Monthly Income Report")
            print("7. Update Profile")
            print("8. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.register_tutor()
            elif choice == "2":
                self.delete_tutor()
            elif choice == "3":
                self.assign_tutor()
            elif choice == "4":
                self.register_receptionist()
            elif choice == "5":
                self.delete_receptionist()
            elif choice == "6":
                self.view_income_report()
            elif choice == "7":
                self.update_profile()
            elif choice == "8":
                print("Logging out.")
                break
            else:
                print("Invalid choice. Please try again.")

    def register_tutor(self):
        username = input("Enter tutor's username: ")
        password = input("Enter tutor's password: ")
        tutor = Tutor(username, password)
        self.tutors.append(tutor)
        print(f"Tutor {username} registered successfully.")

    def delete_tutor(self):
        username = input("Enter tutor's username to delete: ")
        for tutor in self.tutors:
            if tutor.username == username:
                self.tutors.remove(tutor)
                print(f"Tutor {username} deleted successfully.")
                return
        print(f"Tutor {username} not found.")

    def assign_tutor(self):
        username = input("Enter tutor's username: ")
        level = input("Enter the level to assign (e.g., Form 1): ")
        subject = input("Enter the subject to assign: ")
        for tutor in self.tutors:
            if tutor.username == username:
                tutor.assign_to_level_subject(level, subject)
                print(f"{username} assigned to {level} - {subject}.")
                return
        print(f"Tutor {username} not found.")

    def register_receptionist(self):
        username = input("Enter receptionist's username: ")
        password = input("Enter receptionist's password: ")
        receptionist = Receptionist(username, password)
        self.receptionists.append(receptionist)
        print(f"Receptionist {username} registered successfully.")

    def delete_receptionist(self):
        username = input("Enter receptionist's username to delete: ")
        for receptionist in self.receptionists:
            if receptionist.username == username:
                self.receptionists.remove(receptionist)
                print(f"Receptionist {username} deleted successfully.")
                return
        print(f"Receptionist {username} not found.")

    def view_income_report(self):
        level = input("Enter the level (e.g., Form 1): ")
        subject = input("Enter the subject: ")
        total_income = 0
        for record in self.income_records:
            if record['level'] == level and record['subject'] == subject:
                total_income += record['income']
        print(f"Monthly income for {level} - {subject}: ${total_income}")

    def update_profile(self):
        new_password = input("Enter new password: ")
        self.password = new_password
        print("Profile updated successfully.")


class Receptionist(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.students = []

    def receptionist_menu(self):
        while True:
            print("Receptionist Menu:")
            print("1. Register Student and Enroll in Subjects")
            print("2. Update Subject Enrollment")
            print("3. Accept Payment and Generate Receipt")
            print("4. Delete Students")
            print("5. Update Profile")
            print("6. Logout")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.register_student()
            elif choice == "2":
                self.update_subject_enrollment()
            elif choice == "3":
                self.accept_payment()
            elif choice == "4":
                self.delete_students()
            elif choice == "5":
                self.update_profile()
            elif choice == "6":
                print("Logging out.")
                break
            else:
                print("Invalid choice. Please try again.")

    def register_student(self):
        print("Student Registration:")
        name = input("Enter student's name: ")
        ic_passport = input("Enter student's IC/Passport: ")
        email = input("Enter student's email: ")
        contact_number = input("Enter student's contact number: ")
        address = input("Enter student's address: ")
        level = input("Enter student's level (e.g., Form 1): ")

        subjects = []
        while True:
            subject = input("Enter a subject (or type 'done' to finish): ")
            if subject.lower() == 'done':
                break
            subjects.append(subject)

        month_of_enrollment = input("Enter the month of enrollment: ")

        student_info = {
            'name': name,
            'ic_passport': ic_passport,
            'email': email,
            'contact_number': contact_number,
            'address': address,
            'level': level,
            'subjects': subjects,
            'month_of_enrollment': month_of_enrollment
        }

        self.students.append(student_info)
        print("Student registered successfully.")

    def update_subject_enrollment(self):
        print("Update Subject Enrollment:")
        student_name = input("Enter the name of the student to update: ")
        for student in self.students:
            if student['name'] == student_name:
                print(f"Current subjects: {', '.join(student['subjects'])}")
                new_subjects = []
                while True:
                    subject = input("Enter a new subject (or type 'done' to finish): ")
                    if subject.lower() == 'done':
                        break
                    new_subjects.append(subject)
                student['subjects'] = new_subjects
                print("Subject enrollment updated successfully.")
                return
        print(f"Student {student_name} not found.")

    def accept_payment(self):
        # Implement payment acceptance and receipt generation logic
        pass

    def delete_students(self):
        # Implement logic to delete students who have completed their studies
        pass

    def update_profile(self):
        new_password = input("Enter new password: ")
        self.password = new_password
        print("Profile updated successfully.")


class Tutor(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def tutor_menu(self):
        # Implement Tutor-specific menu options
        pass

class Student(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def student_menu(self):
        # Implement Student-specific menu options
        pass

def login_system(users):
    login_attempts = 3
    while login_attempts > 0:
        username = input("Enter username/email: ")
        password = input("Enter password: ")

        for user in users:
            if user.username == username:
                if user.login(password):
                    if isinstance(user, Admin):
                        user.admin_menu()
                    elif isinstance(user, Receptionist):
                        user.receptionist_menu()
                    elif isinstance(user, Tutor):
                        user.tutor_menu()
                    elif isinstance(user, Student):
                        user.student_menu()
                    return

        login_attempts -= 1
        print(f"Invalid login. Attempts left: {login_attempts}")

    print("Login attempts exhausted. Exiting.")

if __name__ == "__main__":
    admin = Admin("admin@example.com", "admin123")
    receptionist = Receptionist("receptionist@example.com", "rec123")
    tutor = Tutor("tutor@example.com", "tutor123")
    student = Student("student@example.com", "student123")

    users = [admin, receptionist, tutor, student]

    login_system(users)