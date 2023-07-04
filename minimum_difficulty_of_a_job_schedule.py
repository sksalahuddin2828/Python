from functools import lru_cache
from math import inf
from typing import List

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        n = len(jobDifficulty)

        @lru_cache(None)
        def dp(cur_difficulty, i, d):
            if d == 1:
                return max(jobDifficulty[i:])
            if i == n - 1:
                return inf

            cur_difficulty = max(cur_difficulty, jobDifficulty[i])

            change = cur_difficulty + dp(cur_difficulty, i + 1, d - 1)
            dont = dp(cur_difficulty, i + 1, d)

            return min(change, dont)

        return dp(jobDifficulty[0], 0, d)

job_difficulty = [6, 5, 4, 3, 2, 1]
days = 2

solution = Solution()
result = solution.minDifficulty(job_difficulty, days)

print("Minimum difficulty:", result)


# Answer: Minimum difficulty: 7
