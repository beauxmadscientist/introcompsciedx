def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    key_list = []

    def is_unique(value, value_list):
        if value in value_list:
            return False
        else:
            return True

    for i, value in enumerate(aDict.values()):
        if not is_unique(value, aDict.values()[i+1:]):
            for key in aDict.keys():
                if aDict[key] == value:
                    del aDict[key]
        
    return sorted(aDict.keys())

print uniqueValues({1: 1, 2: 1, 3: 1})
print uniqueValues({1: 1, 2: 1, 3: 3})
print uniqueValues({1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0})
