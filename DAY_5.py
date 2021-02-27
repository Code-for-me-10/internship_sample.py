
# problem 3.1
char_list=[chr(a) for a in range(ord('a'), ord('z')+1)]
print("char list")
print(str(char_list))


print(chr(65))
# problem 3.2

char_dict = {i:ord(i) for i in char_list}
print("char dictionary:")
print(char_dict)


# problem stmt 3.3
vowels = ["a","e", "i", "o","u"]
char_vowel = {i:ord(i) for i in char_list if i in vowels}
print("char dictionary of vowel:")
print(char_vowel)


# problem 3.4
char_consonant = {i:ord(i) for i in char_list if i not in vowels}
print("char dictionary of consonat:")
print(char_consonant)