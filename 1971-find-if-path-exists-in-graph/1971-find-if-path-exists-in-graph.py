class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph={}
        for u,v in edges:
            graph.setdefault(u,[]).append(v)
            graph.setdefault(v,[]).append(u)
        stk = [source]
        vis = set()

        while stk:
            node = stk.pop()
            if node == destination:
                return True
            if node in vis:
                continue
            vis.add(node)
            for nei in graph.get(node, []):
                stk.append(nei)

        return False   