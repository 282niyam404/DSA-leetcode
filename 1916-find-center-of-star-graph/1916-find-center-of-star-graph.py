class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        com=[]
        for i in range(len(edges)):
            for j in range(i+1,len(edges)):
                comm=set(edges[i])&set(edges[j])
                com.append(list(comm))
                break
            break   
        return com[0][0]    
        
        