import os
import time
from Piano import piano_player
from Flute import *
from Bell import *


x = " "


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


def karaokePlayer():
    logo()
    print("Choose the 'genre' of your choice")
    print("1) Romantic")
    print("2) Patriotic")
    print("3) Sad")
    print("4) Theme")
    print("5) Folk")
    inp2 = input("Enter your choice:")
    if inp2 == "1":
        os.chdir("./Romantic")
        logo()
        print("1) Janam")
        print("2) SanamRe")
        print("3) Bol Do Na Zara")
        print("4) Galiyan")
        print("5) Tuje Dekha")
        print("6) Vaste")
        print("7) Go Back to Menu")
        print("8) Exit")
        print("9) I want to choose my file")
        inp3 = input("Enter Your Choice:")
        if inp3 == "1":
            logo()
            print("Choose music instrument:")
            print("1) Piano")
            print("2) Flute")
            print("3) Bell")
            inp4 = input("Enter Your Choice:")
            if inp4 == "1":
                piano_player("Janam")
                os.chdir("..")
            elif inp4 == "2":
                flute_player("Janam")
                os.chdir("..")
            elif inp4 == "3":
                bell_player("Janam")
                os.chdir("..")
            else:
                os.chdir("..")
                error()
                karaokePlayer()
        elif inp3 == "2":
            clear()
            logo()
            print("Choose music instrument:")
            print("1) Piano")
            print("2) Flute")
            print("3) Bell")
            inp4 = input("Enter Your Choice:")
            if inp4 == "1":
                piano_player("SanamRe")
                os.chdir("..")
            elif inp4 == "2":
                flute_player("SanamRe")
                os.chdir("..")
            elif inp4 == "3":
                bell_player("SanamRe")
                os.chdir("..")
            else:
                os.chdir("..")
                error()
                karaokePlayer()
        elif inp3 == "3":
            clear()
            logo()
            print("Choose music instrument:")
            print("1) Piano")
            print("2) Flute")
            print("3) Bell")
            inp4 = input("Enter Your Choice:")
            if inp4 == "1":
                piano_player("bolDonazara")
                os.chdir("..")
            elif inp4 == "2":
                flute_player("bolDonazara")
                os.chdir("..")
            elif inp4 == "3":
                bell_player("bolDonazara")
                os.chdir("..")
            else:
                os.chdir("..")
                error()
                karaokePlayer()
        elif inp3 == "4":
            clear()
            logo()
            print("Choose music instrument:")
            print("1) Piano")
            print("2) Flute")
            print("3) Bell")
            inp4 = input("Enter Your Choice:")
            if inp4 == "1":
                piano_player("Galiyan")
                os.chdir("..")
            elif inp4 == "2":
                flute_player("Galiyan")
                os.chdir("..")
            elif inp4 == "3":
                bell_player("Galiyan")
                os.chdir("..")
            else:
                os.chdir("..")
                error()
                karaokePlayer()
        elif inp3 == "5":
            clear()
            logo()
            print("Choose music instrument:")
            print("1) Piano")
            print("2) Flute")
            print("3) Bell")
            inp4 = input("Enter Your Choice:")
            if inp4 == "1":
                piano_player("TujeDekha")
                os.chdir("..")
            elif inp4 == "2":
                flute_player("TujeDekha")
                os.chdir("..")
            elif inp4 == "3":
                bell_player("TujeDekha")
                os.chdir("..")
            else:
                os.chdir("..")
                error()
                karaokePlayer()
        elif inp3 == "6":
            clear()
            logo()
            print("Choose music instrument:")
            print("1) Piano")
            print("2) Flute")
            print("3) Bell")
            inp4 = input("Enter Your Choice:")
            if inp4 == "1":
                piano_player("vaste")
                os.chdir("..")
            elif inp4 == "2":
                flute_player("vaste")
                os.chdir("..")
            elif inp4 == "3":
                bell_player("vaste")
                os.chdir("..")
            else:
                os.chdir("..")
                error()
                karaokePlayer()
        elif inp3 == "7":
            os.chdir("..")
            karaokePlayer()
        elif inp3 == "8":
            thanks()
        elif inp3 == "9":
            user_music_choice()
    elif inp2 == "2":
        os.chdir("./Patriotic")
        clear()
        logo()
        print("1) National Anthem")
        print("2) Sare Jahan se Accha")
        print("3) AeWatan")
        print("4) Go Back to Menu")
        print("5) Exit")
        print("6) I want to choose my file")
        inp3 = input("Enter Your Choice:")
        if inp3 == "1":
            clear()
            logo()
            print("Choose music instrument:")
            print("1) Piano")
            print("2) Flute")
            print("3) Bell")
            inp4 = input("Enter Your Choice:")
            if inp4 == "1":
                piano_player("NationalAnthem")
                os.chdir("..")
            elif inp4 == "2":
                flute_player("NationalAnthem")
                os.chdir("..")
            elif inp4 == "3":
                bell_player("NationalAnthem")
                os.chdir("..")
            else:
                os.chdir("..")
                error()
                karaokePlayer()
        elif inp3 == "2":
            clear()
            logo()
            print("Choose music instrument:")
            print("1) Piano")
            print("2) Flute")
            print("3) Bell")
            inp4 = input("Enter Your Choice:")
            if inp4 == "1":
                piano_player("SareJahan")
                os.chdir("..")
            elif inp4 == "2":
                flute_player("SareJahan")
                os.chdir("..")
            elif inp4 == "3":
                bell_player("SareJahan")
                os.chdir("..")
            else:
                os.chdir("..")
                error()
                karaokePlayer()
        elif inp3 == "3":
            clear()
            logo()
            print("Choose music instrument:")
            print("1) Piano")
            print("2) Flute")
            print("3) Bell")
            inp4 = input("Enter Your Choice:")
            if inp4 == "1":
                piano_player("AeWatan")
                os.chdir("..")
            elif inp4 == "2":
                flute_player("AeWatan")
                os.chdir("..")
            elif inp4 == "3":
                bell_player("AeWatan")
                os.chdir("..")
            else:
                os.chdir("..")
                error()
                karaokePlayer()
        elif inp3 == "4":
            os.chdir("..")
            karaokePlayer()
        elif inp3 == "5":
            thanks()
        elif inp3 == "6":
            user_music_choice()

    elif inp2 == "3":  # PAGE2(3)
        os.chdir("./Sad")
        clear()
        logo()
        print("1) Ae Dil Hain Muskil")
        print("2) Samajawan")
        print("3) Kal ho na ho")
        print("4) Tadap tadap")
        print("5) Jeena Yaha marna yaha")
        print("6) Bulleya")
        print("7) Main dhoondne ko zammane")
        print("8) Go Back to Menu")
        print("9) Exit")
        print("10) I want to choose my file")
        inp3 = input("Enter Your Choice:")
        if inp3 == "1":
            clear()
            logo()
            print("Choose music instrument:")
            print("1) Piano")
            print("2) Flute")
            print("3) Bell")
            inp4 = input("Enter Your Choice:")
            if inp4 == "1":
                piano_player("YeDilHainMuskil")
                os.chdir("..")
            elif inp4 == "2":
                flute_player("YeDilHainMuskil")
                os.chdir("..")
            elif inp4 == "3":
                bell_player("YeDilHainMuskil")
                os.chdir("..")
            else:
                os.chdir("..")
                error()
                karaokePlayer()
        elif inp3 == "2":
            clear()
            logo()
            print("Choose music instrument:")
            print("1) Piano")
            print("2) Flute")
            print("3) Bell")
            inp4 = input("Enter Your Choice:")
            if inp4 == "1":
                piano_player("Samjawan")
                os.chdir("..")
            elif inp4 == "2":
                flute_player("Samjawan")
                os.chdir("..")
            elif inp4 == "3":
                bell_player("Samjawan")
                os.chdir("..")
            else:
                os.chdir("..")
                error()
                karaokePlayer()
        elif inp3 == "3":
            clear()
            logo()
            print("Choose music instrument:")
            print("1) Piano")
            print("2) Flute")
            print("3) Bell")
            inp4 = input("Enter Your Choice:")
            if inp4 == "1":
                piano_player("kalhonaho")
                os.chdir("..")
            elif inp4 == "2":
                flute_player("kalhonaho")
                os.chdir("..")
            elif inp4 == "3":
                bell_player("kalhonaho")
                os.chdir("..")
            else:
                os.chdir("..")
                error()
                karaokePlayer()
        elif inp3 == "4":
            clear()
            logo()
            print("Choose music instrument:")
            print("1) Piano")
            print("2) Flute")
            print("3) Bell")
            inp4 = input("Enter Your Choice:")
            if inp4 == "1":
                piano_player("Tadap")
                os.chdir("..")
            elif inp4 == "2":
                flute_player("Tadap")
                os.chdir("..")
            elif inp4 == "3":
                bell_player("Tadap")
                os.chdir("..")
            else:
                os.chdir("..")
                error()
                karaokePlayer()
        elif inp3 == "5":
            clear()
            logo()
            print("Choose music instrument:")
            print("1) Piano")
            print("2) Flute")
            print("3) Bell")
            inp4 = input("Enter Your Choice:")
            if inp4 == "1":
                piano_player("jeenayaha")
                os.chdir("..")
            elif inp4 == "2":
                flute_player("jeenayaha")
                os.chdir("..")
            elif inp4 == "3":
                bell_player("jeenayaha")
                os.chdir("..")
            else:
                os.chdir("..")
                error()
                karaokePlayer()
        elif inp3 == "6":
            clear()
            logo()
            print("Choose music instrument:")
            print("1) Piano")
            print("2) Flute")
            print("3) Bell")
            inp4 = input("Enter Your Choice:")
            if inp4 == "1":
                piano_player("bulleya")
                os.chdir("..")
            elif inp4 == "2":
                flute_player("bulleya")
                os.chdir("..")
            elif inp4 == "3":
                bell_player("bulleya")
                os.chdir("..")
            else:
                os.chdir("..")
                error()
                karaokePlayer()
        elif inp3 == "7":
            clear()
            logo()
            print("Choose music instrument:")
            print("1) Piano")
            print("2) Flute")
            print("3) Bell")
            inp4 = input("Enter Your Choice:")
            if inp4 == "1":
                piano_player("maindhundhane")
                os.chdir("..")
            elif inp4 == "2":
                flute_player("maindhundhane")
                os.chdir("..")
            elif inp4 == "3":
                bell_player("maindhundhane")
                os.chdir("..")
            else:
                os.chdir("..")
                error()
                karaokePlayer()
        elif inp3 == "8":
            os.chdir("..")
            karaokePlayer()
        elif inp3 == "9":
            thanks()
        elif inp3 == "10":
            user_music_choice()

    elif inp2 == "4":
        os.chdir("./Theme")
        clear()
        logo()
        print("1) Friends")
        print("2) Harry Potter")
        print("3) Om Shanti Om")
        print("4) Birthday Song")
        print("5) Jingle Bell")
        print("6) Go Back to Menu")
        print("7) Exit")
        print("8) I want to choose my file")
        inp3 = input("Enter Your Choice:")
        if inp3 == "1":
            clear()
            logo()
            print("Choose music instrument:")
            print("1) Piano")
            print("2) Flute")
            print("3) Bell")
            inp4 = input("Enter Your Choice:")
            if inp4 == "1":
                piano_player("friends")
                os.chdir("..")
            elif inp4 == "2":
                flute_player("friends")
                os.chdir("..")
            elif inp4 == "3":
                bell_player("friends")
                os.chdir("..")
            else:
                os.chdir("..")
                error()
                karaokePlayer()
        elif inp3 == "2":
            clear()
            logo()
            print("Choose music instrument:")
            print("1) Piano")
            print("2) Flute")
            print("3) Bell")
            inp4 = input("Enter Your Choice:")
            if inp4 == "1":
                piano_player("HarryPotter")
                os.chdir("..")
            elif inp4 == "2":
                flute_player("HarryPotter")
                os.chdir("..")
            elif inp4 == "3":
                bell_player("HarryPotter")
                os.chdir("..")
            else:
                os.chdir("..")
                error()
                karaokePlayer()
        elif inp3 == "3":
            clear()
            logo()
            print("Choose music instrument:")
            print("1) Piano")
            print("2) Flute")
            print("3) Bell")
            inp4 = input("Enter Your Choice:")
            if inp4 == "1":
                piano_player("OmShantiOm")
                os.chdir("..")
            elif inp4 == "2":
                flute_player("OmShantiOm")
                os.chdir("..")
            elif inp4 == "3":
                bell_player("OmShantiOm")
                os.chdir("..")
            else:
                os.chdir("..")
                error()
                karaokePlayer()
        elif inp3 == "4":
            clear()
            logo()
            print("Choose music instrument:")
            print("1) Piano")
            print("2) Flute")
            print("3) Bell")
            inp4 = input("Enter Your Choice:")
            if inp4 == "1":
                piano_player("birthdaySong")
                os.chdir("..")
            elif inp4 == "2":
                flute_player("birthdaySong")
                os.chdir("..")
            elif inp4 == "3":
                bell_player("birthdaySong")
                os.chdir("..")
            else:
                os.chdir("..")
                error()
                karaokePlayer()
        elif inp3 == "5":
            clear()
            logo()
            print("Choose music instrument:")
            print("1) Piano")
            print("2) Flute")
            print("3) Bell")
            inp4 = input("Enter Your Choice:")
            if inp4 == "1":
                piano_player("jinglebell")
                os.chdir("..")
            elif inp4 == "2":
                flute_player("jinglebell")
                os.chdir("..")
            elif inp4 == "3":
                bell_player("jinglebell")
                os.chdir("..")
            else:
                os.chdir("..")
                error()
                karaokePlayer()
        elif inp3 == "6":
            os.chdir("..")
            karaokePlayer()
        elif inp3 == "7":
            thanks()
        elif inp3 == "8":
            user_music_choice()

    elif inp2 == "5":
        os.chdir("./Folk")
        clear()
        logo()
        print("1) Raghupati Raghav")
        print("2) Ghoomar")
        print("3) Dholida")
        print("4) Namo Namo")
        print("5) Go Back to Menu")
        print("6) Exit")
        print("7) I want to choose my file")
        inp3 = input("Enter Your Choice:")
        if inp3 == "1":
            clear()
            logo()
            print("Choose music instrument:")
            print("1) Piano")
            print("2) Flute")
            print("3) Bell")
            inp4 = input("Enter Your Choice:")
            if inp4 == "1":
                piano_player("raghupatiraghav")
                os.chdir("..")
            elif inp4 == "2":
                flute_player("raghupatiraghav")
                os.chdir("..")
            elif inp4 == "3":
                bell_player("raghupatiraghav")
                os.chdir("..")
            else:
                os.chdir("..")
                error()
                karaokePlayer()
        elif inp3 == "2":
            clear()
            logo()
            print("Choose music instrument:")
            print("1) Piano")
            print("2) Flute")
            print("3) Bell")
            inp4 = input("Enter Your Choice:")
            if inp4 == "1":
                piano_player("ghoomar")
                os.chdir("..")
            elif inp4 == "2":
                flute_player("ghoomar")
                os.chdir("..")
            elif inp4 == "3":
                bell_player("ghoomar")
                os.chdir("..")
            else:
                os.chdir("..")
                error()
                karaokePlayer()
        elif inp3 == "3":
            clear()
            logo()
            print("Choose music instrument:")
            print("1) Piano")
            print("2) Flute")
            print("3) Bell")
            inp4 = input("Enter Your Choice:")
            if inp4 == "1":
                piano_player("dholida")
                os.chdir("..")
            elif inp4 == "2":
                flute_player("dholida")
                os.chdir("..")
            elif inp4 == "3":
                bell_player("dholida")
                os.chdir("..")
            else:
                os.chdir("..")
                error()
                karaokePlayer()
        elif inp3 == "4":
            clear()
            logo()
            print("Choose music instrument:")
            print("1) Piano")
            print("2) Flute")
            print("3) Bell")
            inp4 = input("Enter Your Choice:")
            if inp4 == "1":
                piano_player("namonamo")
                os.chdir("..")
            elif inp4 == "2":
                flute_player("namonamo")
                os.chdir("..")
            elif inp4 == "3":
                bell_player("namonamo")
                os.chdir("..")
            else:
                os.chdir("..")
                error()
                karaokePlayer()

        elif inp3 == "5":
            os.chdir("..")
            karaokePlayer()
        elif inp3 == "6":
            thanks()
        elif inp3 == "7":
            user_music_choice()
    else:
        error()
        karaokePlayer()


def error():
    print("Please enter a correct choice..!!!")
    time.sleep(2)


def thanks():
    logo()
    print("THANK YOU FOR USING THE PMusk Music & Karaoke Player!")
    print(
        "Developers: \nSanskruti Shingala \nMansi Savaj \nPriya Bhoraniya \nKrinal Boghani \nUdit Kapadia "
    )
    time.sleep(3)
    clear()
    exit()


def user_music_choice():
    clear()
    logo()
    user_choice = input("Enter Your File Name:")
    print("Choose music instrument:")
    print("1) Piano")
    print("2) Flute")
    print("3) Bell")
    inp4 = input("Enter Your Choice:")
    if inp4 == "1":
        piano_player(user_choice)
        os.chdir("..")
    elif inp4 == "2":
        flute_player(user_choice)
        os.chdir("..")
    elif inp4 == "3":
        bell_player(user_choice)
        os.chdir("..")
    else:
        os.chdir("..")
        error()
        karaokePlayer()
