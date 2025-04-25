from backend.anagram_checker import IsAnagram

class TestAnagramChecker:
    def test_is_anagram(self):
        assert IsAnagram.is_anagram("fun", "fnu") == True
        assert IsAnagram.is_anagram("nuf") == False
        assert IsAnagram.is_anagram("123") == True
        assert IsAnagram.is_anagram("123") == False


