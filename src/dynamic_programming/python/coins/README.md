# Coin Change Module

This module provides a function `coin_change_basic` for calculating the minimum number of coins needed to make up a given amount. The function uses a recursive approach to solve the problem.

## Author

Abed Hamami

## Function Description

python def coin_change_basic(amount, coins):


This function calculates the minimum number of coins needed to make up a given amount. It takes two parameters:

- `amount`: The target amount to make up. This should be an integer.
- `coins`: The list of available coin denominations. This should be a list of integers.

The function returns an integer representing the minimum number of coins needed to make up the amount. If it is not possible to make up the amount using the given coins, the function returns `-1`.

## Usage

Here is an example of how to use this function:

python print(coin_change_basic(11, [1, 2, 5])) # Output: 3


In this example, the function is called with an amount of `11` and a list of coin denominations `[1, 2, 5]`. The function returns `3`, which is the minimum number of coins needed to make up the amount `11` using the given coin denominations.

## Implementation

The function uses a recursive approach to solve the problem. It starts by checking if the amount is `0` or less than `0`. If the amount is `0`, it returns `0` because no coins are needed. If the amount is less than `0`, it returns `-1` because it is not possible to make up a negative amount.

Then, the function initializes a variable `res` to `float('inf')` to keep track of the minimum number of coins needed. It iterates over the list of coins and for each coin, it calls itself recursively with the remaining amount after subtracting the value of the current coin. If the result is greater than or equal to `0` and less than `res`, it updates `res` to the current result plus `1`.

Finally, the function returns `-1` if `res` is still `float('inf')`, otherwise it returns `res`.