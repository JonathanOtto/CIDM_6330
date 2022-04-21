import questions as QuestionClass
import login as LoginClass

questions = QuestionClass.Questions()
login = LoginClass.Login()

#Users login with a 6-digit number. valid numbers are [111111, 123456, 654321, 456789, 987654, 999999]
userLength = True
while (userLength):
    userID = int(input('Enter 6-digit User ID: '))
    if (userID >=1000000 or userID < 100000):
        print("Please enter a valid User ID.")
    else:
        idType = login.login(userID)
        if(idType != 'Please enter a valid User ID.'):
            userLength = False

#When logged in as a student, test questions are asked and score is recorded
if (idType == 'Student'):
    assigned = login.getQuestions()
    for x in assigned:
        quiz = questions.question(x)
        questions.checkAnswer(quiz[0],quiz[1],quiz[2])
    score = (questions.getScore() / len(assigned))*100
    login.updateScore(userID, score)

    print(score)

#When logged in as a teacher users can view student data and modify questions being asked
if (idType == 'Teacher'):
    while (True):
        print("Welcome")
        id = int(input("Enter the ID of the student you wish to review, enter 0 to quit: "))
        if (id == 0):
            break
        login.getInfo(id)
        choice = input("Update questions on exam? Y or N: ")
        if (choice.upper() == 'Y'):
            newItems = input("Which questions are they now assigned? (ex. 1,3): ")
            login.updateQuestions(id, newItems)
            print("Updated Questions: " + newItems)