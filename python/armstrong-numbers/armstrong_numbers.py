def is_armstrong_number(number):
    length = len(str(number))
    res = [int(x) for x in str(number)]
    counthold = 0
    for item in res:
        counthold+=item**(length)
    if counthold == number:
        return True
    else:
        return False
