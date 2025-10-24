class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        queue = []
        current_index = 0

        # Adding players to queue
        for i in range(1, n+1):
            queue.append(i)

        # Playing game
        while len(queue) != 1:
            current_index += (k - 1)        # Including starting one
            current_index = current_index % len(queue)      # Circular queue implementation
            queue.pop(current_index)        # Removing the player
  

        return queue[0]     # Returning 1 (remains) element


obj = Solution()
print(obj.findTheWinner(5, 2))      # 3
print(obj.findTheWinner(6, 5))      # 1

# T.C: O(N * K)
# S.C: O(N)