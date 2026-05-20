class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        all_signatures = dict()
        for s in strs:
            # First convert the string to its character signature.
            letter_counts = [0] * 26
            for letter in s:
                letter_counts[ord(letter) - ord('a')] += 1
            signature = tuple(letter_counts)

            if signature in all_signatures:
                # Signature exists, so associate this string with
                # the signature.
                all_signatures[signature].append(s)
            else:
                # Create a new entry for the signature.
                all_signatures[signature] = [s,]

        # Finally, output all the associated strings together.
        output_list = list()
        for string_list in all_signatures.values():
            output_list.append(string_list)

        return output_list