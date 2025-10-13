class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        pass

obj = Solution()
print(obj.minRemoveToMakeValid("lee(t(c)o)de)"))        # lee(t(co)de) / lee(t(c)ode)
print(obj.minRemoveToMakeValid("a)b(c)d"))              # ab(c)d
print(obj.minRemoveToMakeValid("))(("))                 # ""