import questions as QuestionClass

questions = QuestionClass.Questions()

def test_correct_score():
    questions.checkAnswer('A', 'A', 'feedback')
    score = questions.getScore()
    assert score == 1
