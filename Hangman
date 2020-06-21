import random
from string import ascii_lowercase

def game():
    choices = ['python', 'java', 'kotlin', 'javascript']
    solution = random.choice(choices)
    unknown = list("-" * (len(solution)))
    shown = "".join(unknown)
    counter = 8
    tried = []
    while counter > 0:
        print()
        shown = "".join(unknown)
        print(shown)
        letter = input('Input a letter: ')
        if len(letter) != 1:
            print('You should input a single letter')
        elif letter in tried:
            print('You already typed this letter')
        elif letter not in ascii_lowercase:
            print('It is not an ASCII lowercase letter')
        elif letter in solution:
            tried.append(letter)
            for i in range(len(solution)):
                if letter == solution[i]:
                    unknown[i] = letter
        else:
            counter -= 1
            tried.append(letter)
            print('No such letter in the word')

    if shown == unknown:
        print('You guessed the word!')
        print('You survived!')
    else:
        print('You are hanged!')
            
print("H A N G M A N")
while True:
    menu = input('Type "play" to play the game, "exit" to quit: ')
    if menu == "play":
      game()
    elif menu == "exit":
        break
