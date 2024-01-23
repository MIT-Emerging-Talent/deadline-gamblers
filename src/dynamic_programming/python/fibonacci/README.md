# Fibonacci Number Calculation

This module provides a function to calculate the nth Fibonacci number using a recursive approach.

## Module: `fib.py`

The `fib.py` file contains the `fib` function which implements the recursive algorithm.

### Function: `fib`

The `fib` function calculates the nth number in the Fibonacci sequence recursively. The sequence starts with `fib(0) = 0` and `fib(1) = 1`.

#### Signature

```python
def fib(n: int) -> int:
```

#### Parameters

- `n`: the index of the Fibonacci number to calculate

#### Return Value

- The `fib` function returns the nth Fibonacci number.

#### Raises

- `ValueError`: if `n` is less than 0

#### Examples

```python
>>> fib(0)
0
>>> fib(1)
1
>>> fib(5)
5
>>> fib(10)
55
```

Author: Adel Batal