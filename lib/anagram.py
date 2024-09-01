# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, possible_anagrams):
        sorted_word = ''.join(sorted(self.word))
        matches = []
        
        for candidate in possible_anagrams:
            if ''.join(sorted(candidate)) == sorted_word:
                matches.append(candidate)
        
        return matches
