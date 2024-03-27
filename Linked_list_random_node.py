# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    curPointer = None
    stack = None
    counter = 0
    def __init__(self, head: Optional[ListNode]):
        self.stack = head
        self.curPointer = head
        self.counter = 0
        while self.curPointer:
            self.counter+=1
            self.curPointer = self.curPointer.next
        

    def getRandom(self) -> int:
        n = random.uniform(0,self.counter)
        self.curPointer = self.stack
        while n>1:
            self.curPointer = self.curPointer.next
            n-=1
        return self.curPointer.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()