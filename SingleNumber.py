

#finding the number which appears atleast once in the list
# eg: Input: [4,1,2,1,2]
#     Output: 4  element 4 has appeared only once


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hmap = {}
        for i in nums:
            if i in hmap:
                hmap[i]+=1
            else:
                hmap[i]=1
        n = [key for key, value in hmap.items() if value == 1]
        
        return int(str(n).strip('[]'))