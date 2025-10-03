class Solution:
    def isHappy(self, n: int) -> bool:
        
        square_sum = 0

        string = str(n)

        checked = set()

        hash_map = {}

        flag = True
        while flag:

            for i in range(len(string)):
                hash_map[string[i]] = int(string[i]) * int(string[i])


            for num in hash_map:
                square_sum += hash_map[num]
            

            if square_sum not in checked:
                checked.add(square_sum)
            elif square_sum  in checked:
                return False
                           
            elif square_sum != 1 and square_sum != n:
                hash_map.clear()

                string = str(square_sum)

                square_sum = 0

            
            else:
                return True


        # return False

obj = Solution()
print(obj.isHappy(2))       # False
print(obj.isHappy(19))      # True

print(obj.isHappy(7))      # True
print(obj.isHappy(10))      # True
print(obj.isHappy(13))      # True

print(obj.isHappy(4))       # False
print(obj.isHappy(20))       # False
print(obj.isHappy(8))       # False