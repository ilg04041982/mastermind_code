import random

from datetime import datetime


size, digits = 4, 6


def computer_num(size, digits):
    list_nums = list(range(digits))
    res = ''
    i = 0
    while list_nums and i < size:
        elem = random.choice(list_nums)
        if res == '' and elem == 0:
            continue
        res += str(elem)
        list_nums.remove(elem)
        i += 1
    return int(res)


comp_number = computer_num(size, digits)

comp_num = str(comp_number)

def match(comp_num, your_num):
    correct, so_so = 0, 0
    common = [x for x in comp_num if x in your_num]
    matched_nums = []
    if your_num == comp_num:
        correct += len(your_num)
    else:
        for i in range(len(your_num)):
            if comp_num[i] == your_num[i]:
                correct += 1
                matched_nums.append(your_num[i])
        for s in common:
            if comp_num.index(s) != your_num.index(s) and s not in matched_nums:
                so_so += 1
    return correct, so_so


def convert_string_to_a_list_of_strings(Str):
    list1 = []
    list1[:0] = Str
    return list1


def findDup(Str):
    convert = convert_string_to_a_list_of_strings(Str)
    List_of_ints = [int(item) for item in convert]
    List_of_ints.sort()
    Duplicates_list = []
    for i in range(0, len(List_of_ints) - 1):
        if List_of_ints[i] == List_of_ints[i+1]:
            Duplicates_list.append(List_of_ints[i])
    return Duplicates_list


def not_accepted_digits(Str, digit_list):
    string_list = [str(item) for item in digit_list]
    Not_accepted_digits = []
    for i in range(len(Str)):
        if Str[i] not in string_list and Str[i] not in Not_accepted_digits:
            Not_accepted_digits.append(Str[i])
    return Not_accepted_digits


def detect_letters_in_str(Str):
    count = 0
    for s in Str:
        if (s.isalpha()) == True:
            count += 1
    return count


your_num = input('Mastermind game: duplicate: no, num of digits: 4, choices per digits: 0, 1, 2, 3, 4, 5 enter your number please:')
start_time = datetime.now()



if your_num == comp_num:
    print('Congratulations, you guessed the number in just 1 try')
else:
    ctr = 0
    while your_num != comp_num:
        ctr += 1
        detect_letters = detect_letters_in_str(your_num)
        if detect_letters > 0:
            print("Sorry, we don't play with letters")
            your_num = input('Enter your next choice of numbers: ')
        elif detect_letters == 0:
            computer_test = match(comp_num, your_num)
            Not_accepted_digits = not_accepted_digits(your_num, list(range(digits)))
            find_dup = findDup(your_num)
            if len(Not_accepted_digits) == 1:
                print('hmnn ', Not_accepted_digits[0], 'is not an option.')
                your_num = input('Enter your next choice of numbers: ')
            elif len(Not_accepted_digits) > 1:
                print('Sorry, but ', Not_accepted_digits[:], 'are not options')
                your_num = input("Enter your next choice of numbers: ")
            elif len(find_dup) > 0:
                print('No duplication, as indicated above')
                your_num = input('Enter your next choice of numbers: ')
            elif len(your_num) == len(comp_num):
                print('correct: ', computer_test[0], 'so so: ', computer_test[1])
                your_num = input('Enter your next choice of numbers: ')
    if your_num == comp_num:
        ctr += 1
        print('You guessed the number, it took you only ', ctr, 'tries')
        time_elapsed = datetime.now() - start_time
        print('game duration (hh:mm:ss.ms) {}'.format(time_elapsed))











