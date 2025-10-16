import re
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        d=password
        if (len(d) >= 8 
            and re.search(r"[A-Z]", d)     # uppercase
            and re.search(r"[a-z]", d)     # lowercase
            and re.search(r"[0-9]", d)     # digit
            and not re.search(r"(.)\1", d)  # No two same consecutive chars
            and re.search(r"[!@#$%^&*()_+\-={}\[\]|\\:;\"'<>,.?/]", d)):  # special char
                return(True)
        else:
            return(False)
