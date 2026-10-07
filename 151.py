# 151. Reverse Words in a String

class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = []
        buffer = []

        for letter in s:
            if letter != ' ':
                buffer.append(letter)
            else:
                if len(buffer) != 0:
                    words.append("".join(buffer))
                    buffer = []

        if buffer:
            words.append("".join(buffer))

        reversed_words = list(reversed(words))

        return " ".join(reversed_words)

