print("Hello, welcome to the geography quiz. Answer the questions as they are presented.")

print("Question 1. What city is the capital of Australia?")
userInput = input()

if (userInput.lower() == "Canberra".lower()):
    print("That is correct!")
else:
    print("Sorry, the correct answer is Canberra.")