from collections import Counter

def is_anagram(word1, word2):
    """Receives two words and returns True/False (boolean) if word2 is
       an anagram of word1, ignore case and spacing."""
    w1 = word1.replace(' ', '').lower()
    w2 = word2.replace(' ', '').lower()
    return Counter(w1) == Counter(w2)
