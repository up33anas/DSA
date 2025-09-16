# Function
def StringReverse(str, starting, ending):
    if starting == ending: return 
    StringReverse(str, starting+1, ending)
    print(str[starting], end="")

# Driver
s = "University of Engineering and Technology Lahore"
StringReverse(s, 0, 5)
print()