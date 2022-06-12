# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
---------------------------------------------
  RAFFLES UNIVERSITY CODING CHALLENGES 2022
---------------------------------------------

    Challenge 1: Find the second largest element in an list
    Challenge 2: Calculate grade of the final exam
    Challenge 3: Build a simple word game

Date of completion: 12 June 2022

NOTE: You're highly recommended to execute this code in
      a terminal that supports colored output.
"""

import os
import random
import sys
import requests
from typing import List
from time import perf_counter, sleep
from colorama import init, Fore, Back, Style

__author__ = "Melvin Chia"
__copyright__ = "Copyright 2022, thecodeblog.net"
__license__ = "MIT"
__version__ = "final"
__maintainer__ = "Melvin Chia"
__email__ = "melvinchia@thecodeblog.net"

init()  # initialize the colorama module required for colored output

# ----- START CHALLLENGE 1 -----


def findSecondLargest_approach_1(lst: List[int]) -> int:
    """
    Find the second largest element in a list with Python built-in functions.

    Time complexity: O(n log n)
    Space complexity: O(1)

    Args:
        lst (int []): A list of numbers

    Raises:
        ValueError: If the length of the list is lesser than two.
        ValueError: If the list contains non-integers.

    Returns:
        int: The second largest element in the list.
    """

    if len(lst) < 2:
        raise ValueError("The list must have at least 2 elements")

    if not all(isinstance(x, int) for x in lst):
        raise ValueError("The list must contain only integers")

    return sorted(lst)[-2]


def findSecondLargest_approach_2(lst: List[int]) -> int:
    """
    Find the second largest element in a list in the fastest way possible.
    It loops through the list, checks if the current element is larger than
    the previous recorded largest element or the second largest, and if so,
    replaces the previous.

    Time complexity: O(n)
    Space complexity: O(1)

    Args:
        lst (int []): A list of numbers.

    Raises:
        ValueError: If the length of the list is lesser than two.
        ValueError: If the list contains non-integers.

    Returns:
        int: The second largest element in the list.
    """

    if len(lst) < 2:
        raise ValueError("The list must have at least 2 elements")

    if not all(isinstance(x, int) for x in lst):
        raise ValueError("The list must contain only integers")

    # initialize both variable to infinite so that they can be correctly
    # compared and replaced
    first = second = float('inf')

    for i in lst:
        if i > first:
            second, first = first, i
        elif i > second:
            second = i

    return second


def executeFirstChallenge() -> None:  # driver code
    """
    Find the second largest number in any given list.

    Approach Count: 2

        1st Approach:
            Using Python built-in functions.

            Time complexity: O(n log n)
            Space complexity: O(1)

        2nd Approach:
            Using a loop.

            Time complexity: O(n)
            Space complexity: O(1)

    Test Cases:
        Test Count: 5
        List Length: 10000
        List Elements: -10000 <= lst[n] <= 10000
    """

    newLine()
    print(Fore.MAGENTA +
          "CHALLENGE 1: Find the second largest element in an list" + Style.RESET_ALL)

    challenge_1_approach = [
        {
            'approach': findSecondLargest_approach_1,
            'description': 'Using Python built-in functions',
        },
        {
            'approach': findSecondLargest_approach_2,
            'description': 'Using a loop',
        }
    ]

    for index, approach in enumerate(challenge_1_approach):
        newLine()
        print(
            Fore.CYAN + f"APPROACH {index + 1}: {approach['description']}" + Style.RESET_ALL)
        newLine()

        total_time = 0

        for _ in range(5):
            # generate a list of random numbers and print them out
            arr = [random.randint(-10000, 10000) for _ in range(10000)]
            print("Input: ".ljust(10), "[{}, ..., {}]".format(
                ", ".join(map(str, arr[:3])), ", ".join(map(str, arr[-3:]))))

            # execute the function and check if the return value is what we expect
            start = perf_counter()
            ans = findSecondLargest_approach_1(arr)
            stop = perf_counter()
            time = stop - start
            total_time += time

            assert ans == sorted(
                arr)[-2], "The return value of this function is not the second largest"

            # sort the array and print it out for clearer presentation
            sorted_arr = sorted(arr)
            sorted_arr[-2] = Fore.CYAN + str(sorted_arr[-2]) + Style.RESET_ALL
            print("Sorted: ".ljust(10), "[{}, ..., {}]".format(
                ", ".join(map(str, sorted_arr[:3])), ", ".join(map(str, sorted_arr[-3:]))))

            print("Output: ".ljust(10), Fore.CYAN +
                  str(ans) + Style.RESET_ALL)
            print(Fore.GREEN + "Time: ".ljust(10),
                  "{:.6f}s".format(stop - start) + Style.RESET_ALL)

            newLine()

        print(Fore.YELLOW +
              "Total Time: {}s".format("{:.6f}".format(total_time)) + Style.RESET_ALL)

# ----- END CHALLENGE 1 -----

# ----- START CHALLENGE 2 -----


def calculateMark() -> None:
    """
    Calculate the mark of the final exam.
    First the user is asked to enter the score of each question.
    An error message will be shown if user enters an invalid score.
    Then the system will calculate the total mark, the average mark and the grade.
    Finally, these values will be printed out nicely.
    """

    GRADE_LETTERS = ["A", "B", "C", "D", "F"]
    GRADE_BOUNDARIES = [90, 80, 70, 60, 0]

    def calculateGrade(avg): return GRADE_LETTERS[[i for i, x in enumerate(
        GRADE_BOUNDARIES) if x <= avg][0]]

    marks: List[float] = []
    left = 5

    while left:
        mark = input(
            Style.RESET_ALL + f"Enter mark for {Fore.YELLOW}question {5-left + 1}{Style.RESET_ALL}: " + Fore.CYAN)

        try:
            mark = float(mark)
        except ValueError:
            print(Fore.RED + "Invalid input." + Style.RESET_ALL)
            continue

        if mark < 0 or mark > 100:
            print(
                Fore.RED + "Invalid mark. Please enter a number between 0 and 100." + Style.RESET_ALL)
            continue

        marks.append(mark)
        left -= 1

    total = sum(marks)
    average = total / len(marks)
    grade = calculateGrade(average)

    if grade == "F":
        grade = Fore.RED + grade + Style.RESET_ALL

    newLine()
    print(Fore.GREEN + "Total:".ljust(10) + Style.RESET_ALL + str(total))
    print(Fore.GREEN + "Average: ".ljust(10) + Style.RESET_ALL + str(average))
    print(Fore.GREEN + "Grade: ".ljust(10) + Style.RESET_ALL + str(grade))


def executeSecondChallenge() -> None:  # driver code
    """
    Calculate the mark of the final exam.
    """

    print(Fore.MAGENTA +
          "CHALLENGE 2: Calculate grade of the final exam" + Style.RESET_ALL)
    newLine()

    calculateMark()

# ----- END CHALLENGE 2 -----

# ----- START OF CHALLENGE 3 -----


class WordGame:
    WORD_LIST_API_ENDPOINT = "https://wordcounter.net/site/add-simple-words"
    DICTIONARY_API_ENDPOINT = "https://api.dictionaryapi.dev/api/v2/entries/en/{}"

    def __init__(self):
        self.rounds = 0
        self.win = 0
        self.lose = 0

        clear()

        print(Fore.YELLOW + "Initializing the Game..." + Style.RESET_ALL)

        if not self.checkInternetConnection():
            newLine()
            print(Fore.RED + "No internet connection.\nPlease connect to the internet and try again." + Style.RESET_ALL)
            exit()

        self.words = self.fetchWords()

    def checkInternetConnection(self) -> bool:
        try:
            requests.get("https://www.google.com")
            return True
        except requests.exceptions.ConnectionError:
            return False

    def fetchWords(self) -> List[str]:
        words = requests.get(self.WORD_LIST_API_ENDPOINT, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }).json()

        return [word["simple_words"] for word in words["simple_words"] if len(word["simple_words"]) > 3]

    def printBanner(self) -> None:
        print(Fore.YELLOW + """
     __      __                .___   ________                       
    /  \    /  \___________  __| _/  /  _____/_____    _____   ____  
    \   \/\/   /  _ \_  __ \/ __ |  /   \  ___\__  \  /     \_/ __ \ 
     \        (  <_> )  | \/ /_/ |  \    \_\  \/ __ \|  Y Y  \  ___/ 
      \__/\  / \____/|__|  \____ |   \______  (____  /__|_|  /\___  >
           \/                   \/          \/     \/      \/     \/ 
        """ + Style.RESET_ALL)

    def printStats(self) -> None:
        print(Back.CYAN + Fore.BLACK +
              f" {f'Win: {self.win}' : <20}{f'Round {self.rounds}' : ^32}{f'Lose: {self.lose}' : >20} " + Style.RESET_ALL)

    def generateLetters(self) -> List[str]:
        word = set(random.choice(self.words))
        letters = random.sample(list(word), k=min(
            random.randint(1, 5), len(word)-2))

        return letters

    def printLetters(self, letters: List[str]) -> None:
        newLine(2)
        print(
            f"{' - '.join(Fore.YELLOW + letter + Style.RESET_ALL for letter in letters) : ^{74 + len(letters)*9}}")
        newLine(2)

    def printDescription(self) -> None:
        print("You're required to enter a word that contains".center(74))
        print("all the letters above.".center(74))
        newLine()
        print(("Press " + Fore.MAGENTA + "Ctrl + C" + Style.RESET_ALL + " to quit the game.").center(83))
        newLine(2)

    def promptAnswer(self) -> str:
        while True:
            answer = input("Enter your word: " + Fore.CYAN)
            if not answer:
                print(Fore.RED + "Please enter a word." + Style.RESET_ALL)
                continue
            if not all(x.isalpha() for x in answer):
                print(
                    Fore.RED + "Your answer should only consist of letters" + Style.RESET_ALL)
                continue
            break

        return answer

    def checkAnswer(self, answer: str, letters: str) -> bool:
        newLine()
        print(Fore.YELLOW + "Validating your answer..." + Style.RESET_ALL)
        newLine()

        answer = answer.lower()
        res = requests.get(
            self.DICTIONARY_API_ENDPOINT.format(answer)).json()

        if 'title' in res and res['title'] == "No Definitions Found":
            print(Fore.RED + "Invalid word." + Style.RESET_ALL)
            return False

        if not all(x in answer for x in letters):
            print(
                Fore.RED + f"Your word doesn't contain the letter {', '.join(x for x in letters if x not in answer)}." + Style.RESET_ALL)
            return False

        return True

    def updateScore(self, is_win: bool) -> None:
        if is_win:
            print(Fore.GREEN + "Your answer is correct!" + Style.RESET_ALL)
            self.win += 1
        else:
            self.lose += 1

    def play(self):
        while True:
            self.rounds += 1

            clear()
            letters = self.generateLetters()

            self.printBanner()
            self.printStats()
            self.printLetters(letters)
            self.printDescription()

            answer = self.promptAnswer()

            isWin = self.checkAnswer(answer, letters)
            self.updateScore(isWin)

            sleep(2)


def executeThirdChallenge() -> None:  # driver code
    """
    Play a word game.
    """

    print(Fore.MAGENTA +
          "CHALLENGE 3: Word Game" + Style.RESET_ALL)
    newLine()
    input(Fore.GREEN + "Press Enter to start the game..." + Style.RESET_ALL)

    game = WordGame()
    game.play()


# ----- END OF CHALLENGE 3 -----

# function to clear the terminal screen
def clear(): return os.system('cls' if os.name == 'nt' else 'clear')
def newLine(line=1): print("\n" * (line-1))


if __name__ == '__main__': # driver code

    challenges = [
        executeFirstChallenge,
        executeSecondChallenge,
        executeThirdChallenge
    ]

    # loop through the challlenges one by one
    for index, challenge in enumerate(challenges):
        try:
            clear()
            challenge()
            newLine()

            if index != len(challenges) - 1:
                input(Fore.GREEN + "Press Enter to continue..." + Style.RESET_ALL)

        # handling keyboard interrupt so that the program can exit gracefully
        except KeyboardInterrupt:
            newLine(2)
            print(Fore.RED + "Exiting..." + Style.RESET_ALL)
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)
