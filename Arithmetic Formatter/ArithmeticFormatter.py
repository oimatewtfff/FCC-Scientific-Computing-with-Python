import re


def arithmetic_arranger(problems, trueorfalse=None):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    r = []
    for problem in problems:
        first = re.search(r'\d+', problem).group(0)
        third = re.search(r'\d+$', problem).group(0)
        if len(first) > 4 or len(third) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if re.search(r'[a-z]', problem):
            return 'Error: Numbers must only contain digits.'
        x = max([len(first), len(third)])
        r.append(f'{first:>{x + 2}}')
        r.append('    ')
    r[-1] = '\n'
    for problem in problems:
        first = re.search(r'\d+', problem).group(0)
        if re.search(r'[/*]', problem):
            return "Error: Operator must be '+' or '-'."
        second = re.search(r'[+-]', problem).group(0)
        third = re.search(r'\d+$', problem).group(0)
        x = max([len(first), len(third)])
        r.append(f'{second} {third:>{x}}')
        r.append('    ')
    r[-1] = '\n'
    for problem in problems:
        first = re.search(r'\d+', problem).group(0)
        third = re.search(r'\d+$', problem).group(0)
        x = max([len(first), len(third)])
        r.append(f'{"-" * (x + 2)}')
        r.append('    ')
    r[-1] = ''
    if trueorfalse:
        r.append('\n')
        for problem in problems:
            first = re.search(r'\d+', problem).group(0)
            second = re.search(r'[+-]', problem).group(0)
            third = re.search(r'\d+$', problem).group(0)
            if second == '+':
                result = int(first) + int(third)
            else:
                result = int(first) - int(third)
            x = max([len(first), len(third)])
            r.append(f'{result:>{x + 2}}')
            r.append('    ')
        r[-1] = ''
    arr = "".join(r)
    return arr