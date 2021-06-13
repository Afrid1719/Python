import re, string

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

def chars_occurences():
    s = input('Input: ')
    res = {}
    for x in s:
        res[x] = s.count(x)
    
    print('Output: ', end='')
    print(res)

def rev_str():
    s = input('Input: ')

    res = [char for char in s]
    res.reverse()
    res = ''.join(res)
    print('Output: ' + res)

def last_pos():
    haystack = input('Input: ')
    needle = input('Search: ')

    x = haystack.rfind(needle)
    print('Output: ' + str(x))

def str_split():
    s = input('Input: ')
    sep = input('Separator: ')

    res = s.split('-')
    print('Output: ', end=' ')
    print(res)

def remove_empty_str():
    req_inp = []
    for i in range(6):
        inp = input('Input: ')
        req_inp.append(inp)

    res = [char for char in req_inp if char != ""]
    print('Output: ', end=' ')
    print(res)

def remove_punctuation():
    s = input("Input: ")

    mytrans = s.maketrans(' ', ' ', string.punctuation)
    res = s.translate(mytrans)
    print('Output: ' + res)

def remove_all_ints():
    s = input('Input: ')
    s = s.split(' ')
    res = ''

    for x in s:
        if x.isdecimal():
            res += x
    
    print('Output: ' + res)

def find_alphanum_words():
    s = input('Input: ')

    res = re.findall("([a-zA-Z]+[0-9]+|[0-9]+[a-zA-Z]+)[a-zA-Z0-9]*", s)
    print(res)
        
def replace_punctuation():
    s = input('Input: ')

    for term in string.punctuation:
        s = s.replace(term, '#')

    print('Output: ' + s)

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
    '9': digit_sum_avg_regex,
    '10': chars_occurences,
    '11': rev_str,
    '12': last_pos,
    '13': str_split,
    '14': remove_empty_str,
    '15': remove_punctuation,
    '16': remove_all_ints,
    '17': find_alphanum_words,
    '18': replace_punctuation
}

# main() is the root function from where the other functions are called
# depending on problem number provided in selection

def main():
    global problems
    option = input('Selection: ')

    problems[option]()

main() # Run the root function.