class Solution:
    def getLucky(self, s: str, k: int) -> int:
        numm = [i for i in range(1, 27)]
        alp = list("abcdefghijklmnopqrstuvwxyz")

        mapp = dict(zip(alp, numm))

        convert = ""
        for i in s:
            convert += str(mapp[i])

        summ = 0
        for i in convert:
            summ += int(i)

        j = 0
        while j < k - 1:
            su = 0
            for i in str(summ):
                su += int(i)

            summ = su
            j += 1

        return summ
                   