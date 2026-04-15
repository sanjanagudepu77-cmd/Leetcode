class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=[[] for i in range (numCourses)]
        indegree=[0]*numCourses
        for course,dest in prerequisites:
            graph[dest].append(course)
            indegree[course]+=1
        q=[]
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        c=0
        while q:
            node=q.pop(0)
            c+=1
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return c==numCourses
        