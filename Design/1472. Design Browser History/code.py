class BrowserHistory:

    def __init__(self, homepage: str):
        
        self.homepage = homepage

        # Stacks for history
        self.forward_history = []
        self.backward_history = []

        # Adding homepage
        self.forward_history.append(self.homepage)
        

    def visit(self, url: str) -> None:
        # Adding url to stack
        self.forward_history.append(url)

        # Clearing forward history as it is key point
        self.backward_history.clear()
        
        
    def back(self, steps: int) -> str:
        
        # If steps > x, then 1st element will be last opened tab
        if self.forward_history and steps > len(self.forward_history):
            return self.forward_history[0]
        
        # Popping the elements to return last-indexed
        for _ in range(min(steps, len(self.forward_history))):
            current = self.forward_history.pop()
            self.backward_history.append(current)

        if self.forward_history:
            return self.forward_history[len(self.forward_history)-1]
        

    def forward(self, steps: int) -> str:
        
        # If steps > x, then last element will be last-visited one
        if self.backward_history and steps > len(self.backward_history):
            return self.forward_history[len(self.forward_history)-1]

        # Popping the elements to return last-indexed
        for _ in range(min(steps, len(self.forward_history))):
            if self.backward_history:
                current = self.backward_history.pop()
                self.forward_history.append(current)

        if self.forward_history:
            return self.forward_history[len(self.forward_history)-1]
        

# Your BrowserHistory object will be instantiated and called as such:

# Step 1: Initialize with homepage
# obj = BrowserHistory("leetcode.com")   # BrowserHistory

# # Step 2: Visit new URLs
# obj.visit("google.com")                # visit
# obj.visit("facebook.com")              # visit
# obj.visit("youtube.com")               # visit

# # Step 3: Navigate back
# print(obj.back(1))                     # facebook.com
# print(obj.back(1))                     # google.com

# # Step 4: Navigate forward
# print(obj.forward(1))                  # facebook.com

# # Step 5: Visit another site
# obj.visit("linkedin.com")              # visit

# # Step 6: Navigate forward (should stay same if no forward history)
# print(obj.forward(2))                  # linkedin.com

# # Step 7: Back twice
# print(obj.back(2))                     # google.com
# print(obj.back(7))                     # leetcode.com

"""
None
None
None
None
facebook.com
google.com
facebook.com
None
linkedin.com
google.com
leetcode.com
"""


# Custom test for BrowserHistory

obj = BrowserHistory("hdqqhm.com")     # init

obj.visit("yltqtsj.com")               # visit
print(obj.forward(1))    # yltqtsj.com
print(obj.back(1))       # hdqqhm.com
obj.visit("cyv.com")                   # visit
obj.visit("vbpvni.com")                # visit
obj.visit("opy.com")                   # visit
obj.visit("kbyzp.com")                 # visit
print(obj.back(7))       # hdqqhm.com
obj.visit("fchhxaz.com")               # visit
print(obj.back(6))       # hdqqhm.com
print(obj.forward(9))    # fchhxaz.com
obj.visit("rg.com")                    # visit
obj.visit("oemqn.com")                 # visit
obj.visit("hyqsb.com")                 # visit


'''
✅ Correct Logic (concept)

Store current page separately.

Use two stacks:

back_stack (pages you can go back to)

forward_stack (pages you can go forward to)

Operations:

Visit(url):

Push current into back_stack

Clear forward_stack

Update current = url

Back(steps):

While steps > 0 and back_stack not empty:

Push current into forward_stack

Pop from back_stack → new current

Return current

Forward(steps):

While steps > 0 and forward_stack not empty:

Push current into back_stack

Pop from forward_stack → new current

Return current
'''