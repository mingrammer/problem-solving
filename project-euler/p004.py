# Largest palindrome product

found = False
palindromes = []
for i in range(1000, 100, -1):
    for j in range(1000, 100, -1):
        if str(i*j) == str(i*j)[::-1]:
            found = True
            break
    if found:
        palindromes.append(i*j)
print(max(palindromes))
