# your code goes here!
class Anagram:
    def __init__(self, word):
        if not isinstance(word, str) or len(word) == 0:
            raise ValueError("Word must be a non-empty string.")
        self.word = word

    def match(self, words):
        """Returns a list of words that are anagrams of the initialized word."""
        if not isinstance(words, list):
            raise ValueError("Input must be a list of words.")
        
        matched_words = []
        sorted_word = sorted(self.word)  # Sort the letters of the initialized word

        for candidate in words:
            if sorted(candidate) == sorted_word:  # Check if sorted letters match
                matched_words.append(candidate)

        return matched_words