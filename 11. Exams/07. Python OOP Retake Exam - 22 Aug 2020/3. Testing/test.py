from project.student_report_card import StudentReportCard
import unittest


class TestStudentReportCard(unittest.TestCase):

    def setUp(self):
        self.stc = StudentReportCard('Mitko', 2)

    def test__init_student_name(self):
        result = self.stc.student_name
        expected_result = 'Mitko'
        self.assertEqual(result, expected_result)

    def test__init_student_name__when_empty(self):
        with self.assertRaises(ValueError) as ex:
            stc = StudentReportCard('', 2)
        self.assertIsNotNone(ex)
        expected_mess = 'Student Name cannot be an empty string!'
        self.assertEqual(str(ex.exception), expected_mess)

    def test__init_school_year(self):
        result = self.stc.school_year
        expected_result = 2
        self.assertEqual(result, expected_result)

    def test__init_school_year__when_less_1(self):
        with self.assertRaises(ValueError) as ex:
            stc = StudentReportCard('Mitko', 0)
        self.assertIsNotNone(ex)
        expected_mess = 'School Year must be between 1 and 12!'
        self.assertEqual(str(ex.exception), expected_mess)

    def test__init_school_year__when_great_12(self):
        with self.assertRaises(ValueError) as ex:
            stc = StudentReportCard('Mitko', 13)
        self.assertIsNotNone(ex)
        expected_mess = 'School Year must be between 1 and 12!'
        self.assertEqual(str(ex.exception), expected_mess)

    def test__init_grades_by_subject_empty(self):
        result = self.stc.grades_by_subject
        expected_result = {}
        self.assertEqual(result, expected_result)

    def test__add_grade(self):
        self.stc.add_grade('Math', 5.5)
        result = self.stc.grades_by_subject
        expected_result = {'Math': [5.5]}
        self.assertEqual(result, expected_result)

        self.stc.add_grade('Math', 5.75)
        result = self.stc.grades_by_subject
        expected_result = {'Math': [5.5, 5.75]}
        self.assertEqual(result, expected_result)

        self.stc.add_grade('Geo', 6)
        result = self.stc.grades_by_subject
        expected_result = {'Math': [5.5, 5.75], 'Geo': [6]}
        self.assertEqual(result, expected_result)

    def test__average_grade_by_subject(self):
        self.stc.add_grade('Math', 5.5)
        self.stc.add_grade('Math', 5.7)
        self.stc.add_grade('Geo', 6)
        self.stc.add_grade('Geo', 5)
        result = self.stc.average_grade_by_subject()
        expected_result = 'Math: 5.60\nGeo: 5.50'
        self.assertEqual(result, expected_result)

    def test__average_grade_by_subject_empty(self):
        result = self.stc.average_grade_by_subject()
        expected_result = ''
        self.assertEqual(result, expected_result)

    def test__average_grade_for_all_subjects(self):
        self.stc.add_grade('Math', 3)
        self.stc.add_grade('Math', 4)
        self.stc.add_grade('Geo', 6)
        self.stc.add_grade('Geo', 5)
        result = self.stc.average_grade_for_all_subjects()
        expected_result = 'Average Grade: 4.50'
        self.assertEqual(result, expected_result)

    def test__repr__(self):
        self.stc.add_grade('Math', 3)
        self.stc.add_grade('Math', 4)
        self.stc.add_grade('Geo', 6)
        self.stc.add_grade('Geo', 5)

        result = str(self.stc)
        expected_result = 'Name: Mitko\nYear: 2\n----------\nMath: 3.50\nGeo: 5.50\n----------\nAverage Grade: 4.50'
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
