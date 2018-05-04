def convert(nu, x, y):
    #needs to be reversed
    num = str(nu)
    if '-' in num:
        return 'Positive value only!'
    elif x not in range(2, 37) and y not in range(2, 37):
        return "Base should be from 2 to 36!"
    letters = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20,
               'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31,
               'W': 32, 'X': 33, 'Y': 34, 'Z': 35}
    value = [x ** i for i in range(len(num))]
    digits = [num[i] for i in range(len(num))]
    Nsum = 0
    for i in range(len(num)):
        if digits[i] in letters:
            digits[i].replace(digits[i], letters[digits[i]])
        digits[i] = int(digits[i]) * value[i]
        Nsum += int(digits[i])
    print(Nsum)
    n = Nsum
    base = y
    print(num)

    def to_string(n, base):
        conver_tString = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if n < base:
            return conver_tString[n]
        else:
            return to_string(n // base, base) + conver_tString[n % base]

    return to_string(n, base)


print(convert(23, 10, 2))
