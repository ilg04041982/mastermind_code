import random

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


def convert_string_to_a_list_of_strings(string_num):
    list1 = []
    list1[:0] = string_num
    return list1


def findDup(string_num):
    convert = convert_string_to_a_list_of_strings(string_num)
    list_of_ints = [int(item) for item in convert]
    list_of_ints.sort()
    duplicates_list = []
    for i in range(0, len(list_of_ints) - 1):
        if list_of_ints[i] == list_of_ints[i + 1]:
            duplicates_list.append(list_of_ints[i])
    return duplicates_list


def Not_accepted_digits(string_num, digit_list):
    string_list = [str(item) for item in digit_list]
    not_accepted_digits = []
    for i in range(len(string_num)):
        if string_num[i] not in string_list and string_num[i] not in not_accepted_digits:
            not_accepted_digits.append(string_num[i])
    return not_accepted_digits



def detect_letters_in_str(string_num):
    count = 0
    for s in string_num:
        if (s.isalpha()) == True:
            count += 1
    return count

print('Mastermind game: duplicate: no, num of digits: 4, choices per digits: 0, 1, 2, 3, 4, 5 enter your number please:')

ctr = 0

while True:
    your_num = input('')
    ctr += 1
    detect_letters = detect_letters_in_str(your_num)
    if detect_letters > 0:
        print("Sorry, we don't play with letters")
        continue
    find_duplicates = findDup(your_num)
    if len(find_duplicates) > 0:
        print('No duplication, as indicated before')
        continue
    not_Accepted_digits = Not_accepted_digits(your_num, list(range(digits)))
    if len(not_Accepted_digits) > 0:
        print('Sorry, but', not_Accepted_digits[:], 'are not options')
        continue
    if your_num == comp_num:
        print('Congrats, you guessed the number, it took only', ctr, 'tries')
        break
    answer = match(your_num, comp_num)
    print(answer)









