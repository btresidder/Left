"""
this is the "example" module.

The example module supplies one function, factorial().  For example,

>>> factorial(5)
120
"""

def factorial(n):
    """Return the factorial of n, an exact integer >= 0.

    :param n: a positive integer
    :return: the factorial of n as an integer

    .. doctest::
    
	>>> print(2+2)
	4

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]
    
    >>> factorial(30)
    265252859812191058636308480000000
        
    >>> factorial(30.0)
    265252859812191058636308480000000

    """

    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()

