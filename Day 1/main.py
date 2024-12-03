import os

with open(os.path.abspath('./distances.txt'), 'r') as f:
    read_f = f.read()
    r_list = []
    l_list = []

    for line in read_f.splitlines():
        splitLine = line.split('   ')
        r_list.append(int(splitLine[0]))
        l_list.append(int(splitLine[1]))

    # --- Part one ---
    diffs = 0
    sorted_r = sorted(r_list)
    sorted_l = sorted(l_list)
    for i in range(len(r_list)):
        diffs += abs(sorted_r[i] - sorted_l[i])

    print(diffs)

    # --- Part Two ---
    similarity = 0
    for r in r_list:
        count = l_list.count(r)
        if count:
            similarity += r * count

    print(similarity)
