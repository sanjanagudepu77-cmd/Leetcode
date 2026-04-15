class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n=numCourses
        graph=[[] for i in range (numCourses)]
        indegree=[0]*numCourses
        for course,dest in prerequisites:
            graph[dest].append(course)
            indegree[course]+=1
        q=[]
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        c=[]
        while q:
            node=q.pop(0)
            c.append(node)
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        if len(c)==n:
            return c
        else:
            return [] 
        