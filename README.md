# Number Guessing Game Project

Welcome to the Number Guessing Game! This is a simple and fun game where you try to guess the number the computer has picked within a specified range and limited number of guesses. Enjoy challenging yourself and see how quickly you can guess the correct number.

## Game Features

- **Difficulty Levels:** Choose between Easy (1-50), Medium (1-100), and Hard (1-200).
- **Guess Limit:** Each game allows you up to 10 guesses.
- **Engaging Messages:** Interactive messages guide you through the game.

## How to Play

1. **Start the Game:** Run the script to begin the game.
2. **Select Difficulty Level:** Choose from Easy, Medium, or Hard by entering the corresponding number.
3. **Make Guesses:** Enter your guess when prompted.
4. **Feedback:** The game will tell you if your guess is too high or too low.
5. **Win or Lose:** Guess the correct number within the allowed attempts to win. If you use all your guesses, the correct number will be revealed.

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com//number-guessing-game.git
   ```

2. Navigate to the project directory:

   ```sh
   cd number-guessing-game
   ```

3. Run the game:

   ```sh
   python guessing_game.py
   ```

## Code Example

Here's a snippet of the main game loop:

```python
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
```

## Contributing

Contributions are what make the open-source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Contact

NANDAN S - nandans123456321@gmail.com

Project Link: [https://github.com/your-username/number-guessing-game](https://github.com/your-username/number-guessing-game)
```

This `README.md` provides an overview of the game, instructions on how to play, and steps to get the project up and running. You can customize the contact information and project link as needed.
