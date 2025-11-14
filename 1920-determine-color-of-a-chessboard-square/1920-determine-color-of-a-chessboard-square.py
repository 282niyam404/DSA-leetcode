class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        coor = list(coordinates)
        alpha=['a','b','c','d','e','f','g','h']
        for i,a in enumerate(alpha,start=1):
            if a in coor:
                if i%2==0 and int(coor[-1])%2==0:
                    return False
                if i%2!=0 and int(coor[-1])%2!=0:
                    return False
                else:
                    return True
        
        