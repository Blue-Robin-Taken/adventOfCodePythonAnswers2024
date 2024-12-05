import os
import re
import copy

import sys

sys.setrecursionlimit(5000)


def checkRule(check_rules, check_line):  # Part one

    for rule in check_rules:
        if rule[0] in check_line and rule[1] in check_line:
            if check_line.index(rule[0]) > check_line.index(rule[1]):
                return check_line

    return check_line[int(float(len(check_line)) / 2 - .5)]


def checkRulePartTwo(check_rules, check_line):  # Part two
    for rule in check_rules:
        if rule[0] in check_line and rule[1] in check_line:
            if check_line.index(rule[0]) > check_line.index(rule[1]):
                editedLine = copy.deepcopy(check_line)
                ind_0 = check_line.index(rule[0])
                ind_1 = check_line.index(rule[1])
                editedLine[ind_0] = rule[1]
                editedLine[ind_1] = rule[0]
                return checkRulePartTwo(check_rules, editedLine)
    return check_line[int(float(len(check_line)) / 2 - .5)]


with open(os.path.abspath('./input.txt'), 'r') as f:
    fileText = f.read()

    rules = []
    for i in re.finditer(r'\d*\|\d*', fileText):  # Generate rules
        rules.append([i.group(0).split('|')[0], i.group(0).split('|')[1]])

    checkLines = []
    for line in re.finditer(r'((\d+,)+\d+)', fileText):
        checkLines.append(line.group(0).split(','))

    returnSum = 0
    wrong_list = []
    for test_line in checkLines:
        if type(checkRule(rules, test_line)) is list:
            wrong_list.append(checkRule(rules, test_line))
        else:
            returnSum += int(checkRule(rules, test_line))

    print("Part one:", returnSum)

    returnSum = 0

    for test_line in wrong_list:
        returnSum += int(checkRulePartTwo(rules, test_line))

    print("Part two:", returnSum)
