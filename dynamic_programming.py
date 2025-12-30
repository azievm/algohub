"""
Dynamic Programming examples.
"""

# --------------------------------------------------
# Climbing Stairs
# --------------------------------------------------

def climb_stairs(n):
    if n <= 2:
        return n

    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        prev2, prev1 = prev1, prev1 + prev2

    return prev1


# --------------------------------------------------
# Coin Change
# --------------------------------------------------

def coin_change(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != amount + 1 else -1
