class School:
    def __init__(self, school_name):
        self.school_name = school_name
        self.students = []
        self.groups = []
        self.teachers = []

    def add_students(self):
        print("\nEnter student names (press Enter to finish):")
        while True:
            full_name = input("Student's full name: ").strip()
            if full_name == "":
                break
            self.students.append(full_name.title())

        print(f"\nTotal students in {self.school_name}: {len(self.students)}")
        self.manage_groups()

    def manage_groups(self):
        required_groups = (len(self.students) + 29) // 30

        while len(self.groups) < required_groups:
            group_number = len(self.groups) + 1
            teacher_name = input(f"Enter the teacher name for Group {group_number}: ").title()
            self.teachers.append(teacher_name)

            start_index = (group_number - 1) * 30
            end_index = min(start_index + 30, len(self.students))
            new_group = self.students[start_index:end_index]

            self.groups.append({"Teacher": teacher_name, "Students": new_group})

        print("\nGroups have been assigned successfully!")
        for i, group in enumerate(self.groups, 1):
            print(f"Group {i}: {len(group['Students'])} students, Teacher: {group['Teacher']}")

    def remove_school(self):
        print(f"\nDeleting {self.school_name}...")
        self.school_name = None
        self.students.clear()
        self.groups.clear()
        self.teachers.clear()
        print("All school data has been cleared.\n")


def main():
    school = None

    while True:
        print("\nLMS Menu:")
        print("1. Add a School")
        print("2. Add Students to School")
        print("3. Delete School")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            if school is None:
                school_name = input("Enter the school name: ").title()
                school = School(school_name)
                print(f"\nSchool '{school_name}' has been created.")
            else:
                print("\nA school already exists. Delete it before adding a new one.")

        elif choice == "2":
            if school:
                school.add_students()
            else:
                print("\nNo school exists. Add a school first.")

        elif choice == "3":
            if school:
                confirm = input("Are you sure you want to delete the school? (yes/no): ").strip().lower()
                if confirm == "yes":
                    school.remove_school()
                    school = None
            else:
                print("\nNo school exists to delete.")

        elif choice == "4":
            print("\nExiting the LMS. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")


main()




