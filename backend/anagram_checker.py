class IsAnagram:

    @staticmethod
    def is_anagram(str1, str2) -> bool:
        try:
            return (
                    sorted(str(str1).lower().replace(" ", ""))
                    ==
                    sorted(str(str2).lower().replace(" ", "")))
        except Exception as e:
            raise e
