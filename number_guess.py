import random
import art

easy = 10
hard = 5

def check(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")
        return -1

def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return easy
    elif level == "hard":
        return hard
    else:
        print("Invalid input, choose again.")
        return difficulty()

def game():
    print(art.guess_logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    print(answer)
    turns = difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check(guess, answer, turns)
        if turns > 0:
            print("Guess again.")
            continue
        elif turns == 0:
            again = int(input("You've run out of guesses, you lose. Do you want to play again? (yes - 1/no - *): "))
            if again == 1:
                game()
            else:
                break
        elif turns == -1:
            again = int(input("Do you want to play again? (yes - 1/no - *): "))
            if again == 1:
                game()
            else:
                print("Goodbye!")
                break

game()