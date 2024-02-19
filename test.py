from main import StudentsInMLOps

def test_enroll_students():
    mlops = StudentsInMLOps()
    mlops.enroll_students(5)
    assert mlops.get_total_strength() == 5

def test_drop_students():
    mlops = StudentsInMLOps()
    mlops.enroll_students(10)
    mlops.drop_students(3)
    assert mlops.get_total_strength() == 7