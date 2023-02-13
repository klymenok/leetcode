class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odds = (high - low) // 2
        odds += 1 if (low % 2 or high % 2) else 0
        return odds
