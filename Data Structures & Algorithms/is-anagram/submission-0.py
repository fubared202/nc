class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_counts = [0] * 26
        for letter in s:
            letter_counts[ord(letter) - ord('a')] += 1
        for letter in t:
            letter_counts[ord(letter)- ord('a')] -= 1
        
        for count in letter_counts:
            if count != 0:
                return False

        return True