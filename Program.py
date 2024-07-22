import random
import time

def number_guessing_game():
    play_again = 'y'
    
    while play_again.lower() == 'y':
        print("Hi! Welcome to the number guessing game.")
        time.sleep(1)
        
        print("Choose a difficulty level:")
        print("1. Easy (1 to 50)")
        print("2. Medium (1 to 100)")
        print("3. Hard (1 to 200)")
        level = int(input("Enter the level number: "))
        
        if level == 1:
            max_number = 50
        elif level == 2:
            max_number = 100
        elif level == 3:
            max_number = 200
        else:
            print("Invalid choice. Starting with Medium level.")
            max_number = 100
        
        print(f"I am going to pick a number between 1 and {max_number}.")
        time.sleep(2)
        print("Picking a number....")
        time.sleep(2)
        correct_answer = random.randint(1, max_number)
        guess_count = 0
        max_guesses = 10

        while guess_count < max_guesses:
            guess = int(input("What is your guess?: "))
            guess_count += 1
            
            if guess == correct_answer:
                print(f"Congrats!! The correct answer is {correct_answer}. It took you {guess_count} guesses.")
                break
            else:
                if guess < correct_answer:
                    print("Wrong. You need to guess higher.")
                else:
                    print("Wrong. You need to guess lower.")
                
                print(f"You have {max_guesses - guess_count} guesses left.")
        
        if guess_count == max_guesses:
            print(f"Sorry, you've used all your guesses. The correct answer was {correct_answer}.")
        
        play_again = input("Do you want to play again? (y/n): ")

    print("Thanks for playing! See you next time.")

number_guessing_game()
