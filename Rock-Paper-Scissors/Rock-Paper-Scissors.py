import random
# For implementing rankings and score remove the comments '#'
# rate = open('rating.txt', 'r')

name = input('Enter your name: ')
print(f'Hello, {name}')

# rate_list = rate.readlines()
# if name in rate_list:
#     score = int(rate_list[rate_list.index(name) + 1].replace('\n', ''))
# else:
#     score = 0

options = input().split(',')
# Default rules: rock, paper, scissors rules.
# Other classic rules: rock,paper,scissors,lizard,spock
# Advanced rules: rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire
if len(options) <= 1:
    option = ['rock', 'scissors', 'paper']
    win = {'rock':'scissors', 'scissors':'paper', 'paper':'rock'}
else:
    option = options
    win = {}
    for i in range(len(option)):
        shifting_options = []
        winners = []
        inicio = i - (int(len(option) // 2))
        final = i + (int(len(option) // 2)) + 1
        shifting_options = option[inicio:] + option[:final] 
        winners = shifting_options[:int(len(option) // 2)]
        win.update({option[i] : winners})

print("Okay, let's start")
while True:
    userinp = input()
    if userinp == '!exit':
        print('Bye!')
        break
#     elif userinp == '!rating':
#         print(f'Your rating: {score}')
    elif userinp not in option:
        print('Invalid input')
    else:
        compinp = random.choice(option)

        if userinp == compinp:
            print(f'There is a draw ({compinp})')
#             score += 50
        elif compinp not in win[userinp]:
            print(f'Sorry, but computer chose {compinp}')
        else:
            print(f'Well done. Computer chose {compinp} and failed')
#             score += 100

