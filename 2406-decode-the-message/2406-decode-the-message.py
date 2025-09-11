class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        apa="abcdefghijklmnopqrstuvwxyz"
        key_without_space=key.replace(" ","")
        clean_key=[]
        for i in key_without_space:
            if i not in clean_key:
                clean_key.append(i)
            else:
                continue
        maped_dic=dict(zip(clean_key,list(apa)))
        desipher_str=""
        for i in message:
            if i==" ":
                desipher_str+=" "
            else:
                desipher_str+=maped_dic[i]
        return desipher_str            

        