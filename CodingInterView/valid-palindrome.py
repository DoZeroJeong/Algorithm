import re


def isPalindrome(self, s: str) -> bool:

    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]


result = isPalindrome(self=None, s="A man, a plan, a canal: Panama")
print(result)