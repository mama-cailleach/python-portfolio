def get_questions():
    return [
        {
            "question": "Which country won the first-ever Cricket World Cup in 1975?",
            "choices": ["Australia", "West Indies", "India", "England"],
            "answer": "West Indies"
        },
        {
            "question": "How many balls are there in an over in cricket?",
            "choices": ["4", "5", "6", "8"],
            "answer": "6"
        },
        {
            "question": "Who has the most international runs in cricket?",
            "choices": ["Sachin Tendulkar", "Virat Kohli", "Ricky Ponting", "Jacques Kallis"],
            "answer": "Sachin Tendulkar"
        },
        {
            "question": "What is the term for a delivery that dismisses a batsman without scoring any runs?",
            "choices": ["Golden Duck", "Silver Duck", "Bronze Duck", "Platinum Duck"],
            "answer": "Golden Duck"
        }
    ]

def ask_question(q, num):
    print(f"\nQuestion {num}: {q['question']}")
    for idx, choice in enumerate(q["choices"], 1):
        print(f"  {idx}. {choice}")
    while True:
        try:
            answer = int(input("Your answer (enter the number): "))
            if 1 <= answer <= len(q["choices"]):
                return q["choices"][answer - 1]
            else:
                print("Please enter a valid option number.")
        except ValueError:
            print("Please enter a number.")

def main():
    questions = get_questions()
    score = 0
    print("Welcome to the Cricket Quiz!\n")
    for idx, q in enumerate(questions, 1):
        user_answer = ask_question(q, idx)
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was: {q['answer']}")
    print(f"\nQuiz finished! Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    main()
