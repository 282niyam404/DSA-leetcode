class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        n1={"real":num1.split("+")[0],"comp":num1.split("+")[1].split("i")[0]}
        n2={"real":num2.split("+")[0],"comp":num2.split("+")[1].split("i")[0]}
        mul_comp_real=str((int(n1["real"])*int(n2["real"]))-(int(n1["comp"])*int(n2["comp"])))
        mul_comp_comp=str((int(n1["comp"])*int(n2["real"]))+(int(n1["real"])*int(n2["comp"])))
        return f"{mul_comp_real}+{mul_comp_comp}i"

        
        
        