



# Python enumerate()
# The enumerate() method adds counter to an iterable and returns it (the enumerate object).

def starts_with_vowel(word):
  vowels = ['a', 'e', 'i', 'o', 'u']
  if word[0].lower() in vowels:
    return True
  else:
    return False

fruits = ["Apple", "Banana", "Pear", "Apricot", "Orange"]

fruits_map = map(starts_with_vowel, fruits)
for is_fruit in fruits_map:
  print(is_fruit)
print("next")
fruits_map = map(starts_with_vowel, fruits)
for is_fruit in fruits_map:
  print(is_fruit)