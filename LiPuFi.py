import random

def find_life_purpose():
    # Dictionary containing different categories of questions
    questions = {
        "General": [
            "What makes me feel most fulfilled?",
            "What fascinates me?",
            "What do I want to be associated with?",
            "What challenges do I want to take on?",
            "What motivates me to take action?"
        ],
        "Reflection": [
            "What makes me feel fulfilled?",
            "What role is most important to me?",
            "What gives me a sense of purpose in life?",
            "What will I consider the greatest success in my life?",
            "What lesson have I learned from my past experiences?"
        ],
        "Passion": [
            "What brings me joy regardless of reward?",
            "What is my greatest talent?",
            "In which field do I feel most creative?",
            "What do I do when no one is around?",
            "What would I like to do for the rest of my life?"
        ],
        "Mission": [
            "What problem in the world do I want to solve?",
            "Which of my skills could help others?",
            "What is my role in society?",
            "How can I contribute to improving the situation in my environment?",
            "How do I want to leave a mark on history?"
        ]
    }
    
    # User prompt
    print("Please answer each question in 1-5 words.")
    
    # List to store answers
    answers = []
    
    # Iterating through categories
    for category in ["General", "Reflection", "Passion", "Mission"]:
        # Randomly choose a question from the category
        question = random.choice(questions[category])
        
        # User interaction - collecting answers (one word)
        answer = input(f"{question} ").upper()  # Convert user input to uppercase
        answers.append((category, answer))
        
        # Remove the chosen question from the list to avoid repetition
        questions[category].remove(question)
    
    # Prepare expanded answers
    passion = f"exploring passion for {answers[2][1]}"
    reflection = f"reflecting on {answers[1][1]}"
    realization1 = f"realizing {answers[3][1]}"
    realization2 = f"to being able to {answers[0][1]}"
    
    # Create the sentence based on the answers
    sentence = f"Find harmony between {passion}, \n{reflection}, \n{realization1}, \n{realization2}."
    
    # Display user's answers
    print(sentence)

# Run the script
find_life_purpose()
