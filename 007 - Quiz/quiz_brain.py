class QuizBrain:
    def __init__(self, list_input) -> None:
        self.question_num = 0
        self.question_list = list_input
        self.score = 0

    def still_has_questions(self):
        if self.question_num < len(self.question_list):
            return True
        print("You've completed the quiz!🎉")
        print(f"Your final score was {self.score}/{self.question_num}")

    def check_answer(self, question, user_answer):
        if question.answer.lower() == user_answer.lower():
            self.score += 1
            print("Correct! 🥳")
        else:
            print("Wrong. 😢")
        print(f"Score: {self.score}/{self.question_num}\n")

    def next_question(self):
        question = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q.{self.question_num}: {question.text}? True/False: ")
        print()
        self.check_answer(question, user_answer)
