import sys
class Solution:
    # Write your code here
    def __init__(self):
        self.stack = []
        self.queue = []

    def pushCharacter(self, ch):
        self.stack.append(ch)
    
    def enqueueCharacter(self, ch):
        self.queue.append(ch)

    def popCharacter(self):
        return self.stack.pop()
    
    def dequeueCharacter(self):
        return self.queue.pop(0)
    
# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.") 