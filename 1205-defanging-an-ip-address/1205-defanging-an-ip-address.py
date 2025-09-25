class Solution:
    def defangIPaddr(self, address: str) -> str:
        final_ad=""
        for i in address:
            if i==".":
                final_ad=final_ad+"[.]"
            else:
                final_ad=final_ad+i
        return final_ad        