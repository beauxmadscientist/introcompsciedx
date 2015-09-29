def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    for elem in L:
        if not f(elem):
            L.remove(elem)
            satisfiesF(L)
    return len(L)
        
def f(s):
    return 'a' in s

L = ['a']
print satisfiesF(L)
print L

L = ['b']
print satisfiesF(L)
print L

L = ['a',  'b']
print satisfiesF(L)
print L
   
L = ['a', 'b', 'a']
print satisfiesF(L)
print L

L = ['a', 'b', 'c']
print satisfiesF(L)
print L

L = ['d', 'b', 'a']
print satisfiesF(L)
print L
