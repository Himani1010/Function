import random
NUMDIGITS = 3
MAXGUESS = 10

def getSecretNum():
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUMDIGITS):
        secretNum += str(numbers[i])
    return secretNum
def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'
    clue = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clue.append('Fermi')
        elif guess[i] in secretNum:
            clue.append('Pico')

        elif guess[i]!=secretNum[i]:
            clue.append('bagle')    
    return ' '.join(clue)

def isOnlyDigits(num):
    if num =='':
        return False
    for i in num:
        if i not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
    return True
print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUMDIGITS))
print('Here are some clues:')
print('When I say:    That means:')
print('  Pico - One digit is correct but in the wrong position.')
print('  Fermi- One digit is correct and in the right position.')
print('  None - No digit is correct.')

while True:
    secretNum = getSecretNum()
    print('I have thought up a number. You have %s guesses to get it.' % (MAXGUESS))
    numGuesses = 1
    while numGuesses <= MAXGUESS:
        guess=""
        print('guess',numGuesses)
        guess = input("Guess Again: ")
        clue = getClues(guess, secretNum)
        print(clue)
        numGuesses += 1
        if guess == secretNum:
            break
    print ('You ran out of guesses. The answer was ' + secretNum)
    print("do you want paly again?('yes or no;)")
    again=input("enter ('yes or no')")
    if again=='yes':
        continue
    else:
        break
    