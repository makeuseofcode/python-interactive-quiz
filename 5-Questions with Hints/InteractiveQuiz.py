class Question:
    def __init__(self, questionText, answer, hint=None, multipleChoiceOptions=None, alternateAnswers=None):
        self.questionText = questionText
        self.answer = answer
        self.hint = hint
        self.multipleChoiceOptions = multipleChoiceOptions
        self.alternateAnswers = alternateAnswers
 
    def __repr__(self):
        return '{'+ self.questionText +', '+ self.answer +', '+ self.hint +', '+ str(self.multipleChoiceOptions) +', '+ str(self.alternateAnswers) +'}'


quizQuestions = [
    Question("Question 1. What city is the capital of Australia", "Canberra", "Starts with a C"),
    Question("Question 2. What city is the capital of Japan", "Tokyo", "Starts with a T"),
    Question("Question 3. How many islands does the Philippines have", "7100", "A number between 7000 and 8000"),
    Question("Question 4. Which country takes the most land mass", "b", "The country spans two continents", ["(a) United States", "(b) Russia", "(c) Australia", "(d) Antarctica"]),
    Question("Question 5. What hemisphere is Japan located in", "Northern Hemisphere", "The top half of Earth", [], ["north", "northern"]),
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
    count = 0
    while(userInput.lower() != question.answer.lower()):
        if(question.alternateAnswers != None and userInput.lower() in question.alternateAnswers):
            break;
        count = count + 1
        if (count >= 3):
            print(f"Hint: {question.hint}.")
            userInput = input()
        else:
            print("That is not correct, try again.")
            userInput = input()
        
    print("That is correct!")