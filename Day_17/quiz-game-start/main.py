from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

bank_question = []
for question in question_data:
    the_question = Question(question["text"], question["answer"])
    bank_question.append(the_question)

the_quiz = QuizBrain(bank_question)

while the_quiz.still_has_question():
    answer_of_question = the_quiz.next_question()
    print(the_quiz.print())
    print("\n\n")

print("You've completed the game")
print(f"your score {the_quiz.score}/{the_quiz.question_number}")
