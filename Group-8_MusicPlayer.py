import os
import time  # For implementing clear command and deletion of user file.
from Piano import *
from Flute import *
from Bell import *
from KaraokePlayer import *


def clear():
    return os.system("clear")


def logo():
    clear()
    print(
        50 * x
        + "****************************************************************************\n"
        + 50 * x
        + "*                 PMusk Music Player and Music Synthesizer                 *\n"
        + 50 * x
        + "*                       ECE 210 Signals & Systems                          *\n"
        + 50 * x
        + "****************************************************************************"
    )


def initializeProject():
    logo()
    print("WELCOME TO PMusk TECHNOLOGIES!!!\n\n\n")
    print("Press Spacebar to continue...")
    print("Press 0 to exit...")
    inp = input("Your Input:")
    if inp == " ":
        mainMenu()
    elif inp == "0":
        exit()
    else:
        error()
        initializeProject()


def mainMenu():
    logo()
    print("1) Synthesize Music!")
    print("2) Karaoke Player")
    print("3) Project Details!")
    inp1 = input("Enter your choice:")
    if inp1 == "1":
        logo()
        Synthesize()
    elif inp1 == "2":
        karaokePlayer()
        logo()
        print("Press Spacebar to go the Main Menu...")
        print("Press 0 to exit...")
        inp6 = input()
        if inp6 == " ":
            mainMenu()
        elif inp6 == "0":
            thanks()
        else:
            error()
    elif inp1 == "3":
        projectDetails()
        print("\n\nPress Spacebar to go the Main Menu...")
        print("Press 0 to exit...")
        inp6 = input()
        if inp6 == " ":
            mainMenu()
        elif inp6 == "0":
            thanks()
        else:
            error()
    else:
        error()
        mainMenu()


def projectDetails():
    logo()
    details = open("ProjectDetails.txt", "r")
    print(details.read())


def Synthesize():
    clear()
    logo()
    print("Choose the 'Genre' of your Composition")
    print("1) Romantic")
    print("2) Patriotic")
    print("3) Sad")
    print("4) Theme")
    print("5) Folk")
    print("6) Free")
    genre_input = int(input("Enter your Choice:"))
    genre = None
    if genre_input == 1:
        genre = "Romantic"
    elif genre_input == 2:
        genre = "Patriotic"
    elif genre_input == 3:
        genre = "Sad"
    elif genre_input == 4:
        genre = "Theme"
    elif genre_input == 5:
        genre = "Folk"
    elif genre_input == 6:
        genre = "Free"
    else:
        error()
        Synthesize()
    logo()
    print("Choose Instrument in which you want to Synthesize Music :")
    print("1) Piano")
    print("2) Flute")
    print("3) Bell")
    inp5 = input("Enter your Choice: ")
    if inp5 == "1":
        logo()
        piano(genre)
        print("Press Spacebar to go the Main Menu...")
        print("Press 0 to exit...")
        inp6 = input()
        if inp6 == " ":
            mainMenu()
        elif inp6 == "0":
            thanks()
        else:
            error()
    elif inp5 == "2":
        logo()
        flute(genre)
        print("Press Spacebar to go the Main Menu...")
        print("Press 0 to exit...")
        inp6 = input()
        if inp6 == " ":
            mainMenu()
        elif inp6 == "0":
            thanks()
        else:
            error()
    elif inp5 == "3":
        logo()
        bell(genre)
        print("Press Spacebar to go the Main Menu...")
        print("Press 0 to exit...")
        inp6 = input()
        if inp6 == " ":
            mainMenu()
        elif inp6 == "0":
            thanks()
        else:
            error()

    else:
        error()
        time.sleep(2)
        mainMenu()


def error():
    print("Please enter a correct choice..!!!")
    time.sleep(2)


def thanks():
    logo()
    print("THANK YOU FOR USING THE PMusk Music Player!")
    print(
        "Developers: \nSanskruti Shingala \nMansi Savaj \nPriya Bhoraniya \nKrinal Boghani \nUdit Kapadia "
    )
    time.sleep(10)
    clear()
    exit()


########################################
x = " "

initializeProject()

