def climbing_stairs(total_steps):
    # Dictionary to store memoized results: key is remaining_steps, value is number of ways
    memo = {}
    
    def climbing_stairs_helper(remaining_steps):
        # Main Hoon: Define the subproblem
        # State is remaining_steps: number of steps left to reach the top
        
        # Kya Karoon: Check base cases and memoization
        # Base Case 1 (Success): Reached the top (no steps left)
        if remaining_steps == 0:
            print(f"State (remaining_steps={remaining_steps}): 1")
            return 1
        
        # Base Case 2 (Failure): Overshot the staircase (invalid path)
        if remaining_steps < 0:
            print(f"State (remaining_steps={remaining_steps}): 0")
            return 0
        
        # Check memoization to avoid recomputation
        if remaining_steps in memo:
            print(f"State (remaining_steps={remaining_steps}): {memo[remaining_steps]} (from memo)")
            return memo[remaining_steps]
        
        # Bacho Jao: Send kids to solve subproblems
        # Choice 1: Take 1 step
        ways_with_one_step = climbing_stairs_helper(remaining_steps - 1)
        # Choice 2: Take 2 steps
        ways_with_two_steps = climbing_stairs_helper(remaining_steps - 2)
        
        # Kya Laya: Combine results from subproblems
        total_ways = ways_with_one_step + ways_with_two_steps
        
        # Ye Lo: Memoize and return the result
        memo[remaining_steps] = total_ways
        print(f"State (remaining_steps={remaining_steps}): {total_ways}")
        return total_ways
    
    # Start the recursion from the top (total_steps)
    return climbing_stairs_helper(total_steps)

# Test the function
total_steps = 3
result = climbing_stairs(total_steps)
print(f"Number of ways to climb {total_steps} stairs: {result}")