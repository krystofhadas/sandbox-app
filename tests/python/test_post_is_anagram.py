import requests

class TestIsAnagram:
    def __init__(self):
        self.hostname = "http://localhost:8000/"
        self.anagram_endpoint = "is-anagram/"

    def test_is_anagram(self):
        self.resp = requests.post(
            f"{self.hostname}/{self.anagram_endpoint}", json={"str1": "fuck", "str2": "fkuc"}
        )
        print(f"{self.resp.text}")
        try:
            assert self.resp.status_code == 200
            assert "\"is_anagram\":true" in self.resp.text
        except AssertionError as e:
            raise e
        self.resp = requests.post(
            f"{self.hostname}/{self.anagram_endpoint}", json={"str1": "asd", "str2": "fkuc"}
        )
        print(f"{self.resp.text}")
        try:
            assert self.resp.status_code == 200
            assert "\"is_anagram\":false" in self.resp.text
        except AssertionError as e:
            raise e

TestIsAnagram().test_is_anagram()