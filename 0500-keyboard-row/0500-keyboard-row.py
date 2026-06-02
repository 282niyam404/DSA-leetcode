class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row_1="qwertyuiop"
        row_2="asdfghjkl"
        row_3="zxcvbnm"
        final=[]
        for i in words:
            fin_set=set(i.lower())
            if all(x in list(row_1) for x in fin_set):
                final.append(i)
            elif all(x in list(row_2) for x in fin_set):
                final.append(i)
            elif all(x in list(row_3) for x in fin_set):
                final.append(i)
            else:
                continue
        return final