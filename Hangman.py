HANGMAN = [
    """
 ------
|     |
|
|
|
|
|
|
----------
""",
    """
 ------
|     |
|     0
|
|
|
|
|
----------
""",
    """
 ------
|     |
|     0
|     +
|
|
|
|
----------
""",
    """
 ------
|     |
|     0
|    -+
|
|
|
|
----------
""",
    """
 ------
|     |
|     0
|    -+-
|
|
|
|
----------
""",
    """
 ------
|     |
|     0
|   /-+-
|
|
|
|
----------
""",
    """
 ------
|     |
|     0
|   /-+-/
|
|
|
|
----------
""",
    """
 ------
|     |
|     0
|   /-+-/
|     |
|
|
|
----------
""",
    """
 ------
|     |
|     0
|   /-+-/
|     |
|     |
|
|
----------
""",
    """
 ------
|     |
|     0
|   /-+-/
|     |
|     |
|    |
|    |
----------
""",
    """
 ------
|     |
|     0
|   /-+-/
|     |
|     |
|    | |
|    | |
----------
"""
]

secretWork = list("buttholelicker")

guessingWord = list(("_"*len(secretWork)))

overall_wrong_count = 0
loop_wrong_count = 0

while overall_wrong_count != 10 or secretWork != guessingWord:
    print(HANGMAN[overall_wrong_count])
    print(guessingWord)
    inputed_str = input("input your guess please: ")
    loop_wrong_count=0
    for i in range(len(secretWork)):
        if inputed_str == secretWork[i]:
            print(inputed_str)
            guessingWord[i] = secretWork[i]
            loop_wrong_count += 1

    if loop_wrong_count == 0:
        overall_wrong_count += 1
    if overall_wrong_count >= 11:
        print('You lost Cunt!')
    elif guessingWord == secretWork:
        print('You win Kunt!')
#help 