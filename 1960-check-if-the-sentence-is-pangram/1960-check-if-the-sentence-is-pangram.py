class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha_set=set("abcdefghijklmnopqrstuvwxyz")
        sen_set=set(sentence)
        if sen_set==alpha_set:
            return True
        else:
            return False    
           
                         
        
                


                   
        