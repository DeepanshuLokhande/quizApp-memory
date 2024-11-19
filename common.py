import random
from mcqs import *

def getQuestion(topic , no_of_questions=5):
    return random.sample(topic, no_of_questions)


def quiz():
    score = 0
    topic =input("please enter the topic you want to take the quiz on 1 for Java 2 for Python 3 for RDBMS: ")
    if topic == '1' :
        print("Welcome to the Java quiz")
        questions = getQuestion(java_questions)
        for i , question in enumerate(questions):
            print(f"{i+1}. {question['question']}")
            for j ,option in enumerate(question['options']):
                print(f"{j+1}. {option}")
            answer = int(input("Enter your answer: "))
            if question['options'][answer-1] == question['answer']:
                print("Correct answer")
                score += 1
            else:
                print("Incorrect answer")
        print(f"Your score is {score}")
    elif topic == '2':
        print("Welcome to the Python quiz")
        questions = getQuestion(python_questions)
        for i , question in enumerate(questions):
            print(f"{i+1}. {question['question']}")
            for j ,option in enumerate(question['options']):
                print(f"{j+1}. {option}")
            answer = int(input("Enter your answer: "))
            if question['options'][answer-1] == question['answer']:
                print("Correct answer")
                score += 1
            else:
                print("Incorrect answer")
        print(f"Your score is {score}")
    elif topic == '3':
        print("Welcome to the RDBMS quiz")
        questions = getQuestion(rdbms_questions)
        for i , question in enumerate(questions):
            print(f"{i+1}. {question['question']}")
            for j ,option in enumerate(question['options']):
                print(f"{j+1}. {option}")
            answer = int(input("Enter your answer: "))
            if question['options'][answer-1] == question['answer']:
                print("Correct answer")
                score += 1
            else:
                print("Incorrect answer")
        print(f"Your score is {score}")

        return score