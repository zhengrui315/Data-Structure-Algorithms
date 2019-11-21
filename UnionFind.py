# https://leetcode.com/problems/friend-circles/

class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int

        Union Find
        """

        def FindRoot(i):
            while root[i] != i:
                root[i] = root[root[i]]  # path compression
                i = root[i]
            return i

        root = list(range(len(M)))  # initially, there is only one node in each set, then do union
        res = len(M)
        for i in range(len(M)):
            for j in range(i + 1, len(M[0])):
                if M[i][j] == 1:
                    ri, rj = FindRoot(i), FindRoot(j)
                    if ri != rj:
                        res -= 1
                        root[rj] = ri
        return res



# https://leetcode.com/problems/redundant-connection/ LC-684
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def findRoot(i):
            if i not in root:
                root[i] = i
            while root[i] != i:
                root[i] = root[root[i]]
                i = root[i]
            return i

        root = {}
        for i, j in edges:
            ri, rj = findRoot(i), findRoot(j)
            if ri == rj:
                return [i, j]
            root[rj] = ri



