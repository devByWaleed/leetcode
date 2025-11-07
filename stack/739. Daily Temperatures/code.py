from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stk = []

        for index, value in enumerate(temperatures): 
            # If current is larger
            while stk and stk[-1][0] < value:
                # Pop last element
                stk_val, stk_index = stk.pop()

                # Assign the difference for current day
                answer[stk_index] = index - stk_index

            # Adding current value in stack
            stk.append((value, index))

        return answer 
        

obj = Solution()
print(obj.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # [1,1,4,2,1,1,0,0]
print(obj.dailyTemperatures([30, 40, 50, 60]))                  # [1,1,1,0]
print(obj.dailyTemperatures([30, 60, 90]))                      # [1,1,0]

# T.C: O(N)
# S.C: O(N)



# Nested solution
'''
from typing import Listk

class Solution:
    def dailyTemperatures(self, temperatures: Listk[int]) -> Listk[int]:
        answer = []
        n = len(temperatures)
        found = False

        for i in range(len(temperatures)):
            if i == n - 1:
                answer.append(0)
                break
            
            for j in range(i+1, len(temperatures)):

                if temperatures[j] > temperatures[i]:
                    answer.append(j - i)
                    found = True
                    break
                
                found = False
                
            if not found:
                answer.append(0)
        
        return answer

        
obj = Solution()
print(obj.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # [1,1,4,2,1,1,0,0]
print(obj.dailyTemperatures([30, 40, 50, 60]))                  # [1,1,1,0]
print(obj.dailyTemperatures([30, 60, 90]))                      # [1,1,0]
'''