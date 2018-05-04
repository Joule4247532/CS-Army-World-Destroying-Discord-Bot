def convert(nu, x, y):
    nu = str(nu)[::-1]
    xx = int(x)
    yy = int(y)
    if '-' in nu:
        return 'Positive value only!'
    elif 36 < xx < 2 and 36 < yy < 2:
        return "Base should be from 2 to 36!"
    letters = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20,
               'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31,
               'W': 32, 'X': 33, 'Y': 34, 'Z': 35}
    value = [xx ** i for i in range(len(nu))]
    digits = [nu[i] for i in range(len(nu))]
    Nsum = 0
    for i in range(len(nu)):
        if digits[i] in letters:
            digits[i] = letters[digits[i]]
        digits[i] = int(digits[i]) * value[i]
        Nsum += digits[i]
    # print(Nsum)
    n = Nsum
    bas = yy

    # print(nu)

    def to_string(n, bas):
        conver_tString = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if n < bas:
            return conver_tString[n]
        else:
            return to_string(n // bas, bas) + conver_tString[n % bas]

    return to_string(n, bas)


class MathPlugin(object):
    def __init__(self):
        self.msg = []
        self.bs1 = ''
        self.bs2 = ''
        self.snum = ''
        self.b1 = 0
        self.b2 = 0
        self.num = 0

    async def base(self, voice, message, discord_client: object):
        self.msg = message.content.split(' ')
        self.num = convert(self.msg[2], self.msg[1], self.msg[3])
        try:
            await discord_client.send_message(message.channel, "%s" % self.num)
        except Exception:
            await discord_client.send_message(message.channel, 'try this: !base {base of num} {num} {target base}')
