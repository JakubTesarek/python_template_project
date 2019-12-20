"""Template python project"""

def factorial(n: int) -> int: # pylint: disable=invalid-name
    """Calculates factorial

    Example:
        >>> factorial(10)
        3628800
    """
    return [1, 0][n > 1] or factorial(n-1) * n
