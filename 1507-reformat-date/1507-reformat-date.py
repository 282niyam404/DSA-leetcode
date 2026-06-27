class Solution:
    def reformatDate(self, date: str) -> str:
        month_map=dict(zip(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],["01","02","03","04","05","06","07","08","09","10","11","12"]))
        x=date.split(" ")
        x[0]=int(''.join(ch for ch in x[0] if ch.isdigit()))
        x[0]=f"{x[0]:02d}"
        if x[1] in month_map:
            x[1]=month_map[x[1]]
        return "-".join(x[::-1])    
        