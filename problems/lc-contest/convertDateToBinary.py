


def convertDateToBinary(date):
    year = bin(int(date[:4]))[2:]
    month = bin(int(date[5:7]))[2:]
    day= bin(int(date[8:]))[2:]
    res = "{}-{}-{}".format(year, month, day)
    return res


print(bin(2080))


date = "2080-02-29"
print(convertDateToBinary(date))