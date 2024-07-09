from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for ques in question_data:
    text_answer = Question(ques['text'], ques['answer'])
    question_bank.append(text_answer)
# print(question_bank[5].text, question_bank[5].answer)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the Quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
