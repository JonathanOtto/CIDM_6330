import questions as QuestionClass
import login as LoginClass

questions = QuestionClass.Questions()
login = LoginClass.Login()

userLength = True
while (userLength):
    userID = int(input('Enter 6-digit User ID: '))
    if (userID >=1000000 or userID < 100000):
        print("Please enter a valid User ID.")
    else:
        idType = login.login(userID)
        if(idType != 'Please enter a valid User ID.'):
            userLength = False

if (idType == 'Student'):
    assigned = login.getQuestions()
    for x in assigned:
        quiz = questions.question(x)
        questions.checkAnswer(quiz[0],quiz[1],quiz[2])


    score = (questions.getScore() / len(assigned))*100

    login.updateScore(userID, score)

    print(score)

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