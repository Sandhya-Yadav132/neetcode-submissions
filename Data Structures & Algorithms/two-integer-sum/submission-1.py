class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        dict_map={}
        for i in range(n):
            num=nums[i]
            if target-num in dict_map:
                return [dict_map[target-nums[i]],i]
            dict_map[num]=i