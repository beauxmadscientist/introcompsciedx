def isIn(char, aStr):
    if len(aStr) == 1 and char != aStr or len(aStr) == 0:
        return False
    else:
        index = len(aStr)/2
        test = aStr[index]
        if char == test:
            return True
        elif char > test:
            return isIn(char, aStr[index:])
        else:
            return isIn(char, aStr[:index])
