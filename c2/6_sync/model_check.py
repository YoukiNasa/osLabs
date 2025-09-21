import sys

import colorama
colorama.init()

if len(sys.argv) != 2:
    # limit is infinite
    limit = float('inf')
else:
    limit = int(sys.argv[1])
count, n = 0, 100000
while True:
    strings = ''
    k = 0
    for ch in sys.stdin.read(n):
        strings += ch
        k += 1
        if ch == '{': count += 1
        elif ch == '}': count -= 1
        else:
            print(f'Error: invalid character {ch!r}')
            sys.exit(1)
        if not (0 <= count <= limit):
            print(f'Error: {strings[:k-1]}' + colorama.Fore.RED + strings[k-1] + colorama.Style.RESET_ALL + strings[k:])
            print(colorama.Fore.RED + ' '*(k+6) + '^')
            sys.exit(1)
    print(f'{n} OK.')