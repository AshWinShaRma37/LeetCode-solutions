"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        stack = [root]
		
        if root ==None:
            return res
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            for i in range(len(curr.children)-1, -1, -1):
                stack.append(curr.children[i])

        return res