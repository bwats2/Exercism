def convert(number):
    strang = ""
    if number % 3 == 0:
        strang += "Pling"
    if number % 5 == 0:
        strang += "Plang"
    if number % 7 == 0:
        strang += "Plong"
    if strang != "":
        return strang
    else:
        return(f"{number}")