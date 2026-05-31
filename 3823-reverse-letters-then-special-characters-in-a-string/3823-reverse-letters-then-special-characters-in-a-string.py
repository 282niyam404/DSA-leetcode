class Solution:
    def reverseByType(self, s: str) -> str:
        dic_ch={}
        for i, ch in enumerate(s):
            if not ch.isalpha():
                dic_ch[i]=ch
            else:
                continue
        alpha_li=[]
        char=[]
        for i in s:
            if i.isalpha():
                alpha_li.append(i)
            else:
                char.append(i)      
        x_l=alpha_li[::-1]
        char[::-1]
        li_app=[]
        for i in dic_ch.keys():
            li_app.append(i)   
        final_dic=dict(zip(li_app,char[::-1]))
        for ind,val in sorted(final_dic.items()):
            x_l.insert(ind,val)       
        return "".join(x_l)    
        