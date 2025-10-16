class Solution:
    def interpret(self, command: str) -> str:
        fs=""
        i=0
        while i<len(command):
            if command[i]=="G":
                fs+="G"
            elif command[i:i+2]=="()":
                fs+="o"
            elif command[i:i+4]=="(al)":
                fs+="al"
            i=i+1  
        return fs    
        