class Quiz:
    def __init__(self):
        self.questions = [
            ["What is the capital of France?", "Paris"],
            ["What is 5 + 3?", "8"],
            ["Which language is used for web apps?", "Python"]
        ]
        self.score = 0

    def run_quiz(self):
        print("Welcome to the Quiz!\n")

        for question in self.questions:
            user_answer = input(question[0] + " ")
            if user_answer.strip().lower() == question[1].lower():
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {question[1]}.\n")

        print(f"You got {self.score} out of {len(self.questions)} correct!")

quiz = Quiz()
quiz.run_quiz()class Quiz:
    def __init__(self):
        self.questions = [
            ["What is the capital of France?", "Paris"],
            ["What is 5 + 3?", "8"],
            ["Which language is used for web apps?", "Python"]
        ]
        self.score = 0

    def run_quiz(self):
        print("Welcome to the Quiz!\n")

        for question in self.questions:
            user_answer = input(question[0] + " ")
            if user_answer.strip().lower() == question[1].lower():
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {question[1]}.\n")

        print(f"You got {self.score} out of {len(self.questions)} correct!")

quiz = Quiz()
quiz.run_quiz()