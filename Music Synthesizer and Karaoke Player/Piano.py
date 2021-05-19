from scipy.io.wavfile import write
import numpy as np
from subprocess import call
import os
import matplotlib.pyplot as plt

samplerate = 44100


def piano_notes():
    """
    Returns a dict object for all the piano 
    note's frequencies
    """
    # White keys are in Uppercase and black keys (sharps) are in lowercase
    note_freqs = {
        "C1": 130.82,
        "c1": 138.59,
        "D1": 146.83,
        "d1": 155.56,
        "E1": 164.81,
        "F1": 174.61,
        "f1": 185,
        "G1": 196,
        "g1": 207.65,
        "A1": 220,
        "a1": 233.08,
        "B1": 246.94,
        "C2": 261.63,
        "c2": 277.18,
        "D2": 293.66,
        "d2": 311.13,
        "E2": 329.63,
        "F2": 349.23,
        "f2": 369.99,
        "G2": 392,
        "g2": 415.3,
        "A2": 440,
        "a2": 466.16,
        "B2": 493.88,
        "C3": 523.25,
        "c3": 554.37,
        "D3": 587.33,
        "d3": 622.25,
        "E3": 659.26,
        "F3": 698.46,
        "f3": 739.99,
        "G3": 783.99,
        "g3": 830.61,
        "A3": 880,
        "a3": 932.33,
        "B3": 987.77,
        " ": 0.00,
    }
    return note_freqs


def piano_wave(freq, duration=0.5):
    amplitude = 4096
    global time
    time = np.linspace(0, duration, int(samplerate * duration))

    wave = (
        amplitude
        * (2 / np.pi)
        * (
            np.sin(2 * np.pi * freq * time)
            - (1 / 2) * np.sin(2 * np.pi * 2 * freq * time)
            + (1 / 3) * np.sin(2 * np.pi * 3 * freq * time)
            - (1 / 4) * np.sin(2 * np.pi * 4 * freq * time)
            + (1 / 5) * np.sin(2 * np.pi * 5 * freq * time)
            - (1 / 6) * np.sin(2 * np.pi * 6 * freq * time)
            + (1 / 7) * np.sin(2 * np.pi * 7 * freq * time)
            - (1 / 8) * np.sin(2 * np.pi * 8 * freq * time)
            + (1 / 9) * np.sin(2 * np.pi * 9 * freq * time)
        )
    )
    return wave


def piano_keys(userInput):
    note_freqs = piano_notes()
    global song
    song = [piano_wave(note_freqs[note]) for note in userInput.split("-")]
    song = np.concatenate(song)
    return song.astype(np.int16)


def piano_inputs():
    global userInput
    userInput = input(
        "Enter your set of notes from below (seperated by hyphens '-'):\n"
    )
    return userInput


def piano_file():
    global fileName
    fileName = input("Enter your desired File Name: ")
    store_file = open(fileName + ".txt", "w+")
    store_file.write(userInput)
    store_file.close()
    write(fileName + ".wav", samplerate, data.astype(np.int16))
    return fileName


def piano_visualize():
    x = np.array(time)
    y = np.array(song)
    plt.figure("Wave Output")
    plt.title("Sound Wave")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.plot(x[0:500], y[0:500])
    plt.show()


def piano(genre):
    os.chdir("./" + genre)
    global data
    data = piano_keys(piano_inputs())
    data = data * (16300 / np.max(data))
    call(["aplay", piano_file() + ".wav"])
    piano_visualize()
    os.remove(fileName + ".wav")
    os.chdir("..")


def piano_player(input):
    temp_notes = open(input + ".txt", "r")
    global data
    data = piano_keys(temp_notes.read())
    data = data * (16300 / np.max(data))
    write(input + ".wav", samplerate, data.astype(np.int16))
    call(["aplay", "-d", "15", input + ".wav"])
    piano_visualize()
    os.remove(input + ".wav")
