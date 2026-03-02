class solution:
    def isvalid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []

        for i in range(len(s)):
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                top = stack.pop()
                if (s[i] == ')' and top != '(') or (s[i] == '}' and top != '{') or (s[i] == ']' and top != '['):
                    return False
        return not stack


# Test cases __name__ == "__main__":
    sol = solution()
    
 test
    for test_string, expected in test_cases:
        result = sol.isvalid(test_string)
        status = "✓" if result == expected else "✗"
        print(f"{status} isvalid('{test_string}') = {result} (expected {expected})")