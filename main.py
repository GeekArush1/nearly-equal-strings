def nearlyequal(str1, str2):
    if len(str1) != len(str2):
        return False
    i, count = 0, 0
    while i < len(str1):
        if str1[i] == str2[i]:
            count += 1
        i += 1
    count=len(str1)-count
    if count > 1:
        return False
    else:
        return True
str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")
if nearlyequal(str1, str2):
    print("Strings are nearly equal!")
else:
    print("Strings are not nearly equal")
