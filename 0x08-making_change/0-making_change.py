def makeChange(coins, total):
    """
    Finds the minimum number of coins to make a given amount of change.

    Args:
        coins: A list of coin denominations.
        amount: The target amount to make change for.

    Returns:
        The minimum number of coins needed, or -1 if not possible.
    """
    # Sort the coins in descending order
    
    if total <= 0:
      return 0
    # coins.sort(reverse=True)
    # coins_need = 0;
    # for coin in coins:
    #     coins_need += total // coin
    #     total %= coin
    #     if total == 0:
    #         return coins_need
    # return
    # Initialize the DP table
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    # Fill the DP table
    for current_amount in range(1, total + 1):
        for coin in coins:
            if coin <= current_amount:
                dp[current_amount] = min(dp[current_amount], dp[current_amount - coin] + 1)

    # Check the result
    return dp[total] if dp[total] <= total else -1