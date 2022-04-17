

class Quiz:
    type = ""
    userAnswer = ""
    correctAnswer = "b"
    message = ""
    def login(self,id):
        if (int(id/100000) == 9):
            self.type = "Teacher"
        else:
            self.type = "Student"
        return(self.type)

    def question(self):
        print("Question 1: Mixing Blue and Red result in what color?")
        print("A. Green    B. Purple    C. Black    D. White\n")
        self.userAnswer = input("Enter the letter of the answer choice you choose:")
        return (self.userAnswer.lower(), self.correctAnswer)
    
    def checkAnswer(self, answer, correct):
        if (answer == correct):
            print ("Correct, good job!")
        else:
            print("Incorrect")
            self.message = "Remember the color wheel practice"
        return self.message
    
    def feedback(self, id, message):
        if (id == "Teacher" and message == ""):
            return ("Student got question correct")
        if (id == "Teacher" and message != ""):
            return ("Student got question wrong and recieved feedback of: " + message)
        else:
            return message