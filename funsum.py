import math as m

def polyPeri(n ,s):
    return n * s
    
def polyArea(n, s):
    return .25 * (n * s**2 * (1/m.tan(m.pi/n)))
    
def funsum(n, s):
    return round((polyArea(n, s) + (polyPeri(n, s)**2)), 4)
    
n = 7
s = 3
print(funsum(n, s))
