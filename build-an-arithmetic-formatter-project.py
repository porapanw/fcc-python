def formatted(max_len,num):
    formatted_num = ''
    in_front = ''
    space = max_len + 2 - len(num)
    for char in range(space):
        in_front += '_'
    formatted_num = in_front + num
    return formatted_num

def find_first_num(problem):
    num = ''
    for char in problem:
        if char == ' ':
            break
        num += char
    return num

def find_second_num(problem):
    num = ''
    for char in problem[::-1]:
        if char == ' ':
            break
        num = char + num
    return num

def find_operator(problem):
    for char in problem:
        if char == '+' or char == '-':
            return char

def check_digit(arr):
    for num in arr:
        if not num.isdigit():
            return 'Error: Numbers must only contain digits.'

def check_operator(arr):
    for op in arr:
        if not op in ['-','+']:
            return "Error: Operator must be '+' or '-'."

def check_len(arr):
    for num in arr:
        if len(num) > 4:
            return 'Error: Numbers cannot be more than four digits.'

def arithmetic_arranger(problems, show_answers=False):
    # exceed limit
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    first_arr = []
    second_arr = []
    operator = []
    for problem in problems:
        first_arr.append(find_first_num(problem))
        second_arr.append(find_second_num(problem))
        operator.append(find_operator(problem))

    # invalid operator
    op_error = check_operator(operator)
    if op_error:
        return op_error
    # invalid input
    digit_error = check_digit(first_arr + second_arr)
    if digit_error:
        return digit_error
    # exceed digits
    len_error = check_len(first_arr + second_arr)
    if len_error:
        return len_error

    max_len = []
    for n in range(0,len(problems)):
        max_len.append([n,max(len(first_arr[n]),len(second_arr[n]))])

    def formatted_line(arr):
        line = []
        i = 0
        while i < len(problems):
            space = 0
            num = ''
            each_max_len = max_len[i][1]
            each_len = len(arr[i])
            space = each_max_len - each_len + 2
            while space > 0:
                num = ' ' + num
                space -= 1
            num = num + arr[i]
            line.append(num)
            i += 1
        return line
    
    divider = formatted_line(first_arr)
    formatted_divider = []
    for num in divider:
        formatted_num = ''
        i = 0
        while i < len(num):
            formatted_num += '-'
            i += 1
        formatted_divider.append(formatted_num)
    
    def format_second_line(arr):
        temp = formatted_line(arr)
        result = []
        i = 0
        while i < len(temp):
            result.append(temp[i].replace(' ',operator[i],1))
            i += 1
        return result

    sum_arr = []
    for problem in problems:
        sum_arr.append(str(eval(problem)))

    first_line = '    '.join(formatted_line(first_arr))
    second_line = '    '.join(format_second_line(second_arr))
    dash_line = '    '.join(formatted_line(formatted_divider))
    sum_line = '    '.join(formatted_line(sum_arr))

    if show_answers:
        result = f'{first_line}\n{second_line}\n{dash_line}\n{sum_line}'
    else:
        result = f'{first_line}\n{second_line}\n{dash_line}'

    return result

print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"],True)}')


