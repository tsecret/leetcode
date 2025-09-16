from typing import List

# URL: ""
# topics: array, hash-table, sorting

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      d = {}

      for n in nums:
         if n in d:
            return True
         d[n] = 1

      return False
