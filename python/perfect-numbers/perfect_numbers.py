def classify(number):
    if number <=0:
        raise ValueError("Must be valid number!")
    summed = sum([x for x in range(1, number) if number%x==0])
    if summed == number:
        return "perfect"
    elif summed > number:
        return "abundant"
    else:
        return "deficient"
