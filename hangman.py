import random

print("Welcome to Hangman!\n")

wordList = [
    "apple", "grape", "table", "chair", "plant",
    "banana", "orange", "python", "window", "cloud",
    "river", "mountain", "school", "laptop", "garden",
    "keyboard", "mouse", "screen", "flower", "pencil",
    "notebook", "bottle", "camera", "bridge", "forest",
    "umbrella", "puzzle", "rocket", "planet", "engine",
    "guitar", "violin", "castle", "desert", "island",
    "jungle", "mirror", "pillow", "blanket", "wallet",
    "ticket", "wallet", "helmet", "cookie", "pocket"
]
randomWord = random.choice(wordList)
word= []
chances = 5

for letter in randomWord:
    word.append("_")

while chances> 0 and "_" in word:
    print("You have", chances, "guesses left.")
    guess= input("Guess a letter: ").lower()
    safe= False

    for position in range(len(randomWord)):
        letter = randomWord[position]
        if letter == guess:
            word[position] = letter
            safe = True
       
    if not safe: 
        chances -= 1
    print(word)
    print("\n")


if chances> 0:
    print("Congratulations! You've guessed the word:", randomWord)
else:
    print("Loser! The word was:", randomWord)



