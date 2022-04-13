import quiz as QuizClass
import login as LoginClass

quiz = QuizClass.Quiz()
login = LoginClass.Login()

userLength = True
while (userLength):
    userID = int(input('Enter 6-digit User ID: '))
    if (userID >=1000000 or userID < 100000):
        print("Please enter a valid User ID.")
    else:
        userLength = False
idType = login.login(userID)
choice = quiz.question()
result = quiz.checkAnswer(choice[0],choice[1])
print (quiz.feedback(idType, result))