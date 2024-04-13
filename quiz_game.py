class QuizGame:
    def __init__(self):  
        self.questions = [
            {"question": "1)Who won the First IPL Tile?", "options":["A)Deccan Chargers","B)Chennai Super kings","C)Mumbai Indians","D)Rajasthan Royals"], "answer": "D"},
            {"question": "2)Who was captain of Chennai Super Kings in 2008 to 2023?", "options":["A)Ravindra Jadeja","B)Micheal Hussy","C)Mahendra Singh Dhoni","D)Ruturaj Gaikwad"], "answer": "C"},
            {"question": "3)Who is the player to reach the first 5000 runs in IPL?", "options":["A)Suresh Raina","B)Rohit Sharma","C)Virat Kohli","D)Shikhar Dhawan"], "answer": "A"},
            {"question": "4)How many times did CSK win the IPL Trophy?", "options":["A)4","B)5","C)3","D)2"], "answer":"B"},
            {"question": "5)Who was the Orange Cap holder in 2021?", "options": ["A)Ruturaj Gaikwad","B)Virat Kohli","C)FaF Du Plessis","D)Shubhanm Gill"], "answer":"A"},
            {"question": "6)Which color cap is awarded to the player taking the most wicket in the tournament?", "options":["A)Green","B)Orange","C)Red","D)Purple"], "answer":"D"},
            {"question": "7)How many teams currently participate in the IPL?", "options":["A)8","B)6","C)9","D)10"], "answer":"D"},
            {"question": "8)What is the maximum number of foreign players allowed in an IPL playing XI?", "options":["A)3","B)2","C)4","D)6"], "answer":"C"},
            {"question": "9)Which player holds the record for the most number of sixes hit in the IPL?", "options":["A)Chris Gayle","B)AB de Villiers","C)Kieron Pollard","D)MS Dhoni"], "answer":"D"},
            {"question": "10)What is the highest individual score ever recorded in an IPL match?", "options":["A)175 by Chris Gayle","B)180 by Rohit Sharma","C)185 by Virat Kohli","D)200 by MS Dhoni"], "answer":"A"}
        ]
        self.score = 0

    def ask_question(self, question):
        print(question["question"])
        for option in question["options"]:
            print(option)
        player_answer = input("Enter your answer (A/B/C/D): ").upper()
        if player_answer == question["answer"]:
            print("Correct!")
            self.score += 10
        else:
            print("Incorrect. The correct answer is:", question["answer"])        

    def start_game(self):
        print("Welcome to the IPL Quiz Game!")
        print("Intruction:")
        print("Each Question Carry 10 mark")
        print("Quiz Begins:")
        for question in self.questions:
            self.ask_question(question)
        print("Game over! Your score is 100 out of:", self.score);


if __name__ == "__main__":
    quiz = QuizGame()
    quiz.start_game() 

print("Please Give The Feedback")
Feedback=input("Feedback: ")
print("Thank You for your Feedback")     



