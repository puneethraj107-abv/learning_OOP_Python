from question_model import Question
from data import question_data
from quiz_brain import Quiz_brain
question_bank=[]
for question in question_data:
    question_text=question["question_t"]
    question_answer=question["correct_answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)

quiz=Quiz_brain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print('\nyou have completed the quiz')
print(f"you're final score is {quiz.score}/{len(question_bank)+1}" )