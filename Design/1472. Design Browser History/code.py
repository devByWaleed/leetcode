class BrowserHistory:

    def __init__(self, homepage: str):
        
        self.current = homepage   # Storing current page

        # Stacks for history
        self.back_stack = []        # Backward History
        self.forward_stack = []     # Forward History
    
        
    def visit(self, url: str) -> None:

        # Add url to back_stack (u can visit)
        self.back_stack.append(self.current)
        
        # Clearing forward history as per rule
        self.forward_stack.clear()

        # Setting current website to url (opened)
        self.current = url
        
        
    def back(self, steps: int) -> str:

        # Popping if Stack is not empty
        while steps > 0 and self.back_stack:
            self.forward_stack.append(self.current)

            self.current = self.back_stack.pop()

            steps -= 1
        
        # Returning current url 
        return self.current
        
        
    def forward(self, steps: int) -> str:
        
        # Popping if Stack is not empty
        while steps > 0 and self.forward_stack:
            self.back_stack.append(self.current)

            self.current = self.forward_stack.pop()

            steps -= 1
        
        # Returning current url 
        return self.current
        
        

# Your BrowserHistory object will be instantiated and called as such:

# Step 1: Initialize with homepage
obj = BrowserHistory("leetcode.com")   # BrowserHistory

# Step 2: Visit new URLs
obj.visit("google.com")                # visit
obj.visit("facebook.com")              # visit
obj.visit("youtube.com")               # visit

# Step 3: Navigate back
print(obj.back(1))                     # facebook.com
print(obj.back(1))                     # google.com

# Step 4: Navigate forward
print(obj.forward(1))                  # facebook.com

# Step 5: Visit another site
obj.visit("linkedin.com")              # visit

# Step 6: Navigate forward (should stay same if no forward history)
print(obj.forward(2))                  # linkedin.com

# Step 7: Back twice
print(obj.back(2))                     # google.com
print(obj.back(7))                     # leetcode.com

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

# T.C: O(1)
# S.C: O(N)