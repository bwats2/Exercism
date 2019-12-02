import datetime

def add(moment):
    return moment + datetime.timedelta(seconds=(10**9))

print (datetime.timedelta(seconds=100000))