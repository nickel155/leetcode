def description():
    """
        nums --> list of numbers that can be added
        target --> the target
        return indices of the two numbers such that they add up to target.
    """


def brute_force( nums, target ):
    n = len( nums )
    for i in range( n ):
        for j in range( i + 1, n ):
            if nums[ i ] + nums[ j ] == target:
                return i, j


def optimised( nums, target ):
    d = { }
    for i, n in enumerate( nums ):
        if target - n in d:
            return d[ target - n ], i
        d[ n ] = i