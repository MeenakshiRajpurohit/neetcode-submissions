class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

sol = Solution()
p = sol.isAnagram("jar", "jam")
print(p)

h = sol.isAnagram("racecar", "carrace")
print(h)
        