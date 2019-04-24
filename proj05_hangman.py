import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    inFile = open(WORDLIST_FILENAME, "r", 0)
    line = inFile.readline()
    wordlist = string.split(line)
    return wordlist

def choose_word(wordlist):
    return random.choice(wordlist)

wordlist = load_words()

counter = 8
counter2 = 0
word = wordlist[random.randint(1, 55901)]
word_list = list(word)
word_length = int(len(word_list))
blanks = []
guess_list = []
while counter2 < word_length:
    blanks.append("_")
    counter2 = counter2 + 1
print "Welcome to the game, Hangman!"
print"I am thinking of a word that is", word_length, "letters long"
alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z"]
while counter > 0:
    print"You have", counter, "guesses left."
    print "Available letters: " + "".join(alpha)
    guess = raw_input("Please enter your letter or take a guess at the word: ")
    counter1 = 0
    counter3 = 0
    while counter1 < word_length:
        if guess == word_list[counter1]:
            blanks[counter1] = guess
        counter1 = counter1 + 1
        while counter3 < 26:
            if guess == alpha[counter3]:
                alpha[counter3] = ""
                print "Good Guess."
            counter3 = counter3 + 1
    if guess in guess_list:
        print "You already guessed this letter. Try again."
    print " ".join(blanks)
    if guess not in word_list:
        counter = counter - 1
        print "This letter is not a part of the world."
    guess_list.append(guess)
    if word_list == blanks:
        print "Congratulations! You guessed the word", word, "correctly!"
        break
if counter == 0:
    print "You did not guess the correct word, which was " + word + ". " 


