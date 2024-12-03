import re

with open('input.txt', 'r') as f:
    text = f.read()

    sumReturn = 0
    #  https://stackoverflow.com/a/6110113/15982771
    funIter = re.finditer(r"""(don't\(\)|do\(\))|(mul\(\d*?,\d*?\))""", text, )
    disabled = False
    for i in funIter:
        # sumReturn += int(i.split(',')[0][4:])*int(i.split(',')[1][:-1])
        cur = i.group(0)
        print(cur, disabled)
        if "don't" in cur:
            disabled = True
        elif 'do' in cur:
            disabled = False
        if "mul" in cur and not disabled:
            r = cur.replace('mul(', '').replace(')', '').split(',')
            sumReturn += int(r[0]) * int(r[1])

    print(sumReturn)
