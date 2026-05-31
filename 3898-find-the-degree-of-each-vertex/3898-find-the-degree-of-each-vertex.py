class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        graph={}
        for u,row in enumerate(matrix):
            graph.setdefault(u,[])
            for v,w in enumerate(row):
                if w:
                    graph.setdefault(u,[]).append(v)
        li=[]
        for l in graph.values():
            li.append(len(l))
        return li    