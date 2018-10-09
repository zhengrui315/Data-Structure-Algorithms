
# LeetCode 307. Range Sum Query - Mutable
# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
# The update(i, val) function modifies nums by updating the element at index i to val.
# Given nums = [1, 3, 5]

# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8


class NumArray:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.data = [0] * (len(nums) + 1)  # the first element is just to reset the index
        self.nums = [0] * len(nums)
        for i in range(len(nums)):
            self.update(i, nums[i])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val - self.nums[i]
        self.nums[i] = val
        i += 1
        while i < len(self.data):
            self.data[i] += diff
            i += i & (-i)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.cumSum(j) - self.cumSum(i - 1)

    def cumSum(self, i):
        """
        self.nums[0] + ... + self.nums[i]
        """
        res = 0
        i += 1
        while i > 0:
            res += self.data[i]
            i -= i & (-i)
        return res

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)







# LeetCode 308. Range Sum Query 2D - Mutable
# Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by
# its upper left corner (row1, col1) and lower right corner (row2, col2).

class NumMatrix:
    """  in dim-2 case, binary indexed tree doesn't necessarily perform better than the naive sum way, since in the naive way, we update only one row at a time"""

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            return
        self.sum = [[0] * (len(matrix[0]) + 1) for r in range(len(matrix))]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.sum[r][c] = self.sum[r][c - 1] + matrix[r][c]

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        diff = val - (self.sum[row][col] - self.sum[row][col - 1])
        for c in range(col, len(self.sum[0]) - 1):
            self.sum[row][c] += diff

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        res = 0
        for r in range(row1, row2 + 1):
            res += self.sum[r][col2] - self.sum[r][col1 - 1]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)