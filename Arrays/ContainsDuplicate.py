class Solution(object):
    def containsDuplicateOn2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #time com = O(n2)
        for elem1 in nums:
            count = 0
            for elem2 in nums:
                if elem1 == elem2:
                    count += 1
                if count > 1:
                    return True
        return False
    def containsDuplicate(self, nums):
        elem_count_dict = {}
        for elem1 in nums:
            if elem1 not in elem_count_dict:
                elem_count_dict[elem1] = 1
            else:
                return True
        print(elem_count_dict)
        return False


if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,3,4,3,3]
    if sol.containsDuplicate(nums):
        print("Duplicate")
    else:
        print("not duplicate")
