class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for i in nums:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        
        top_k = sorted(hash_map.keys(), key=lambda key:hash_map[key], reverse=True)[:k]
        return top_k
        
        
        

        