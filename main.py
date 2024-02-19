class StudentsInMLOps:
    def __init__(self):
        self.total_strength = 0

    def enroll_students(self, count):
        self.total_strength += count

    def drop_students(self, count):
        self.total_strength -= count

    def get_total_strength(self):
        return self.total_strength

    def get_class_name(self):
        return "StudentsInMLOps"
