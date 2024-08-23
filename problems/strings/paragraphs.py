def splitLines(paragraphs, w): 
    res = []
    for i, line in enumerate(paragraphs): 
        curRes = ""
        j = 0
        while j < len(line): 
            word = line[j]
            space = " "
            if j == 0 or curRes == "": space = "" 
            if len(curRes + space + word) <= w: 
                curRes += space + word
                j += 1
            else: 
                res.append([curRes, i])
                curRes = ""
        if curRes: 
            res.append([curRes, i])
    return res


def applyAlignment(lines, aligns, w): 
    res = []
    for line, i in lines: 
        spaces = " " * (w - len(line))
        if aligns[i] == "LEFT": 
            newLine = line + spaces
        else: 
            newLine = spaces + line
        res.append(newLine)
    return res


def buildParagraph(paragraphs, aligns, w):
    res = []

    # build lines, accounting for words 
    evenLines = splitLines(paragraphs, w)
    # apply alignment and then trailing spaces
    res = applyAlignment(evenLines, aligns, w)
    # apply the stars at the left and right for each line
    res = ["*" + line + "*" for line in res]

    # attach the top and bottom borders
    starLine = "*"*(w+2)
    res = [starLine] + res + [starLine]

    for x in res: 
        print(x)
    return res


paragraphs = [["hello", "world"], ["How", "areYou", "doing"], ["Please look", "and align", "to right"]]
w = 16
aligns = ["LEFT", "RIGHT", "RIGHT"]

paragraphs = [["you got that james dean", "day dream", "look in", "your eye and I got that"], ["red", "lip", "classic thing", "that you like"], ["Please look", "and align", "to right"]]
w = 40
aligns = ["LEFT", "RIGHT", "RIGHT"]


# res = splitLines(paragraphs, w)
# print(res)

# ['******************', 
#  '*hello world     *', 
#  '*How areYou doing*', 
#  '*     Please look*', 
#  '*       and align*', 
#  '*        to right*', 
#  '******************']

buildParagraph(paragraphs, aligns, w)


c = "  asdfas   "

