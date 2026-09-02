class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        output=[]
        for i in nums:
            count[i]=1+count.get(i,0)
        
        sorted_counts = sorted(count.items(), key=lambda item: item[1], reverse=True)
        for i in range(k):
            output.append(sorted_counts[i][0])
        return output