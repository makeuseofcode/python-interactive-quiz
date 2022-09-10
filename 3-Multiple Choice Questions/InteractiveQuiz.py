class Question:
    def __init__(self, questionText, answer, multipleChoiceOptions=None):
        self.questionText = questionText
        self.answer = answer
        self.multipleChoiceOptions = multipleChoiceOptions
 
    def __repr__(self):
        return '{'+ self.questionText +', '+ self.answer +', '+ str(self.multipleChoiceOptions) +'}'
        
quizQuestions = [
    Question("Question 1. What city is the capital of Australia", "Canberra"),
    Question("Question 2. What city is the capital of Japan", "Tokyo"),
    Question("Question 3. How many islands does the Philippines have", "7100"),
    Question("Question 4. Which country takes the most land mass", "b", ["(a) United States", "(b) Russia", "(c) Australia", "(d) Antarctica"]),
] 

print("\nHello, welcome to the geography quiz. Type in the answer to the given questions as they are presented.\n")

for question in quizQuestions:
    if (question.multipleChoiceOptions != None):
        print(f"{question.questionText}?")
        for option in question.multipleChoiceOptions:
            print(option)
        userInput = input()  
    else:
        print(f"{question.questionText}?")
        userInput = input()
        
    if (userInput.lower() == question.answer.lower()):
        print("That is correct!")
    else:
        print(f"Sorry, the correct answer is {question.answer}.") 