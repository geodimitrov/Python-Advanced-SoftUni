text = input()

VOWELS = {'a', 'o', 'u', 'e', 'i'}
VOWELS = VOWELS.union(x.upper() for x in VOWELS)

result = [ch for ch in text if ch not in VOWELS]
print("".join(result))