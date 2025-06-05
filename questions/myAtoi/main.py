class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Strip whitespace
        s = s.strip()
        
        # Step 2: Handle empty string
        if not s:
            return 0
        
        # Step 3: Handle sign
        sign = 1
        start = 0
        if s[0] == '-':
            sign = -1
            start = 1
        elif s[0] == '+':
            start = 1
        
        # Step 4: Convert digits
        result = 0
        for idx in range(start, len(s)): 
            if not s[idx].isdigit():
                break
            result = result * 10 + int(s[idx])  ## sara game idhar hai, har bar 10 multipiply. 
        
        # Step 5: Apply sign
        result *= sign
        
        # Step 6: Handle overflow
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN
        
        return result