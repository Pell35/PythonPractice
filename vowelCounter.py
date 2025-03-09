vowels = ["a", "e", "i", "o", "u"]

word = input("Give a word. \n")

ranNum = len(word)

numVowels = 0

for i in range(ranNum):
    if word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u":
        numVowels += 1

print("Your word, " + str(word) + ", has " + str(numVowels) + " vowels.")