# LeetCode 307. Range Sum Query - Mutable
# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
# The update(i, val) function modifies nums by updating the element at index i to val.
# Given nums = [1, 3, 5]

# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8

class TreeNode():
    def __init__(self):
        self.val = None
        self.range = [None, None]
        self.left = None
        self.right = None
        
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.root = self.segTree(0, len(nums)-1, nums)
        
    def segTree(self, i, j, nums):
        if i > j:
            return None
        else:
            node = TreeNode()
            node.range = [i, j]
            if i == j:
                node.val = nums[i]
            else:
                node.left, node.right = self.segTree(i, (i+j)//2, nums), self.segTree((i+j)//2+1, j, nums)
                node.val = node.left.val + node.right.val
            return node
            
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        node = self.root
        stack = [node]
        while node.range[0] != node.range[1]:
            if node.range[0] <= i <= sum(node.range) // 2:
                node = node.left
            else:
                node = node.right
            stack.append(node)
            
        diff = val - node.val
        while stack:
            stack.pop().val += diff
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        def helper(node):
            if not node or node.range[1] < i or node.range[0] > j:
                return 0
            elif i <= node.range[0] and node.range[1] <= j:
                return node.val
            else:
                return helper(node.left) + helper(node.right)

        return helper(self.root)
    
    
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)



