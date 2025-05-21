import random
while True:
    chances = int(input('How many tries do you want?\n'))
    if chances <= 0:
        print('Please enter a number greater than 0')
        continue
    break
while True:
    random_number = random.randint(1, 100)
    is_found = False

    while chances != 0:
        current_number = input('Enter a number from 1 to 100:\n')
        if not current_number.isdigit():
            print('Please enter a number')
            continue
        str_number = int(current_number)
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
    if not is_found:
        print('You failed to find it !\n')
    else:
        print(f'You won!\nThe number is {random_number}!')
    try_again = int(input('Do you wish to try again?!\nFor Yes press 1,\nFor No press 2\n'))
    if try_again != 1:
        print('Thanks for playing!\n')
        exit()