from typing import List
import math

def coinChange(coins: List[int], amount: int) -> int:
    # Initialize memoization dictionary
    memo = {}
    
    def countCoins(remaining_amount: int, coin_index: int) -> int:
        # Step 1: Main Hoon (Who Am I?)
        # Subproblem: min coins needed for remaining_amount using coins[coin_index:]
        
        # Step 2: Kya Karoon (Check and Do?)
        # Base Case (Success): Made exact amount
        if remaining_amount == 0:
            print(f"State (amount={remaining_amount}, coin_index={coin_index}): 0")
            return 0
        # Base Case (Failure): Overshot amount or ran out of coins
        if remaining_amount < 0 or coin_index >= len(coins):
            print(f"State (amount={remaining_amount}, coin_index={coin_index}): -1")
            return float('inf')
        # Limits: Check memoization
        state = (remaining_amount, coin_index)
        if state in memo:
            print(f"State (amount={remaining_amount}, coin_index={coin_index}): {memo[state] if memo[state] != float('inf') else -1} (memoized)")
            return memo[state]
        
        # Step 3: Bacho Jao (Send Kids!)
        # Lun Na Lun Approach
        # Lun: Take current coin (if possible)
        take_coin = float('inf')
        if remaining_amount >= coins[coin_index]:
            take_coin = 1 + countCoins(remaining_amount - coins[coin_index], coin_index)
        # Na Lun: Skip current coin
        skip_coin = countCoins(remaining_amount, coin_index + 1)
        
        # Step 4: Kya Laya (What Did Kids Bring?)
        # Minimum of take or skip
        min_coins = min(take_coin, skip_coin)
        
        # Step 5: Ye Lo (Here’s the Answer!)
        # Memorize and return
        memo[state] = min_coins
        print(f"State (amount={remaining_amount}, coin_index={coin_index}): {min_coins if min_coins != float('inf') else -1}")
        return min_coins
    
    # Start from amount and coin_index 0
    result = countCoins(amount, 0)
    return result if result != float('inf') else -1

# Test the solution
def main():
    test_cases = [
        ([1, 2, 5], 11),
        ([2], 3),
        ([1], 0)
    ]
    for coins, amount in test_cases:
        print(f"\nTest Case: Coins={coins}, Amount={amount}")
        result = coinChange(coins, amount)
        print(f"Result: {result}\n")

if __name__ == "__main__":
    main()