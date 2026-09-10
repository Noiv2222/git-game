"""
Python Quiz Game
-----------------
An interactive quiz game for beginners.

Concepts demonstrated:
- Variables
- Conditional statements (if / elif / else)
- Loops (for)
- Functions
- Basic scoring and feedback system
"""

import random
import time


# ---------------------------------------------------------
# Quiz Data
# ---------------------------------------------------------
questions = [
    {
        "question": "What does 'print()' do in Python?",
        "options": ["A) Deletes a variable", "B) Displays output on the screen",
                    "C) Creates a loop", "D) Stops the program"],
        "answer": "B"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A) //", "B) <!-- -->", "C) #", "D) **"],
        "answer": "C"
    },
    {
        "question": "What data type is the value True?",
        "options": ["A) String", "B) Integer", "C) Float", "D) Boolean"],
        "answer": "D"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A) func", "B) def", "C) function", "D) lambda"],
        "answer": "B"
    },
    {
        "question": "What will 'len([1, 2, 3])' return?",
        "options": ["A) 2", "B) 3", "C) 4", "D) Error"],
        "answer": "B"
    },
    {
        "question": "Which loop is used to repeat code a fixed number of times?",
        "options": ["A) while", "B) if", "C) for", "D) do-while"],
        "answer": "C"
    },
    {
        "question": "What is the output of '10 % 3' in Python?",
        "options": ["A) 3", "B) 1", "C) 0", "D) 3.33"],
        "answer": "B"
    },
]


# ---------------------------------------------------------
# Functions
# ---------------------------------------------------------
def welcome_message():
    """Prints an introduction to the quiz."""
    print("=" * 50)
    print("        WELCOME TO THE PYTHON QUIZ GAME")
    print("=" * 50)
    print("Answer each question by typing A, B, C, or D.")
    print("Let's test your knowledge!\n")
    time.sleep(1)


def ask_question(question_data, question_number):
    """Displays a single question and returns True if answered correctly."""
    print(f"Q{question_number}: {question_data['question']}")
    for option in question_data["options"]:
        print("   " + option)

    user_answer = input("Your answer: ").strip().upper()

    if user_answer == question_data["answer"]:
        print("Correct! ✅\n")
        return True
    else:
        correct = question_data["answer"]
        print(f"Wrong! ❌ The correct answer was {correct}.\n")
        return False


def show_result(score, total):
    """Displays final score and feedback based on performance."""
    print("=" * 50)
    print(f"You scored {score} out of {total}!")

    percentage = (score / total) * 100

    if percentage == 100:
        feedback = "Perfect score! You're a Python pro! 🏆"
    elif percentage >= 70:
        feedback = "Great job! You really know your stuff. 👏"
    elif percentage >= 40:
        feedback = "Not bad! A little more practice and you'll master it. 💪"
    else:
        feedback = "Keep learning! Practice makes perfect. 📘"

    print(feedback)
    print("=" * 50)


def play_again():
    """Asks the user if they want to play another round."""
    choice = input("\nDo you want to play again? (yes/no): ").strip().lower()
    return choice == "yes"


# ---------------------------------------------------------
# Main Game Loop
# ---------------------------------------------------------
def main():
    welcome_message()
    keep_playing = True

    while keep_playing:
        score = 0
        shuffled_questions = random.sample(questions, len(questions))

        for i, q in enumerate(shuffled_questions, start=1):
            if ask_question(q, i):
                score += 1

        show_result(score, len(shuffled_questions))
        keep_playing = play_again()

    print("\nThanks for playing the Python Quiz Game! Goodbye 👋")


if __name__ == "__main__":
    main()
