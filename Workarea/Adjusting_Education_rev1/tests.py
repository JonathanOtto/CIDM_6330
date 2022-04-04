import unittest
import quiz as QuizClass

quiz = QuizClass.Quiz()
class Testing(unittest.TestCase):
    def test_login_teacher(self):
        
        a = quiz.login(999999)
        b = "Teacher"
        self.assertEqual(a, b)
        
    def test_login_student(self):
        
        a = quiz.login(123456)
        b = "Student"
        self.assertEqual(a, b)

    def test_checkAnswer_wrong(self):
        a = quiz.checkAnswer("a","b")
        b = "Remember the color wheel practice"
        self.assertEqual(a, b)
        
    def test_checkAnswer_right(self):
        a = quiz.checkAnswer("a","a")
        b = ""
        self.assertEqual(a, b)

    def test_feedback_teacher_correct(self):
        a = quiz.feedback("Teacher","")
        b = "Student got question correct"
        self.assertEqual(a, b)

    def test_feedback_teacher_wrong(self):
        a = quiz.feedback("Teacher","Remember the color wheel practice")
        b = "Student got question wrong and recieved feedback of: Remember the color wheel practice"
        self.assertEqual(a, b)
    
    def test_feedback_teacher_correct(self):
        a = quiz.feedback("Student","Remember the color wheel practice")
        b = "Remember the color wheel practice"
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()