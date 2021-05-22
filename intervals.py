import random

note_values = [(0, "C"), (1, "C#/Db"), (2, "D"), (3, "D#/Eb"), (4, "E"), (5, "F"), (6, "F#/Gb"), (7, "G"), (8, "G#/Ab"), (9, "A"), (10, "A#/Bb"), (11, "B")]

interval_values = [(0, "Unison"), (1, "Minor Second"), (2, "Major Second"), (3, "Minor Third"), (4, "Major Third"), (5, "Perfect Fourth"), (6, "Tritone"), (7, "Perfect Fifth"), (8, "Minor Sixth"), (9, "Major Sixth"), (10, "Minor Seventh"), (11, "Major Seventh")]

print("Hello, welcome to Intervals, the music theory interval review game!")
mode = ""


def interval_game(mode, correct=0, incorrect=0, start_value=None, second_value=None):
    if start_value == None:
        start_value = random.randint(0, 11)
    if second_value == None:
        second_value = random.randint(0, 11)
    start_note = note_values[start_value]
    second_note = note_values[second_value]
    interval = interval_values[second_value]
    difference = None
    
    print("Here is a list of possible inputs:\n")
    if mode == "A":
        for i in range(len(note_values)):
            print(f"{interval_values[i][1]}: {interval_values[i][0]}\n")
        print(f"The starting note is {start_note[1]} and the second note is {second_note[1]}.")
        difference = int((second_note[0] - start_note[0] + 12) % 12)
        answer = int(input("What is the interval between the two notes? Please enter the interval's corresponding number: "))
    elif mode == "B":
        for i in range(len(note_values)):
            print(f"{note_values[i][1]}: {note_values[i][0]}\n")
        print(f"The starting note is {start_note[1]}, and the interval is {interval[1]}.")
        difference = int((second_note[0] + start_note[0]) % 12)
        answer = int(input(f"Which note is a(n) {interval[1]} away from the start note? Please enter the note's corresponding number: "))
    if answer == difference:
        correct += 1
        proceed = input("Good job, that is correct! Try another? (Y/N): ").upper()
        if proceed == "Y":
            interval_game(mode, correct, incorrect)
        else:
            print(f"You had {str(correct)} correct answers and {str(incorrect)} incorrect answers. Thank you for playing!")
            return
    else:
        while answer != difference:
            incorrect += 1
            proceed = input("Sorry, that is incorrect. Try again? (Y/N): ").upper()
            if proceed == "N":
                print(f"You had {str(correct)} correct answers and {str(incorrect)} incorrect answers. Thank you for playing!")
                return
            else:
                interval_game(mode, correct, incorrect, start_value, second_value)

def setup():
    mode = ""
    if mode != "A" or mode != "B":
        mode = input("Would you like to identify intervals given two notes and direction(A) or identify notes given a starting note and interval(B)? Answer A or B: ").upper()
    interval_game(mode)

setup()