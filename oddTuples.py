def oddTuples(aTup):
    newTup = ()
    for i in range(len(aTup)):
        if i%2 == 0:
            newTup += (aTup[i],)
    return newTup

tup = ('I', 'am', 'a', 'test', 'tuple')
print(oddTuples(tup))
