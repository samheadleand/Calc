ord_constant = 48

def single_string_to_int(s):
    n = ord(s) - ord_constant
    return n

def multi_string_to_int(s):
    acc = 0
    for c in s:
        acc = acc * 10        
        acc = acc + single_string_to_int(c)
    return acc

def find_single_operator(s):
    plus = s.find('+')
    minus = s.find('-')
    divide = s.find('/')
    multiply = s.find('*')
    if plus != -1:
        return '+'
    elif minus != -1:
        return '-'
    elif divide != -1:
        return '/'
    elif multiply != -1:
        return '*'
    else:
        'error'

def first_number_split_string_up(s):
    plus = s.index(find_single_operator(s))
    if s[plus-1] == ' ':
        return multi_string_to_int(s[0:plus-1])
    elif ord(s[plus-1]) in range(48,58):
        return multi_string_to_int(s[0:plus])
    else:
        return 'error'

def second_number_split_string_up(s):
    plus = s.index(find_single_operator(s))
    if s[plus+1] == ' ':
        return multi_string_to_int(s[plus+2:])
    elif ord(s[plus+1]) in range(48,58):
        return multi_string_to_int(s[plus+1:])
    else:
        return 'error'


def complete_sum(s):
    if find_single_operator(s) == '+':
        return first_number_split_string_up(s) + second_number_split_string_up(s)
    elif find_single_operator(s) == '-':
        return first_number_split_string_up(s) - second_number_split_string_up(s)
    elif find_single_operator(s) == '/':
        return first_number_split_string_up(s) / second_number_split_string_up(s)    
    elif find_single_operator(s) == '*':
        return first_number_split_string_up(s) * second_number_split_string_up(s)
    else:
        return 'error'

sum_ = input("What sum do you want doing?")

print(complete_sum(sum_))

def shush_robie():
    answer = input('Will that do? (Answer y/n)').lower()
    if answer == "y":
        print ("I know, I'm awesome right!")
    elif answer == "n":
        print ("Stop being mean!")
    else:
        print ("You didn't pick y or n! Try again.")



