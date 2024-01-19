# Coin Change  
This module provides a function for calculating the minimum number of coins needed to make up a given amount.

## Examples
Here's an example of how you can use the ```coin_change_basic()``` function:

1. coin_change_basic():


```python
# Example usage
amount = 5
coins = [1, 2, 5]
print(coin_change_basic(amount, coins)) # Output: 1

```

2. coin_change_memo():


```python
# Example usage
amount = 11
coins = [1, 2, 5, 10]
print(coin_change_memo(amount, coins)) # Output: 2

```
3. coin_change_tab():

```python
# Example usage
amount = 11
coins = [1, 2, 5, 10]
print(coin_change_tab(amount, coins)) # Output: 2

```


## Approach

This code defines three functions: `coin_change_basic()`, `coin_change_memo()`, and `coin_change_tab()`. Each function takes an amount and a list of coins as input and returns the minimum number of coins needed to make the given amount of money. The `coin_change_basic` function uses a recursive approach, the `coin_change_memo` function uses a recursive approach with memoization, and the `coin_change_tab` function uses a dynamic programming approach.


## Unittest results
test command:
```
coins % python3 -m unittest discover -v                          
```
results:

```
test_with_1 (tests.test_coins.TestCoinChangeBasic.test_with_1) ... ok
test_with_10 (tests.test_coins.TestCoinChangeBasic.test_with_10) ... ok
test_with_12 (tests.test_coins.TestCoinChangeBasic.test_with_12) ... ok
test_with_7 (tests.test_coins.TestCoinChangeBasic.test_with_7) ... ok
test_with_1 (tests.test_coins.TestCoinChangeMemo.test_with_1) ... ok
test_with_10 (tests.test_coins.TestCoinChangeMemo.test_with_10) ... ok
test_with_12 (tests.test_coins.TestCoinChangeMemo.test_with_12) ... ok
test_with_7 (tests.test_coins.TestCoinChangeMemo.test_with_7) ... ok
test_with_1 (tests.test_coins.TestCoinChangeTab.test_with_1) ... ok
test_with_10 (tests.test_coins.TestCoinChangeTab.test_with_10) ... ok
test_with_12 (tests.test_coins.TestCoinChangeTab.test_with_12) ... ok
test_with_7 (tests.test_coins.TestCoinChangeTab.test_with_7) ... ok

----------------------------------------------------------------------
Ran 12 tests in 0.000s

OK
```

## Author

Abed Hamami