word = input()
 
palindrome = 1
for i in range(len(word) // 2):
    if word[i] != word[-1 - i]:
        palindrome = 0
        break
 
print(palindrome)