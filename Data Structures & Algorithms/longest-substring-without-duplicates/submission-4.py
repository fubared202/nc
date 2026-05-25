class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        max_seen = min(1, len(s))
        chars_seen = set()
        if len(s) > 0:
            chars_seen.add(s[l])

        while r < len(s):
            if s[r] not in chars_seen:
                max_seen = max(max_seen, r - l + 1)
            else:
                while l <= r:
                    dup = s[l]
                    print(chars_seen)
                    chars_seen.remove(dup)
                    l += 1
                    if s[r] == dup:
                        break
            chars_seen.add(s[r])
            r += 1

        return max_seen