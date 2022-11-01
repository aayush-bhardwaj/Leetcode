class Solution:
    def longestCommonPrefix(self, strs):
        prefix = ""
        output = ""
        stop = False
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        for x in range(1, len(strs[0])+1):
            prefix = strs[0][0:x]
            for item in strs:
                if not item.startswith(prefix):
                    stop = True
                    break
            if stop: break
            output = prefix

        return output


obj = Solution()
input = ["flower", "flow", "flight"]
output = obj.longestCommonPrefix(input)
print(output)
