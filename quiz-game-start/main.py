from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
"""
   Dictionary's inside a list. How to loop through it??
   ****************************************************
   Union[dict[str, str], dict[str, str], dict[str, str], dict[str, str]]
   For example , question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"}]
   first of all -->lets divide the components.

   One list --> Many dictionaries --> each dictionary will have a key-value.
   So, list1 = [ {dict1 --> key:value}, {dict2 --> key:value}, {dict3 --> key:value} ]

   If you want to retrieve the dictionary values, you need to do -->
   1) ACCESS THE LIST.
         for items in list: --> items here are the dictionaries -->dict1,dict2,dict3
   2) ACCESS THE DICTIONARIES USING "Items".
         for values of dictionary --> 
            values_of_1stKey = items["1st key"]

         Suppose in the dictionary we have more than one "Key- Value" pair -->
            Then, simply keep oon adding --> values_of_2ndKey = items["2nd Key"]

   """

question_bank = []

#ACCESS THE LIST
for question in question_data:
   # ACCESS THE DICTIONARIES USING "Items".
   question_text = question["text"]
   question_answer = question["answer"]

   # Converting each of these values(question_text,question_answer) into object which has now
   # all of that data in a very easy and fool proof way of accessing
   new_question = Question(question_text,question_answer)

   question_bank.append(new_question)

qb = QuizBrain(question_bank)
# qb.next_question()

while qb.still_has_questions():
   final_score = qb.next_question()



print(f"Your final score is {final_score}/{qb.question_number}")





