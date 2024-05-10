from random import randint

L_results = ['Five of a kind', 'Four of a kind', 'Full house', 'Straight', 'Three of a kind', 'Two pair', 'One pair',
             'Bust']
L_type = ['Ace', 'King', 'Queen', 'Jack', '10', '9']


def roll_put():
    L = []
    for _ in range(5):
        L.append(randint(0, 5))
    L.sort()
    for i in range(5):
        L[i] = L_type[L[i]]
    return L


def judge(L):
    L_judge = []
    L_len = len(L)
    i = 0
    while i < len(L):
        j = i + 1
        while j < len(L):
            if L[i] == L[j]:
                if L[j] not in L_judge:
                    L_judge.append(L[j])
                L_len -= 1
                j += 1
            else:
                break
        i = j
    if L_len == 5:
        for i in range(len(L)-1):
            if L[0] == 0:
                if L[i] != (L[i+1]-1):
                    return 7
            elif L[0] == 'Ace':
                if L[i] != L_type[L_type.index(L[i])+1]:
                    return 7
        return 3
    elif L_len == 4:
        return 6
    elif L_len == 3:
        if len(L_judge) == 1:
            return 4
        else:
            return 5
    elif L_len == 2:
        if len(L_judge) == 1:
            return 1
        else:
            return 2
    else:
        return 0


def print_roll(L):
    S_print = ''
    for n in L:
        S_print = S_print + ' ' + n
    print('The roll is:' + S_print)


def change_dice(dice_choice, L):
    if dice_choice == '':
        return roll_put()
    L_dice_choice = dice_choice.split(' ')
    if len(L_dice_choice) == 1 and (L_dice_choice[0] == 'all' or L_dice_choice[0] == 'All'):
        return L_dice_choice
    for i in L_dice_choice:
        if i not in L:
            return []
    if len(L_dice_choice) == 5:
        return L
    return L_dice_choice


def reroll(short_L):
    for i in range(len(short_L)):
        short_L[i] = L_type.index(short_L[i])
    for _ in range(len(short_L), 5):
        short_L.append(randint(0, 5))
    short_L.sort()
    for i in range(5):
        short_L[i] = L_type[short_L[i]]
    return short_L


def play():
    L = roll_put()
    print_roll(L)
    print('It is a', L_results[judge(L)])
    dice_choice = input('Which dice do you want to keep for the second roll? ')
    L_change = change_dice(dice_choice, L)
    while (L_change == []):
        dice_choice = input('That is not possible, try again!\nWhich dice do you want to keep for the second roll? ')
        L_change = change_dice(dice_choice, L)
    if L_change[0].lower() == 'all' or L_change is L:
        print('Ok, done.')
    else:
        if len(L_change) < 5:
            L_change = reroll(L_change)
        print_roll(L_change)
        print('It is a', L_results[judge(L_change)])
        dice_choice = input('Which dice do you want to keep for the third roll? ')
        L_change = change_dice(dice_choice, L)
        while (L_change == []):
            print('That is not possible, try again!\nWhich dice do you want to keep for the second roll? ')
            L_change = change_dice(dice_choice, L)
        if L_change[0].lower() == 'all' or L_change is L:
            print('Ok, done.')
        else:
            L_change = reroll(L_change)
            print_roll(L_change)
            print('It is a', L_results[judge(L_change)])


def simulate(n):
    num_str = ''
    for _ in range(n):
        L = []
        for _ in range(5):
            L.append(randint(0, 5))
        L.sort()
        num_str += str(judge(L))
    for i in range(7):
        print(L_results[i] + ' ' * (15 - len(L_results[i])) + ':', '%.2f' % (num_str.count(str(i)) / n * 100) + '%')
