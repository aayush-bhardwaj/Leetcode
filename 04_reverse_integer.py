class Solution:
    def reverse(self, x: int) -> int:
        output = ""
        negative = False
        input = str(x)
        ignore_zero_flag = True
        if len(input) == 1:
            return x
        for item in input:
            if item == "0" and ignore_zero_flag:
                continue
            if item == "-":
                negative = True
                continue
            ignore_zero_flag = False
            output = item + output

        if int(output) > 2**31 -1:
            return 0
        if negative:
            return int(output) * -1
        return int(output)

class Solution2:
    def reverse(self, x: int) -> int:
        pass

obj = Solution()
output = obj.reverse(-103)
print(output)
