import os
import copy


def check_line(l):
    line_ints = [int(x) for x in l.split(' ')]
    safe = True
    decreasing = 'unknown'

    for i in range(len(line_ints)):
        if i != 0:
            if abs(int(line_ints[i]) - int(line_ints[i - 1])) < 1 or abs(
                    int(line_ints[i]) - int(line_ints[i - 1])) > 3:
                safe = False
                break
            if (decreasing != 'unknown') and decreasing:
                if line_ints[i] > line_ints[i - 1]:
                    safe = False
                    break
            if (decreasing != 'unknown') and not decreasing:
                if line_ints[i] < line_ints[i - 1]:
                    safe = False
                    break
            if decreasing == 'unknown':
                if line_ints[i] > line_ints[i - 1]:
                    decreasing = False
                if line_ints[i] < line_ints[i - 1]:
                    decreasing = True
    return safe


with open(os.path.abspath('input.txt'), 'r') as f:
    safe_reports = 0
    split_lines = f.read().splitlines()
    for line in split_lines:
        if check_line(line):
            safe_reports += 1
        else:
            for char_num in range(len(line.split(' '))):
                copyList = copy.copy(line.split(' '))
                copyList.pop(char_num)
                newline = ' '.join(copyList)

                if check_line(newline):
                    safe_reports += 1
                    break

    print(safe_reports)
