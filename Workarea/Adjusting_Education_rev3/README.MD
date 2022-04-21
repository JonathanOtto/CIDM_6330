# Needed items
    sqlalchemy
    pytest

# Use and explanation
    Running main.py starts the program. You are asked to enter a login, these are compared to the login data in users.db
    The purpose of this program is to test students and record their score, as well as allow teachers to view these scores and modify which
    questions will be asked on the exam.

# Results of student login
    If a student login is used (ex. 123456), you will be asked to answer all the questions assigned to that student login (ex. Question 1).
    After answering each question, the user will get a "correct" message for right answers, or a feedback about the answer for wrong answers.
    when the exam is complete the score is displayed as well as stored in the database for that login.

# Results of teacher login
    If a teacher login is used (ex. 987654), you will be asked which student login you would like to view (ex. 123456).
    Once entered the students name, assigned questions, and test score are displayed (or a "test not taken" message)
    The user will then be asked if they want to edit the assigned questions ('Y' or 'N') and can then enter the new set if desired.
    To exit view student prompt, users must enter and id of '0'

    
