class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair=[]
        for i in range (len(nums)):
            x=target - nums[i]
            if x in nums and nums.index(x)!=i:
                pair.append(i)
                pair.append(nums.index(x))
                return (sorted(pair))