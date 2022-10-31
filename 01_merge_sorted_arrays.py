class Solution:
    def mergeTwoLists(self, list1, list2):
        output = []
        while len(list1) > 0 and len(list2) > 0:
            if list1[0] <= list2[0]:
                smaller_item = list1[0]
                del(list1[0])
                output.append(smaller_item)
            else:
                smaller_item = list2[0]
                del (list2[0])
                output.append(smaller_item)

        if len(list1) > 0:
            output = output + list1
        else:
            output = output + list2

        return output

if __name__ == "__main__":
    obj = Solution()
    list_1 = [1,2,4]
    list_2 = [1,3,4]
    output = obj.mergeTwoLists(list_1, list_2)
    print(output)
