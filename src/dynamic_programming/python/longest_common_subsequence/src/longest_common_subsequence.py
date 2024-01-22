# src/longest_common_subsequence.py

def lcs_basic(a, b):
    '''
    Finds the length of the Longest Common Subsequence (LCS) using a basic approach.

    Args:
    a (str): The first input string.
    b (str): The second input string.

    Returns:
    int: The length of the LCS.
    '''
    set_a = set(a)
    set_b = set(b)
    result = 0
    for i in set_a:
        for j in set_b:
            if i == j:
                result = result + 1
    return result

def lcs_memo(a, b):
    '''
    Finds the length of the Longest Common Subsequence (LCS) using memoization.

    Args:
    a (str): The first input string.
    b (str): The second input string.

    Returns:
    int: The length of the LCS.
    '''
    memo = {}

    def helper(i, j):
        '''
        Recursive helper function for memoized LCS calculation.

        Args:
        i (int): Current index in string a.
        j (int): Current index in string b.

        Returns:
        int: Length of the LCS for substrings a[:i] and b[:j].
        '''
        if (i, j) in memo:
            return memo[(i, j)]

        if i == 0 or j == 0:
            result = 0
        elif a[i - 1] == b[j - 1]:
            result = 1 + helper(i - 1, j - 1)
        else:
            result = max(helper(i - 1, j), helper(i, j - 1))

        memo[(i, j)] = result
        return result

    return helper(len(a), len(b))

def lcs_tab(a, b):
    '''
    Finds the length of the Longest Common Subsequence (LCS) using tabulation.

    Args:
    a (str): The first input string.
    b (str): The second input string.

    Returns:
    int: The length of the LCS.
    '''
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]
