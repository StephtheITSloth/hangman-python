# Write your code here
import random
import string

def init_game():    
    words = ['python', 'java', 'swift', 'javascript']
    secret_word = random.choice(words)
    hidden_word = "-" * len(secret_word)
    secret_word_set = set(secret_word)
    return (hidden_word, secret_word, secret_word_set)
    
def game_logic():
    hidden_word, secret_word, secret_word_set = init_game()
    num_attempt = 8
    letter_guessed = set()

    while num_attempt > 0:
        if hidden_word == secret_word: # ------ == python
            print(hidden_word)
            return (num_attempt, secret_word, hidden_word)
            
        while True:
            print(f"\n{''.join(hidden_word)}")
            attempt = input("Input a letter: ")
            if attempt == None or attempt == "":
                print("Please, input a single letter\n")
            elif attempt in string.ascii_uppercase or attempt in string.digits or attempt in string.whitespace or attempt in string.punctuation:
                print("Please, enter a lowercase letter from the English alphabet.\n")
            elif len(attempt) != 1:
                print("Please, input a single letter\n")
            elif attempt in letter_guessed:
                print("You've already guessed this letter.\n")
            elif attempt in string.ascii_lowercase:
                break
                
        letter_guessed.add(attempt)
        if attempt in secret_word:
            idx = secret_word.index(attempt)
            hidden_word = list(hidden_word) 
            hidden_word[idx] = attempt

            for i in range(idx + 1, len(secret_word)):
                if attempt == secret_word[i]:
                    hidden_word[i] = attempt
            hidden_word = "".join(hidden_word)
        elif attempt not in secret_word:
            print("That letter doesn't appear in the word.")
            num_attempt -= 1
    return (num_attempt, secret_word, hidden_word)
        
if __name__== '__main__':
    print("H A N G M A N  # 8 attempts")
    win = 0
    lost = 0
    while True:
        menu_action = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
        if menu_action == "exit":
            break
        elif menu_action == "play":
            num_attempt, secret_word, hidden_word = game_logic()
            if num_attempt == 0 and hidden_word != secret_word:
                print("\nYou lost!")
                lost += 1
            elif hidden_word == secret_word:
                print(f"\nYou guessed the word {secret_word}!")
                print("\nYou survived!")
                win += 1
        elif menu_action == "results":
            print(f"You won: {win} times.")
            print(f"You lost: {lost} times")
        
    
    
    
# Write your code here
