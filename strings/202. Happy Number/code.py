class Solution:
    def isHappy(self, n: int) -> bool:
        
        square_sum = 0  # Calculate sum of digit's square

        string = str(n)     # int to string for iteration

        checked = set()     # Keep track of seen numbers

        hash_map = {}       # To map digit & its square
 
        while True:
            # Mapping value to hashmap
            for i in range(len(string)):
                hash_map[string[i]] = int(string[i]) * int(string[i])

            # Calculate sum
            for num in hash_map:
                square_sum += hash_map[num]
            
            # Condition if sum equals to 1
            if square_sum == 1:
                return True                

            # Condition if sum equals to 1
            elif square_sum in checked:
                return False
            
            # Else continue for the number
            else:
                checked.add(square_sum)
                hash_map.clear()

                string = str(square_sum)

                square_sum = 0


obj = Solution()
print(obj.isHappy(19))       # True
print(obj.isHappy(2))        # False
print(obj.isHappy(11))       # False, but True given









# class Solution:
#     def isHappy(self, n: int) -> bool:
        
#         square_sum = 0  # Calculate sum of digit's square

#         string = str(n)

#         checked = set()     # Keep track of seen numbers

#         hash_map = {}       # To map digit & its square
 
#         while True:
            
#             # Mapping value to hashmap
#             for i in range(len(string)):
#                 hash_map[string[i]] = int(string[i]) * int(string[i])

#             # Calculate sum
#             for num in hash_map:
#                 square_sum += hash_map[num]
            
#             # Condition if sum equals to 1
#             if square_sum not in checked:
#                 checked.add(square_sum)
#                 hash_map.clear()

#                 string = str(square_sum)

#                 square_sum = 0

#             elif square_sum in checked:
#                 break
                
#         return square_sum == 1 and square_sum in checked


# obj = Solution()
# print(obj.isHappy(7))      # True
# print(obj.isHappy(19))      # True
# print(obj.isHappy(2))       # False

# print(obj.isHappy(10))      # True
# print(obj.isHappy(13))      # True

# print(obj.isHappy(4))       # False
# print(obj.isHappy(20))       # False
# print(obj.isHappy(8))       # False