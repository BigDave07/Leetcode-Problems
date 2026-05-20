class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hash_map = set()

        for n in nums:
            if n in hash_map:
                return True
            hash_map.add(n)

        return False
    
# Time complexity: O(n)
# Space complexity: O(n)