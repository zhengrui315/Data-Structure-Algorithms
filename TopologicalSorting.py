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


# https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/
# this problem is solved by two-step topological sorting

class Solution4:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        from collections import defaultdict

        # topological sorting for groups
        gpre, gsuc = defaultdict(set), defaultdict(set)
        for i, before in enumerate(beforeItems):
            for j in before:
                if group[i] == -1: #### assign group id for sorting if the order of the item matters
                    group[i] = m
                    m += 1
                if group[j] == -1:
                    group[j] = m
                    m += 1
                if group[i] == group[j]: #### don't forget this check!!!
                    continue
                gpre[group[i]].add(group[j])
                gsuc[group[j]].add(group[i])

        gStack = set([g for g in range(m) if g not in gpre])
        gSort = []
        while gStack:
            g0 = gStack.pop()
            gSort.append(g0)
            for g1 in gsuc[g0]:
                gpre[g1].remove(g0)
                if len(gpre[g1]) == 0:
                    gStack.add(g1)
        if len(gSort) < m:
            return []



        # topological sorting for items:
        pre, suc = defaultdict(set), defaultdict(set)
        for i, before in enumerate(beforeItems):
            pre[i] |= set(before)
            for j in before:
                suc[j].add(i)

        ### for the sake of time complexity
        gMap = defaultdict(set)
        for i in range(len(group)):
            if group[i] != -1:
                gMap[group[i]].add(i)

        res = [i for i in range(len(group)) if group[i] == -1] # first append items whose order doesn't matter
        for gId in gSort:
            ready = set([i for i in gMap[gId] if len(pre[i]) == 0])
            new = []
            while ready:
                i = ready.pop()
                new.append(i)
                for j in suc[i]:
                    pre[j].remove(i)
                    if len(pre[j]) == 0 and group[j] == gId:
                        ready.add(j)
            if len(new) < len(gMap[gId]):
                return []
            res.extend(new)
        return res