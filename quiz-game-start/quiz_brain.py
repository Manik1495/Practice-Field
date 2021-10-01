class QuizBrain:

    def __init__(self, q_list):
        print(q_list)
        self.question_number = 0
        self.question_list = q_list
        self.score = 0


    def still_has_questions(self):
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False
        return self.question_number < len(self.question_list)




    def next_question(self):

        """
        Step to get the first object from the list of objects -->question_list
        """
        current_question = self.question_list[self.question_number]
        # print(current_question.text)
        self.question_number += 1
        user_choice = input(f"Q.{self.question_number}: {current_question.text} (True/False)?:")

        self.check_answer(user_choice,current_question.answer)
        str_score = str(self.score)
        str_question_number = str(self.question_number)
        return self.score


    def check_answer(self, user_answer, current_answer):
        if user_answer == current_answer:
            print("You got it right!!")
            print(f"The correct answer was : {current_answer}")
            self.score += 1
            print(f"score is {self.score}/{self.question_number}")
            print("\n")
        else:
            print("that's wrong answer!!")
            print(f"The correct answer was : {current_answer}")
            print(f"score is {self.score}/{self.question_number}")
            print("\n")


        # for ques in self.question_list:
        #     self.question_number = self.question_list.index(ques) + 1
        #     print(self.question_number)
        #     ques_answer = ques.answer
        #     user_choice = input(f"Q.{self.question_number}: {ques.text}. (True/False)?:")
        #     user_score = 0
            # if user_choice == ques_answer:
            #     print("You got it right!!")
            #     print(f"The correct answer was : {ques.answer}")
            #
            #     print()