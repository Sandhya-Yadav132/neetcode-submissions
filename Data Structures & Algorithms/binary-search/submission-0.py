class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        st=0
        end=n-1
        while st<=end:
            mid=st+(end-st)//2
            if target>nums[mid]:
                st=mid+1
            elif target<nums[mid]:
                end=mid-1
            else :
                return mid
        return -1