"""
Module: coin_change

This module provides a function for calculating the minimum number of coins needed to make up a given amount.

Author: Abed Hamami
"""
def coin_change_basic(amount, coins):
   """
   Calculates the minimum number of coins needed to make up a given amount.

   Parameters:
       amount (int): The target amount to make up.
       coins (list): The list of available coin denominations.

   Returns:
       int: The minimum number of coins needed to make up the amount. Returns -1 if it is not possible to make up the amount using the given coins.
   """
   if amount == 0:
       return 0
   if amount < 0:
       return -1
   res = float('inf')
   for i in range(len(coins)):
       sub_res = coin_change_basic(amount - coins[i], coins)
       if sub_res >= 0 and sub_res < res:
           res = sub_res + 1
   return -1 if res == float('inf') else res