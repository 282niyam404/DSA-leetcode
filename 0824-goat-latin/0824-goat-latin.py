class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sen_splits=sentence.split(" ")
        vov="AaIiOoEeUu"
        final=[]
        for i in range(len(sen_splits)):
            if sen_splits[i][0] in vov:
                final.append(sen_splits[i]+"ma"+"a"*(i+1))
            else:
                x = sen_splits[i][0]
                j = sen_splits[i][1:] + x
                final.append(j+"ma"+("a"*(i+1)))
        return " ".join(final)        
        