from importlib.metadata import metadata
from sqlalchemy import create_engine, ForeignKey, null, select, Table
from sqlalchemy import Column, Date, Integer, String, MetaData, update
from sqlalchemy.ext.declarative import declarative_base

#Reading in table "logins" from users.db
engine = create_engine('sqlite:///users.db', echo=False)
connection = engine.connect()
metadata = MetaData()

users = Table("logins", metadata, autoload=True, autoload_with=engine)
stmt = select([users])
results = connection.execute(stmt).fetchall()

#Returns from the table each user type. Also each question is stored
class Login:
    type = ""
    questions = []
    def login(self,id):
        for x in range(len(results)):
            row = results[x]
            if(id == row['login']):
                self.type = row['type']
                self.questions = str(row['questions'])
                self.questions = [int(x) for x in self.questions.split(',') if x != '']
        if (self.type ==''):
            return ('Please enter a valid User ID.')
        else:
            return(self.type)

#Returns the stored question
    def getQuestions(self):
        return(self.questions)

#Pushes the users score back to the table
    def updateScore(self, id, newscore):
        updateScore = update(users).where(users.c.login == id).values(score = newscore)
        push = connection.execute(updateScore)

#Pushes the assigned questions to table
    def updateQuestions(self, id, items):
        updateQuestion = update(users).where(users.c.login == id).values(questions = items)
        push = connection.execute(updateQuestion)

#Pulls students name, assigned questions, and score    
    def getInfo(self, id):
        for x in range(len(results)):
            row = results[x]
            if(id == row['login'] and row['type'] == 'Student'):
                print("Name: "+ row['name'])
                print("Questions assigned: " + str(row['questions']))
                if (row['score'] < 0):
                    score = 'Test not taken'
                else:
                    score = str(row['score'])
                print("Score: " + score)            