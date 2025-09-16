def PalindromRecursive(str):
    if len(str) == 0 or len(str) == 1: return True
    if str[0] == str[-1]: return PalindromRecursive(str[1:-1])
    else: return False

str = "radar"
print("Palindrome" if PalindromRecursive(str) else "Not a palindrome")
