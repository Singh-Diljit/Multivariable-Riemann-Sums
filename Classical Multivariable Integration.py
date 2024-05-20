"""Estimate the definite integral of a continuous bounded function."""

from typing import List #Not required for python 3.9 and above

def build_vectors(arr: List[list]) -> List[list]:
    """Return all lists satisfying a combinatorial restriction.

    Given N lists (x_1, ..., x_n) each consisting of M entries
    (that is x_i = [e_{i,1}, ... , e_{i,M}] construct all lists that
    draw exactly once from each x_i. Even if e_{i,j} == e_{i,k} they are
    considered different elements.

    Parameters
    ----------
    arr : List
        The original list of lists we build our new set on.

    Returns
    -------
    vectors : List
        A list of lists such that 'vectors[i][j]' is a member of 'arr[j].'
    
    """
    if len(arr[0]) == 1: #Each list contains only one element
        return [[x] for x in arr]
    
    elif len(arr) == 1: #There is only one list
        return [[x] for x in arr[0]]

    #Recursively build all vectors
    vectors = []
    for x in arr[0]:
        vectors += [[x] + tmp for tmp in build_vectors(arr[1:])]

    return vectors
	
def evalution_points(region: List[tuple], step_size: float) -> List[list]:
    """Return points to be used in the evaluation of hyperrectangle heights.

    Riemann sums approximate the volume of a given function by using easy
    to compute chunks (hyperrectangles). The height of each hyperrectangle
    depends on the surface of the function over that hyperplane. This function
    generates all heights to be used in our integral approximation. Occasionally
    the bounds of the integral are swapped - this negates the integral
    and is tracked with the 'flag' variable. 
        

    Parameters
    ----------
    region : List
        The original list of lists we build our new set on.
    step_size : float
        The fineness of discretization in each dimension.

    Returns
    -------
    eval_points : List
        A list points to be used as heights for hyperrectangles.
    flag : int
        Either 1 or -1 this tracks how many times the integral was 'flipped'.
    
    """
    dimension = len(region)

    subdivisions = [[0]] * dimension
    flag = 1 #Tracks how many bounds need to be flipped
    
    for i in range(dimension):
        start, end = region[i]
        if start > end:
            #By flipping the bounds we negate the integral
            start, end = end, start
            flag *= -1

        count_steps = int((end-start) // step_size)
        subdivisions[i] = [start + k * step_size for k in range(count_steps)]
        
    eval_points = build_vectors(subdivisions)
    return eval_points, flag

def est_integral(region: List[tuple], function, step_size: float) -> float:
    """Use Riemann sums to approximate the volume of a given function over a region.
        
    Parameters
    ----------
    region : List
        The original list of lists we build our new set on.
    function : robust to different types 
    step_size : float
        The fineness of discretization in each dimension.

    Returns
    -------
    eval_points : List
        A list points to be used as heights for hyperrectangles.
    flag : int
        Either 1 or -1 this tracks how many times the integral was 'flipped'.
    
    """
    dimension = len(region)
	
    #Volume of hypercube
    tower_vol = step_size ** dimension
    
    #Generate set of positions to evaluate
    #and the sign of the region of integration
    eval_points, flag = evalution_points(region, step_size) 

    #Evaluate and sum the volume of the hyperrectangles
    result = 0
    for position in eval_points:
        result += function(position) * tower_vol

    result *= flag
    
    return result
