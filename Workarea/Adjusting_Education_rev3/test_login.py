import login as LoginClass


login = LoginClass.Login()

def test_login_teacher():
    type = login.login(999999) 
    assert type == 'Teacher'

def test_login_student():
    type = login.login(111111) 
    assert type == 'Student'

def test_get_questions():
    question = login.getQuestions()
    assert question == [1,2,3]
