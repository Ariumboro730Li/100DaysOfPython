class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.is_answer_right = True
        self.score = 0
        self.answer = ""

    def next_question(self):
        current_question = self.question_list[self.question_number]
        question = current_question.text
        self.answer = current_question.answer
        user_answer = input(f"Q.{self.question_number + 1}: {question} True/False ? {self.answer}  \n")
        self.check_answer(user_answer, self.answer)
        self.question_number += 1

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, real_answer):
        self.is_answer_right = user_answer.lower() == real_answer.lower()
        if self.is_answer_right:
            self.score += 1

    def print(self):
        if self.is_answer_right:
            return f"You got it right"
        else:
            return f"You got it wrong, the answer is {self.answer}"