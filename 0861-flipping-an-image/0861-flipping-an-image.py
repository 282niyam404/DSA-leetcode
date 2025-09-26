class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rev_img=[i[::-1] for i in image]
        for i in range(len(rev_img)):
            for j in range(len(rev_img)):
                if rev_img[i][j]==1:
                    rev_img[i][j]=0
                else:
                    rev_img[i][j]=1
        return rev_img        
        