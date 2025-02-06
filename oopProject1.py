class School:
    def __init__(self, school_name):
        self.school_name=school_name
        self.students=[]
        self.group=[]
        self.teacher=[]
    
    def add_student(self):
        """Add student to school"""
        while True:
            full_name=input("Input Student's full name: ")
            self.students.append(full_name.title())
            if full_name=="":
                break
        return f"Students in school are: {self.students}."

        self.manage_groups()

    def manage_groups(self):
        required_groups = len(self.students)//30
        if len(self.groups) < required_groups:
            teacher_name=input(f"Enter the teacher name for {len(self.groups+1)}: ".title())
            self.teacher.append(teacher_name)
            new_group=self.students[len(self.students)*30: (len(self.students)+1)*30]
            self.groups.append (new_group)
            self.teacher.append(teacher_name)
            self.groups.append(new_group)
            
    def remove_school(self):
        """Delete all school data."""
        print(f"Deleting {self.school_name}...")
        self.school_name = None
        self.students.clear()
        self.groups.clear()
        self.teachers.clear()
        print("School data has been cleared.\n")



my_school = School("School n11")




