import os

with open(os.path.abspath('./input.txt'), 'r') as f:
    text = str(f.read())

    total_count = 0

    # Check horizontal

    horizontal_list = [x for x in text.split('\n')]

    for x in horizontal_list:
        total_count += x.count('XMAS')
        total_count += x.count(''.join(reversed(list('XMAS'))))

    # Check Vertical
    vert_list = []
    for x in range(len(horizontal_list[0])):
        v = []
        for y in range(len(horizontal_list)):
            v.append(horizontal_list[y][x])
        vert_list.append(v)
    for y in vert_list:
        total_count += ''.join(y).count("XMAS")
        total_count += ''.join(y).count(''.join(reversed(list('XMAS'))))

    # Check diagonal 1

    for i in range(len(horizontal_list)):
        per = []
        for p in range(len(horizontal_list)):
            if (i + p) > len(horizontal_list) - 1:
                break
            per.append(horizontal_list[(i + p)][p])
        total_count += ''.join(per).count("XMAS")
        total_count += ''.join(per).count(''.join(reversed(list('XMAS'))))

    diag_list = []
    for i in range(len(horizontal_list)):
        per = []
        for p in range(len(horizontal_list)):
            if (i + p) > len(horizontal_list) - 1:
                break
            per.append(horizontal_list[p][i + p])
        diag_list.append(per)
    diag_list.pop(0)
    for l in diag_list:
        total_count += ''.join(l).count('XMAS')
        total_count += ''.join(l).count(''.join(reversed(list('XMAS'))))

    #diag 2
    # Check diagonal 1
    for i in horizontal_list:
        i = reversed(i)
    horizontal_list.reverse()
    for i in range(len(horizontal_list)):
        per = []
        for p in range(len(horizontal_list)):
            if (i + p) > len(horizontal_list) - 1:
                break
            per.append(horizontal_list[(i + p)][p])
        total_count += ''.join(per).count("XMAS")
        total_count += ''.join(per).count(''.join(reversed(list('XMAS'))))

    diag_list = []
    for i in range(len(horizontal_list)):
        per = []
        for p in range(len(horizontal_list)):
            if (i + p) > len(horizontal_list) - 1:
                break
            per.append(horizontal_list[p][i + p])
        diag_list.append(per)
    diag_list.pop(0)
    for l in diag_list:
        total_count += ''.join(l).count('XMAS')
        total_count += ''.join(l).count(''.join(reversed(list('XMAS'))))

    print("Part one:", total_count)

    # Part 2
    new_count = 0
    for i in range(len(horizontal_list) - 1):
        for p in range(len(horizontal_list) - 1):
            if i < 1 or p < 1 or i > 139 or p > 139:
                continue
            if horizontal_list[i][p] == 'A':
                if horizontal_list[i + 1][p + 1] == 'S' and horizontal_list[i - 1][p + 1] == 'M':
                    if horizontal_list[i - 1][p - 1] == 'M' and horizontal_list[i + 1][p - 1] == 'S':
                        new_count += 1
                if horizontal_list[i + 1][p + 1] == 'S' and horizontal_list[i - 1][p + 1] == 'S':
                    if horizontal_list[i - 1][p - 1] == 'M' and horizontal_list[i + 1][p - 1] == 'M':
                        new_count += 1
                if horizontal_list[i + 1][p + 1] == 'M' and horizontal_list[i - 1][p + 1] == 'S':
                    if horizontal_list[i - 1][p - 1] == 'S' and horizontal_list[i + 1][p - 1] == 'M':
                        new_count += 1
                if horizontal_list[i + 1][p + 1] == 'M' and horizontal_list[i - 1][p + 1] == 'M':
                    if horizontal_list[i - 1][p - 1] == 'S' and horizontal_list[i + 1][p - 1] == 'S':
                        new_count += 1
    print("Part two:", new_count)
