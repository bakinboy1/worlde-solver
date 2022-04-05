import webbrowser
import random


# compare each letter in guess to the answer
# ID the letters that match
# ID the letters that dont match
# from the letters that match ID the ones that match and are in the right place
# exclude words that contain wrong letters

# if there is a letter in the right spot-
# search dictionary for all words with a letter in that spot and group them and guess a random one

# if there is no letter in the right spot but a right letter guessed-
# group all words with matching letters and guess a random one

# if there is no match at all-
# find all words that dont contain guessed letters, group, and guess randomly
# webbrowser.open_new_tab("https://www.nytimes.com/games/wordle/index.html")
# from typing import List

#######################################################
# read text file

text_file = open(r"C:\Users\fhucke\Desktop\wordle bank.txt", "r")

# split text into array by line into 'lines' array
lines = text_file.read().splitlines()
text_file.close()

# split words into 2d array of letters
global splitWords
splitWords = [list(splitWords) for splitWords in lines]
#######################################################

# initialize variables
#######################################################
answer = "grind"
testList = list(answer)

firstGuess = "orean"
guessList = list(firstGuess)

# correctLetters = np.empty((5, 2), object)
correctLetters = []
correctIndex = []
wrongLetters = []
filteredWords = []


#######################################################

# guessing loop
#######################################################


#######################################################

# method definitions
#######################################################
#######################################################
# compare firstGuess to test
# split both into character arrays
# check for matching letters first, record hits into 3d letterMatch
# array with index position of matched letters and blank boolean 'rightSpot' value

# for each letter in test, check if that letter is in firstGuess at all,
# then check if test's letter index matches firstGuess's letter index
##############################
#######################
# guessing process
#######################

def delete_element(list_object, pos):
    # Delete element from list at given index
    # position (pos)
    if pos < len(list_object):
        list_object.pop(pos)


def findMatches():
    for letter in testList:
        i = 0
        testIndex = testList.index(letter)
        # check every letter in guessList against the current letter in testList
        for letterGuessed in guessList:
            guessIndex = guessList.index(letterGuessed)

            # if the letter and index match, record both
            if guessIndex == testIndex and letter == letterGuessed:
                correctLetters.append([testIndex, letter])
                # correctLetters[testIndex][0] = testIndex
                # correctLetters[testIndex][1] = letter

            # if the letter matches but the index doesnt, put 6 as the index
            if guessIndex != testIndex and letter == letterGuessed:
                correctLetters.append([6, letter])

                # correctLetters[i][0] = 6
                # correctLetters[i][1] = letter

            # if the letter guessed is not in the word at all, add it to the wrongLetters list
            # if not already in there
            if letterGuessed not in testList and (letterGuessed not in wrongLetters):
                wrongLetters.append(letterGuessed)

        i += 1


# findMatches()
#######################
# guessing process
#######################
##############################


##############################
#######################
# shrink guessing word pool
#######################
# create new word bank that includes matched letters and/or matched index
# and excludes wrong letters
# store index values of words marked as having wrong guessed letters
# check splitWords for words that contain Wrong letters and remove them
def removeWrongLetters():
    global splitWords
    for word in splitWords:
        # iterate through wrong letter array

        for i in wrongLetters:
            # if wrong letter is in the word

            if i in word:
                # append index of words in splitWords that need to be removed
                filteredWords.append(splitWords.index(word))
                # once a wrong letter is found, break the loop.
                # otherwise it'll put in the same index multiple times for each wrong letter
                # found in a word
                break
        for x in correctLetters:
            # print(word.index(i))

            # checks if word doesnt contain any letters
            if x[1] not in word and splitWords.index(word) not in filteredWords:
                # print(x[1])
                # print(word)
                filteredWords.append(splitWords.index(word))
                break

        # all word at this point contain correct letters, though maybe not in the right place
        # all X in correct letters will either be less than 5 or = to 6
        # if word does not contain correct letter in correct position, eliminate
        for x in correctLetters:
            for v in word:
                if word.index(v) != x[0] and x[0] <= 4 and v == x[1] and splitWords.index(word) not in filteredWords:
                    # print(word.index(v), v)
                    # print(x[0], x[1])
                    # print(word)
                    filteredWords.append(splitWords.index(word))
                    break
    # print(filteredWords)
    # splitWords = np.delete(splitWords, filteredWords, axis=0)

    for x in sorted(filteredWords, reverse=True):
        del splitWords[x]

    # clear out list of words index
    filteredWords.clear()


# print(splitWords)
# removeWrongLetters()
# print("splitWords")
# print(splitWords)


#######################
# shrink guessing word pool
#######################
##############################

##############################
#######################
# select where to start looking for new guesses
#######################

# every word with a wrong letter has been filtered out
# check if all values in correctLetters == none, if so then exit and select a random
# new word from splitWords as the guess
def NoMatchingLetters():
    global splitWords
    global guessList

    # if no correct letters, then guess random new word
    if not correctLetters:
        # get the size of the splitWords array

        randomGuess = random.randint(0, len(splitWords))

        # select a random word within the array size to assign as the new guess
        guessList = splitWords[randomGuess]


# removeNoMatchingLetters()


def newGuess():
    global splitWords
    global guessList
    randomGuess = random.randint(0, len(splitWords) - 1)

    # select a random word within the array size to assign as the new guess
    guessList = splitWords[randomGuess]
    # print(guessList)


def answer():
    # print(guessList)
    #######################################################
    while guessList != testList:
        print(splitWords)
        print(guessList)
        # check for correct & wrong letters in guess
        findMatches()

        # remove all words from word bank that contain wrong letters
        # if there are correct letters in the guess, remove words that dont have correct letters
        # if there are correct letters in the correct position in the guess, remove words that dont have correctly
        # positioned letters
        removeWrongLetters()

        # if there are no matching letters in the guess, pick a new random word
        NoMatchingLetters()

        # select a random new word from the filtered word bank to use as the next guess
        newGuess()
    print("correct guess is ", guessList, " answer is = ", testList)


answer()
