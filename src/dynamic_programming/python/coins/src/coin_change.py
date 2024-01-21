"""
This module provides functions to find the minimum number of coins needed to make the given amount of money using the available coins.
"""

__author__ = "Abed Hamami"


def coin_change_basic(amount, coins):
    """
    Calculates the minimum number of coins needed to make a given amount of change.

    Args:
        amount (int): The amount of change to be made.
        coins (List[int]): A list of coin denominations available.

    Returns:
        int: The minimum number of coins needed to make the given amount of change. Returns -1 if it is not possible to make the change.
    """
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    res = float("inf")
    for coin in coins:
        sub_res = coin_change_basic(amount - coin, coins)
        if sub_res >= 0 and sub_res < res:
            res = sub_res + 1
    return -1 if res == float("inf") else res


def coin_change_memo(amount, coins):
    """
    Calculates the minimum number of coins needed to make up a given amount using a dynamic programming approach with memoization.

    Parameters:
        amount (int): The target amount to be made up using the coins.
        coins (list): A list of coin denominations.

    Returns:
        int: The minimum number of coins needed to make up the target amount. Returns -1 if it is not possible to make up the target amount using the given coins.
    """
    memo = {}

    def calculate_minimum_coins(n):
        """
        Calculates the minimum number of coins required to make change for a given amount.

        Parameters:
            n (int): The amount for which we need to make change.

        Returns:
            int: The minimum number of coins required to make change for the given amount.
        """
        if n == 0:
            return 0
        if n < 0:
            return -1
        if str(n) not in memo:
            res = float("inf")
            for coin in coins:
                sub_res = calculate_minimum_coins(n - coin)
                if sub_res >= 0 and sub_res < res:
                    res = sub_res + 1
            memo[str(n)] = -1 if res == float("inf") else res
        return memo[str(n)]

    return calculate_minimum_coins(amount)


def coin_change_tab(amount, coins):
    """
    Calculate the minimum number of coins needed to make up a given amount.

    Parameters:
        amount (int): The target amount to make up.
        coins (List[int]): The denominations of coins available.

    Returns:
        int: The minimum number of coins needed to make up the amount. Returns -1 if it is not possible to make up the amount with the given coins.
    """
    calculate_minimum_coins = [float("inf")] * (amount + 1)
    calculate_minimum_coins[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                calculate_minimum_coins[i] = min(calculate_minimum_coins[i], calculate_minimum_coins[i - coin] + 1)
    return -1 if calculate_minimum_coins[amount] == float("inf") else calculate_minimum_coins[amount]
