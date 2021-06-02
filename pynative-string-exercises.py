import re

def mid_of_odd_string():
    s = input('Input: ')
    mid = len(s)//2
    substr = s[(mid-1):(mid+2)]
    print('Output: ' + str(substr))

def append_in_middle():
    s1 = input('Input: ')
    s2 = input('Input: ')
    mid = len(s1)//2
    new_s1 = s1[:mid:] + s2 + s1[mid:]
    print('Output: ' + new_s1)

def combine_strings():
    s1 = input('Input: ')
    s2 = input('Input: ')

    do = lambda i = 0, j = 0 : s1[i] + s2[i]

    res = do() + do(len(s1)//2, len(s2)//2) + do(len(s1)-1, len(s2)-1)
    print('Output: ' + res) 

def lower_in_front():
    s = input('Input: ')

    l_str = ''
    u_str = ''

    for i in range(len(s)):
        if s[i].islower():
            l_str += s[i]
        else:
            u_str += s[i]

    print('Output: ' + l_str + u_str)

def count_all_chars():
    s = input('Input: ')

    chars = dig = sym = 0

    for i in range(len(s)):
        if s[i].isalpha():
            chars += 1
        elif s[i].isdigit():
            dig += 1
        else:
            sym += 1

    print('Characters: ' + str(chars))
    print('Digits: ' + str(dig))
    print('Symbols: ' + str(sym))

def mix_strings():
    s1 = input('Input: ')
    s2 = input('Input: ')
    s2 = s2[::-1]
    res = ''

    len_s1 = len(s1)
    len_s2 = len(s2)

    loop = len_s1 if len_s1 > len_s2 else len_s2

    for i in range(loop):
        if loop < len_s1:
            res += s1[i]

        if loop < len_s2:
            res += s2[i]

    print('Output: ' + res)

def string_balance_test():
    s1 = input('Input: ')
    s2 = input('Input: ')
    
    for s in s1:
        if s2.count(s) == 0:
            print('False')
            return
    
    print('True')

def string_occurences():
    s1 = input('Input: ')
    s2 = input('Input: ')

    print('Output: ' + str(s2.lower().count(s1.lower()))) 

def digit_sum_avg_regex():
    s = input('Input: ')
    matches = re.findall("(\d+)",s)
    sum = 0
    for num in matches:
        sum += int(num)

    avg = sum/int(len(matches))

    print('Sum: ' + str(sum))
    print('Average: {:.2f}'.format(avg))

# Problems map is a dictionary mapping the serial number with its solver function.

problems = {
    '1': mid_of_odd_string,
    '2': append_in_middle,
    '3': combine_strings,
    '4': lower_in_front,
    '5': count_all_chars,
    '6': mix_strings,
    '7': string_balance_test,
    '8': string_occurences,
    '9': digit_sum_avg_regex
}

# main() is the root function from where the other functions are called
# depending on problem number provided in selection

def main():
    global problems
    option = input('Selection: ')

    problems[option]()

main() # Run the root function.