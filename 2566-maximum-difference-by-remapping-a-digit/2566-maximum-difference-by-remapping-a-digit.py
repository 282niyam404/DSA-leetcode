class Solution:
    def minMaxDifference(self, num: int) -> int:
        c = str(num)

        maxx = 9


        digits = [int(i) for i in c]
        min_in_c = min(digits)
        max_in_c = max(digits)


        max_target = None
        for ch in c:
            if ch != '9':
                max_target = ch
                break

        maxint = ""
        if max_target is None:          
            maxint = c
        else:
            for ch in c:
                if ch == max_target:
                    maxint += '9'
                else:
                    maxint += ch



        min_target = c[0]

        min_int = ""
        for ch in c:
            if ch == min_target:
                min_int += '0'
            else:
                min_int += ch


        final = int(maxint) - int(min_int)
        return final

                