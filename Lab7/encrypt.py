'''
Xuan Guo
CS5001, Fall 2020

This program uses Caesar cipher method convert the message to encrypt code
'''


UPPER_BOUND = 122
LOWER_BOUND = 97
DIFF = 1


def check_input(letter):
    '''
        Function -- check_input
        Parameters:
            letter -- a English letter
        Returns:
            True if the input is a letter, False otherwise
    '''
    return letter.isalpha()


def check_amount(amount):
    '''
        Function -- check_amount
        Parameters:
            amount -- a non-negative integer
        Returns:
            True if amount is between 0 and 25 inclusive, False otherwise
        '''
    LOWER_BOUND = 0
    UPPER_BOUND = 26
    return amount in range(LOWER_BOUND, UPPER_BOUND)


def convert_amount(amount):
    '''
        Function -- convert_amount
        Parameters:
            amount -- a non-negative integer
        Returns:
            The original amount if it's between 0 and 25 inclusive, otherwise
            return amount % 25
    '''
    BOUND = 25
    if check_amount(amount):
        return amount
    return amount % BOUND


def encrypt(message, amount):
    '''
        Function -- encrypt
        Parameters:
            message -- a string
            amount -- a non-negative integer between 0 to 26 inclusive
        Returns:
            The converted encrypt code
    '''
    new_mes = ''
    amount = convert_amount(amount)
    for i in message:
        if check_input(i):
            temp = ord(i) + amount
            if temp > UPPER_BOUND:
                temp = LOWER_BOUND + temp % UPPER_BOUND - DIFF
            new_mes += chr(temp)
        else:
            new_mes += i
    return new_mes


def dencrypt(message, amount):
    '''
        Function -- dencrypt
        Parameters:
            message -- a string
            amount -- a non-negative integer between 0 to 26 inclusive
        Returns:
            The original string before it's converted to encrypt code
    '''
    old_mes = ''
    amount = convert_amount(amount)
    for i in message:
        if check_input(i):
            temp = ord(i) - amount
            if temp < LOWER_BOUND:
                temp = UPPER_BOUND - LOWER_BOUND % temp + DIFF
            old_mes += chr(temp)
        else:
            old_mes += i
    return old_mes


def deslide(mesg, num):
    return mesg[num :] + mesg[:num]


def main():
    mes = input('Enter a message to encript: ').lower()
    amount = int(input('Enter a shift amount: '))
    encrypted = encrypt(mes, amount)
    print('Your super secret message is: ' + encrypted)
    print('...decrypting encoded message now...')
    dencrypted = dencrypt(encrypted, amount)
    print('It was: ' + dencrypted)
    START = 1
    TIMES = 6
    code1 = "*.glygo rsvvmw'w gshi avmxiw gsqqirxw efsyx *lmq"
    code2 = "aqwuvwem, kp cp kphkpkvg nqqr, ykvj"
    code3 = ".sjajw ywzxy f htruzyjw dtz hfs’y ymwtb tzy f bnsitb.."
    code4 = "yko.vjg swguvkqp qh yjgvjgt eqorwvgtu ecp vjkpm ku nkmg vjg \
        swguvkqp qh yjgvjgt uwdoctkpgu ecp u"
    code5 = ".ejwem pqttku ytkvgu dqqngcp gzrtguukqpu vjcv ctg dqvj vtwg \
        cpf hcnug"
    CODES = [code1, code2, code3, code4, code5]
    for item in CODES:
        for i in range(START, TIMES):
            new = dencrypt(item, i)
            for a in range(START, TIMES):
                print(deslide(new, a))
    result1 = "chuck norris's code writes comments about *him*."
    result2 = "stuck, in an infinite loop, withyou"
    result3 = "never trust a computer you can’t throw out a window..."
    result4 = "the question of whether computers can think is like the \
        question of whether submarines can swim."
    result5 = "chuck norris writes boolean expressions that are both true \
        and false."


if __name__ == "__main__":
    main()
