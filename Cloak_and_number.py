import random
rules = print('\nThis is game of cloak and number!\nFirst you choose how many runs you want,\nthen you choose a number '
              'of your choice.\nWin to earn trophies!\n')
emoji = ['🍕','🍔','🍟','🍫','🍨','🌭','🥪','🌮','🌯','🥙','🍝','🍜','🥠','🥟','🍣'
         ]
random_emoji = random.choice(emoji)
emoji_count = []
emoji_found = True
from string import digits
while True:
    while True:
        chances = input('How many tries do you want?\n')
        if chances not in digits:
            print('Please enter a number! ')
            print()
            continue
        chances = int(chances)
        if chances <= 0:
            print('Please enter a number greater than 0')
            continue
        break
    random_number = random.randint(1, 100)
    is_found = False
    is_winner = False
    while chances != 0:
        current_number = input('Enter a number from 1 to 100:\n')
        if not current_number.isdigit():
            print('Please enter a number')
            continue
        str_number = int(current_number)
        if str_number > 100:
            print('Please enter a number from 1 to 100:\n')
            continue
        if str_number == random_number:
            print(f'You found it!\nThe number is {random_number}!')
            is_found = True
            break
        elif abs(str_number - random_number) <= 3:
            print('Just around the corner!')
            if str_number > random_number:
                print('Bit too high!')
            else:
                print('Bit too low!')
        elif abs (str_number - random_number) <= 5:
            print('So close!')
            if str_number > random_number:
                print('Bit too high!')
            else:
                print('Bit too low')
                
        elif abs(str_number - random_number) <= 10:
            print('It\'s close!')
            if str_number > random_number:
                print('But too high')
            else:
                print('But too low!')
                
        elif str_number < random_number:
            print('Too low!')
        else:
            print('Too high')
        chances -= 1
        print(f'Chances left: {chances}\n')
    if not is_found:
        print(f'You failed to find it !\n')
    else:
        is_winner = True
        prize = input('Want to reveal your prize ?!\n\nFor Yes press 1,\nFor No press 2\n')
        if prize not in digits:
            print('No cookie for you, you didn\'t choose one of the options above!')
        elif prize == '1':
            for i in (emoji):
                if i not in emoji_count:
                    print(f'Here something for your journey!\n{i}')
                    emoji_count.append(i)
                    break
            if len(emoji_count) != 0:
                print(f'Your trophies so far: {"".join(emoji_count)}')
        elif prize == '2':
            print('No trophie for  you ! ')
        else:
            print('No cookie for you, you didn\'t choose one from the options above!')
    if len(emoji_count) == len(emoji):
        print("Wow! You've collected all trophies!")
        exit()
    try_again = int(input('Do you wish to try again?!\nFor Yes press 1,\nFor No press 2\n'))
    if try_again != 1:
        print('Thanks for playing!\n')
        exit()