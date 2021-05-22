# intervals

Intervals is a free-reign portfolio project as part of Codecademy's Computer Science career path. The assignment was to make a basic terminal project from scratch using Python that takes at least one user input. Additionally, a technical blog post and refactoring were encouraged. This readme will serve as the blog post.

This program was first constructed with two lists full of tuples. Each tuple contains an integer used for the primary function's internal logic and a string with either a musical note name or interval. The program then initiates by printing a greeting and declaring a variable "mode" as an empty string.

A function - "setup()" - asks the user to choose one of two game methods. The first provides two different note names for which the user must identify the musical interval between them. A second provides a starting note and interval for which the user must identify the note that interval away from the starting pitch. Error handlinging in the form of a loop, instructions, and the .upper() method on the input seek to assign a truthy value to "mode" before setup() calls interval_game() with "mode" as its sole argument.

Noting that interval_game() is called with a single argument is important because it can optionally take four others. The two arguments after mode are "correct" and "incorrect". They default to 0 and keep track of correct/incorrect answers. Last are "start_value" and "second_value". Those two values default to "None". The first step within the function is to detect whether those values are "None", and if they are they're assigned a random value in the range of the numbers in the tuples. Start note, second note, and interval values are then assigned using these values to select the index of the correct tuple within. "None" is also assigned to the variable of "difference".

An "if" statement then uses the "mode" argument to determine which game mode is played. Depending on the user-selected mode, a the program iterates through a list of either intervals or note names and prints it into a formatted list with possible answer values. The problem is then printed for the user - either two notes or a starting note and interval - again using formatted values from the original lists. An answer, labeled as "difference" is calculated based one of two ways:

1. If the game mode provides two notes: int((second_note[0] - start_note[0] + 12) % 12)
2. If the game mode provides a note and interval: int((second_note[0] + start_note[0]) % 12)

The index of zero finds the numerical value within a tuple within the list.

User input is then collected and saved to the variable "answer". If answer is the same value as "difference", "correct" is incremented by one and input asks if the player wants another problem. If they answer yes, interval_game() is called with mode, correct, and incorrect carried into it as arguments to preserve the values of each. If the user-provided answer is not the same value as "difference", a message lets the user know they are incorrect and gives the option to try the same question again. If they select yes, interval_game() is called with arguments mode, correct, incorrect, start_value, and second_value to preserve the values of each.

Should the user select not to continue, a message is printed that provides them a count of correct and incorrect answers.
