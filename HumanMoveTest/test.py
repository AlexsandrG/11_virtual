from main import Student
import unittest

class TestStudent(unittest.TestCase):

    def test_walk(self):
        go = Student('Alex')
        for _ in range(0, 10):
            go.walk()
        self.assertEqual(50, go.distance, 'Дистанции не равны '
                                          '[дистанция человека(объекта)] != 500')

    def test_run(self):
        run = Student('Victor')
        for _ in range(0, 10):
            run.run()
        self.assertEqual(100, run.distance,  'Дистанции не равны'
                                           ' [дистанция человека(объекта)] != 1000')

    def test_greater(self):
        student_1 = Student('Alex')
        student_2 = Student('Victor')
        for _ in range(10):
            student_1.walk()
            student_2.run()
        self.assertGreater(student_2.distance, student_1.distance,
                         f'Бегущий человек - {student_2.name} должен преодолеть '
                         f'дистанцию больше, чем идущий человек - {student_1.name}')
