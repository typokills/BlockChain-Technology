import datetime

class Block():

    def __init__(self,transactions, root, timestamp, nonce):
        print(timestamp)


year = str(datetime.datetime.now().year)
month = str(datetime.datetime.now().month)
day = str(datetime.datetime.now().day)
hour = str(datetime.datetime.now().hour)
minute = str(datetime.datetime.now().minute)
second = str(datetime.datetime.now().second)
timestamp = year + month + day + hour + minute + second


Block = Block(1,2,timestamp,4)