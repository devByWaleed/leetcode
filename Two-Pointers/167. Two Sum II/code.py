class Solution:
    def twoSum(self, numbers: list[int], target: int):
        
        n = len(numbers)
        
        # 2 Pointers
        left = 0
        right = n - 1
        
        # Condition for looping
        while left != right:
        
            # Calculating sum
            sum = numbers[left] + numbers[right]
            
            # If equal, return it. Otherwise move pointers
            if sum == target:
                return [left+1, right+1]
            
            elif sum < target:
                left += 1
            
            else:
                right -= 1

                
obj = Solution()
print(obj.twoSum([2, 7, 11, 15], 9))       # [1, 2]
print(obj.twoSum([2, 3, 4], 6))            # [1, 3]
print(obj.twoSum([-1, 0], -1))             # [1, 2]

# T.C: O(N)
# S.C: O(1)