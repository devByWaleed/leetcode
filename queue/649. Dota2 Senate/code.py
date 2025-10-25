from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        n = len(senate)

        # 2 queues for both parties
        radiant, dire = deque(), deque()

        # Adding elements to right queue
        for i in range(n):
            if senate[i] == "R":
                radiant.append(i)
            else:
                dire.append(i)

        # Logic of voting
        while radiant and dire:

            r = radiant.popleft()
            d = dire.popleft()

            # Remove D and adjust circular queue
            if r < d:
                radiant.append(r + n)
            
            # Remove R and adjust circular queue
            else:
                dire.append(d + n)

        # Return party name
        return "Radiant" if not dire else "Dire"


obj = Solution()
print(obj.predictPartyVictory("DDRRR"))     # Dire
print(obj.predictPartyVictory("RD"))        # Radiant
print(obj.predictPartyVictory("RDD"))       # Dire
print(obj.predictPartyVictory("DR"))        # Dire
print(obj.predictPartyVictory("D"))         # Dire

# T.C: O(N)
# S.C: O(N)