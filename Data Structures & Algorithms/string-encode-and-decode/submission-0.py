class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}-{s}"
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        elements = list()
        print(f"Got encoded string {s}")
        while i < len(s):
            element_len = 0
            while s[i] != '-':
                digit = ord(s[i]) - ord('0')
                i += 1
                if 0 <= digit <= 9:
                    element_len = (element_len * 10) + digit
                else:
                    break
            i += 1   # Skip over the 'hyphen'

            # Slurp the entire string as a slice.
            print(f"Got length {element_len}, i={i}")
            elements.append(s[i:i + element_len])
            i += element_len
        
        return elements


             

