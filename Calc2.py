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

numbers_and_operators = {42,43,45,47,48,49,50,51,52,53,54,55,56,57}

def simplify_sum(s):
    a = ''
    for c in s:
        if ord(c) in numbers_and_operators:
            a = a + c
    return a


def first_number_split_string_up(s):
    a = ''
    for c in s:
        if ord(c) in range (48,58):
            a = a + c
        else:
            return a
    return a

def find_next_operator_in_sum(s):
    op = ''
    operators = {42,43,45,47}
    for c in s[len(first_number_split_string_up(s)):]:
        if ord(c) in operators:
            op = op + c
        else:
            return op



def find_next_part_of_sum(s):
    # Example 1+2+3
    # Function finds +2
    # Example +2+3
    # Function finds +2
    # Example +3
    # Function should find +3
    number = ''
    for c in s[len(first_number_split_string_up(s)+find_next_operator_in_sum(s)):]:
        if ord(c) in range (48,58):
            number = number + c
        return find_next_operator_in_sum(s) + number



def add_on_extra_sum(sum_so_far,s):
    operator = find_next_operator_in_sum(s)
    number = multi_string_to_int(find_next_part_of_sum(s)[1:])
    if operator[0] == '+':
        return sum_so_far + number
    elif operator[0] == '-':
        return sum_so_far - number
    elif operator[0] == '/':
        return sum_so_far / number
    elif operator[0] == '*':
        return sum_so_far * number
    else:
        return 'error'


def sum_multiple_numbers(s):
    #sum_str is the already processed part of s
    sum_str = first_number_split_string_up(s)
    sum_ = multi_string_to_int(first_number_split_string_up(s))
    while len(sum_str) < len(s):
        sum_ = add_on_extra_sum(sum_,s[len(sum_str):])
        sum_str = sum_str + find_next_part_of_sum(s[len(sum_str):])       
    return sum_


#if __name__ == '__main__':
#    sum_ = input("What sum do you want doing?")
#    if sum_multiple_numbers(sum_) == 3:
#        print ('Approximately tau/2')
#    elif sum_multiple_numbers(sum_) == 6:
#        print ('Approximately tau')
#    else:
#        print(sum_multiple_numbers(sum_))

def shush_robie():
    answer = input('Will that do? (Answer y/n)').lower()
    if answer == "y":
        print ("I know, I'm awesome right!")
    elif answer == "n":
        print ("Stop being mean!")
    else:
        print ("You didn't pick y or n! Try again.")
#shush_robie()

    
