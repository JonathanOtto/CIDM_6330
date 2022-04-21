from importlib.metadata import metadata
from pickle import TRUE
from sqlalchemy import create_engine, ForeignKey, select, Table, true
from sqlalchemy import Column, Date, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

#Reading in table "questions" from users.db
engine = create_engine('sqlite:///users.db', echo=False)
connection = engine.connect()
metadata = MetaData()

questions = Table("questions", metadata, autoload=True, autoload_with=engine)
stmt = select([questions])
results = connection.execute(stmt).fetchall()

#Returns from the table each questions text, choices, answers, and feedback
class Questions:
    correctCount = 0
    def question(self, assign):
        invalid = True
        for x in range(len(results)):
            row = results[x]
            if(assign == row['qid']):
                print(row['question'])
                print(row['choices'])
                correctAnswer = row['answer']
                message = row['feedback']
                while (invalid):
                    userAnswer = input("Enter the letter of the answer choice you choose:")
                    userAnswer = userAnswer.upper()
                    if (userAnswer == 'A' or userAnswer == 'B' or userAnswer == 'C' or userAnswer == 'D'):
                        invalid = False
                    else:
                        print("Please enter a valid response")
        return (userAnswer, correctAnswer, message)

 #Checks if answer is correct and prints feedback if wrong   
    def checkAnswer(self, answer, correct, message):
        if (answer == correct):
            print ("Correct, good job!")
            self.correctCount += 1
        else:
            print("Incorrect")
            print(message)

#Getting total correct in order to finalize score
    def getScore(self):
        return self.correctCount
    