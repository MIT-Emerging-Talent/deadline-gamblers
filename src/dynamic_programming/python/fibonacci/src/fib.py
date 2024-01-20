def fib(n: int) -> int:
    """
    Calculate the nth Fibonacci number using a recursive approach.

    Args:
    - n (int): The position in the Fibonacci sequence to calculate. The first position is 0.

    Returns:
    - int: The nth Fibonacci number.

    Raises:
    - ValueError: If n is negative.

    Examples:
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(5)
    5
    >>> fib(10)
    55
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
