# https://leetcode.com/problems/course-schedule-ii/

class Solution1:
    def findOrder(self, numCourses, prerequisites):
        """
        Kahn's Algorithm

        """
        from collections import defaultdict

        pre, suc = defaultdict(set), defaultdict(set)
        for c1, c0 in prerequisites:
            pre[c1].add(c0) # c0 is the prerequisite of c1
            suc[c0].add(c1)

        ready = set(list(range(numCourses))).difference(set(pre.keys()))
        res = []
        while ready:
            c0 = ready.pop() # all prerequisites of course c0 have been taken or it doesn't have prerequisite
            res.append(c0)
            for c1 in suc[c0]:
                if len(pre[c1]) == 1:
                    ready.add(c1)
                pre[c1].remove(c0)

        if len(res) == numCourses:
            return res
        else: # no sol due to cycle
            return []


class Solution2:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Topological sorting: DFS with recursion

        This is an implementation of the DFS from https://en.wikipedia.org/wiki/Topological_sorting#Depth-first_search
        """
        from collections import defaultdict

        pre = defaultdict(set)
        for c1, c0 in prerequisites:
            pre[c1].add(c0) # c0 is the prerequisite of c1

        res = [c for c in range(numCourses) if c not in pre]
        def dfs(c1, seen):
            # check cycle
            if c1 in seen:
                return True
            # seen.add(c1)     ### DON'T DO THIS!!!

            # avoid duplicates
            if len(pre[c1]) == 0:
                return False

            # DFS
            for c0 in pre[c1]:
                if dfs(c0, seen | {c1}):
                    return True

            pre.pop(c1)
            res.append(c1)

        for c1 in range(numCourses):
            if dfs(c1, set()):
                return []
        return res


class Solution3:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Topological sorting: DFS with iteration

        It is very similar to Solution1, except that a stack is used to implement DFS with iteration
        """
        from collections import defaultdict

        pre, suc = defaultdict(set), defaultdict(set)
        for c1, c0 in prerequisites:
            pre[c1].add(c0) # c0 is the prerequisite of c1
            suc[c0].add(c1)

        ready = [c for c in range(numCourses) if c not in pre]
        res = []
        while ready:
            c0 = ready.pop()
            res.append(c0)
            for c1 in suc[c0]:
                pre[c1].remove(c0)
                if len(pre[c1]) == 0:
                    ready.append(c1)

        return res if len(res) == numCourses else []