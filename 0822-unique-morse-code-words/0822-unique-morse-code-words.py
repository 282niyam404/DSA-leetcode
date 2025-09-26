class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alpha_l=list("abcdefghijklmnopqrstuvwxyz")
        morse_code=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        map_dic=dict(zip(alpha_l,morse_code))
        morse_l=[]

        for i in words:
            mc=""
            for j in i:
                mc=mc+map_dic[j]
            morse_l.append(mc)
        return len(set(morse_l))    

        