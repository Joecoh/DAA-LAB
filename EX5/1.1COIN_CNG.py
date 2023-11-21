def coin_change_ways(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1  # There is one way to make change for zero

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]

# Example usage:
coins = [1, 2, 5]
amount = 5
ways = coin_change_ways(coins, amount)
print(f"Number of ways to make change for {amount}: {ways}")
