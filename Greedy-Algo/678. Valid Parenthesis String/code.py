class Solution:
    def checkValidString(self, s: str) -> bool:
        # 2 var greedy approach 

        # min -> ) & max for (
        min_open, max_open = 0, 0

        for char in s:

            if char == "(":
                min_open += 1
                max_open += 1
            
            if char == "*":
                # * -> )
                min_open -= 1
                # * -> (
                max_open += 1

            if char == ")":
                # * -> )
                min_open -= 1
                # * -> (
                max_open -= 1
            
            # If -ve, we assume to use * as ""
            if min_open < 0:
                min_open = 0
            
            # If -ve, we could not balance the parentheses
            if max_open < 0:
                return False

        # There is a way to make string balanced
        return min_open == 0


obj = Solution()
print(obj.checkValidString("()"))      # True
print(obj.checkValidString("(*)"))     # True
print(obj.checkValidString("(*))"))    # True
print(obj.checkValidString("("))       # False
print(obj.checkValidString("(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((("))      # False

# T.C: O(N)
# S.C: O(1)