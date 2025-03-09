vowels = ["a", "e", "i", "o", "u"]

word = input("Give a word. \n").lower()

numVowels = 0

for letter in word:
    if letter in vowels:
        numVowels += 1

print("Your word, " + str(word) + ", has " + str(numVowels) + " vowels.")