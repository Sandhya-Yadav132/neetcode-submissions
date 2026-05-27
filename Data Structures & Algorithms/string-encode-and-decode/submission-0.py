class Solution:

    def encode(self, strs):
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s):
        result = []
        i = 0

        while i < len(s):

            # find #
            j = i
            while s[j] != "#":
                j += 1

            # length of string
            length = int(s[i:j])

            # actual string
            word = s[j + 1 : j + 1 + length]
            result.append(word)

            # move pointer
            i = j + 1 + length

        return result

