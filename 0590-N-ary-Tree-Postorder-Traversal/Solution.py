# Completed on: 08/26/2024
# Submission: https://leetcode.com/problems/n-ary-tree-postorder-traversal/submissions/1368558077/
# Time Complexity: O(n)
# Space Complexity: O(n) 

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: Node) -> list[int]:
        re = []
        def helper(node):
            if not node: return None
            else:
                for child in node.children:
                    helper(child)
            re.append(node.val)
        helper(root)
        return re

        