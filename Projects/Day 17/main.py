from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    new_q = Question(data["question"],data["correct_answer"])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
quiz.next_question()
if not quiz.still_has_question():
    print("You have completed the quiz!")
    print(f"Your final score is:{quiz.score}/{quiz.question_number}")
