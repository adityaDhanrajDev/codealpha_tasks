import random
import os

class HangmanGame:
    def __init__(self):
        # Word categories
        self.word_categories = {
            "Animals": ["elephant", "giraffe", "kangaroo", "penguin", "dolphin", "octopus"],
            "Fruits": ["strawberry", "blueberry", "watermelon", "pineapple", "mango", "apricot"],
            "Countries": ["canada", "australia", "germany", "japan", "brazil", "egypt"],
            "Sports": ["football", "basketball", "baseball", "tennis", "cricket", "hockey"]
        }
        
        self.max_attempts = 6
        self.current_word = ""
        self.word_display = []
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.category = ""
    
    def clear_screen(self):
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def select_word(self):
        """Select a random word from a random category"""
        self.category = random.choice(list(self.word_categories.keys()))
        self.current_word = random.choice(self.word_categories[self.category])
        self.word_display = ['_' for _ in self.current_word]
    
    def display_hangman(self):
        """Display the hangman ASCII art"""
        stages = [
            """
               --------
               |      |
               |      
               |    
               |      
               |     
               -
            """,
            """
               --------
               |      |
               |      O
               |    
               |      
               |     
               -
            """,
            """
               --------
               |      |
               |      O
               |      |
               |      
               |     
               -
            """,
            """
               --------
               |      |
               |      O
               |     /|
               |      
               |     
               -
            """,
            """
               --------
               |      |
               |      O
               |     /|\\
               |      
               |     
               -
            """,
            """
               --------
               |      |
               |      O
               |     /|\\
               |     / 
               |     
               -
            """,
            """
               --------
               |      |
               |      O
               |     /|\\
               |     / \\
               |     
               -
            """
        ]
        return stages[self.wrong_guesses]
    
    def display_game_state(self):
        """Display current game state"""
        self.clear_screen()
        print("\n" + "="*50)
        print("🎮 HANGMAN GAME 🎮")
        print("="*50)
        print(f"\nCategory: {self.category}")
        print(self.display_hangman())
        print(f"\nWord: {' '.join(self.word_display)}")
        print(f"\nGuessed letters: {', '.join(sorted(self.guessed_letters)) if self.guessed_letters else 'None'}")
        print(f"Wrong guesses: {self.wrong_guesses}/{self.max_attempts}")
        print("-"*50)
    
    def get_guess(self):
        """Get and validate player's guess"""
        while True:
            guess = input("\nGuess a letter: ").lower().strip()
            
            if len(guess) != 1:
                print("Please enter a single letter!")
                continue
            
            if not guess.isalpha():
                print("Please enter a valid letter!")
                continue
            
            if guess in self.guessed_letters:
                print(f"You already guessed '{guess}'. Try another letter!")
                continue
            
            return guess
    
    def process_guess(self, guess):
        """Process the player's guess and update game state"""
        self.guessed_letters.add(guess)
        
        if guess in self.current_word:
            # Correct guess
            for i, letter in enumerate(self.current_word):
                if letter == guess:
                    self.word_display[i] = guess
            return True
        else:
            # Wrong guess
            self.wrong_guesses += 1
            return False
    
    def check_win(self):
        """Check if player has won"""
        return '_' not in self.word_display
    
    def play_again(self):
        """Ask if player wants to play again"""
        while True:
            choice = input("\nWould you like to play again? (y/n): ").lower().strip()
            if choice in ['y', 'yes']:
                return True
            elif choice in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' or 'n'")
    
    def play(self):
        """Main game loop"""
        print("\nWelcome to Hangman!")
        print("Try to guess the word letter by letter.")
        print(f"You have {self.max_attempts} wrong guesses allowed.\n")
        
        while True:
            # Reset game for new round
            self.select_word()
            self.guessed_letters = set()
            self.wrong_guesses = 0
            
            # Main game loop
            while self.wrong_guesses < self.max_attempts:
                self.display_game_state()
                guess = self.get_guess()
                
                if self.process_guess(guess):
                    print(f"\n✓ Good guess! '{guess}' is in the word!")
                    if self.check_win():
                        self.display_game_state()
                        print(f"\n🎉 CONGRATULATIONS! You won! 🎉")
                        print(f"The word was: {self.current_word.upper()}")
                        break
                else:
                    print(f"\n✗ Sorry, '{guess}' is not in the word!")
                
                input("\nPress Enter to continue...")
            
            # Check if player lost
            if self.wrong_guesses == self.max_attempts:
                self.display_game_state()
                print(f"\n💀 GAME OVER! You lost! 💀")
                print(f"The word was: {self.current_word.upper()}")
            
            # Ask to play again
            if not self.play_again():
                print("\nThanks for playing Hangman! Goodbye! 👋")
                break

# Run the game
if __name__ == "__main__":
    game = HangmanGame()
    game.play()
