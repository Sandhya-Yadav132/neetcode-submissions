class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_map={}
        for num in nums:
            dict_map[num] = dict_map.get(num,0)+1
        return heapq.nlargest(k,dict_map.keys(),key=dict_map.get)