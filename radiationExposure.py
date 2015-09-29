def f(x):
	import math
	return 400*math.e**(math.log(0.5)/3.66 * x)

def new_range(start, stop, step):
    result = [start]
    while result[-1] < stop - step:
        result.append(result[-1] + step)
    return result

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    # FILL IN YOUR CODE HERE...
    total = 0.0
    for x in new_range(start, stop, step):
        total += f(x) * step
    return total

print radiationExposure(5, 10, 0.25)
