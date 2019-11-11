import os
import random
from os import listdir
from os.path import isfile, join
from tkinter import Tk, Frame, Button, filedialog, Label
from pydub import AudioSegment
from pydub.playback import play
from threading import Thread
import threading
import simpleaudio
import psutil
import sys

global directory 
directory = os.getcwd()

global tracks
tracks = []

exit_call = False

current_index = 0
current_song = "Nothing playing."

play = None

def choose_directory():
    global tracks
    directory = filedialog.askdirectory()
    print(directory)
    tracks = [f for f in listdir('music') if isfile(join('music', f))]
    random.shuffle(tracks) # Shuffle the array order
    play_music()
    ##music_thread = Thread(target=play_music)
    ##music_thread.start()
    
def play_music():
    global play
    global tracks
    current_song = "♫ " + tracks[current_index]
    current_music.config(text=current_song)
    current_music.update()
    print("Playing " + tracks[current_index])
    song = simpleaudio.WaveObject.from_wave_file(join('music', tracks[current_index]))
    play = song.play()
    #song = AudioSegment.from_mp3(join('music', tracks[0]))
    #play(song)

def stop_music():
    global play
    play.stop()

def skip_music():
    global current_index
    global tracks
    stop_music()    

    if current_index >= len(tracks) - 1:
        current_index = 0
    else:
        current_index += 1

    play_music()

root = Tk()
root.title("Audebil Music")
root.config(bg='#2C2F33')
root.geometry("860x260")

frame = Frame(root, background="#cb7972")
bottomFrame = Frame(root, background="#2C2F33")
frame.pack(side="top", fill="both", expand=True)
bottomFrame.pack(side="bottom", fill="both", expand=True)

current_music = Label(frame, text=current_song, fg="white", bg="#cb7972", font=("Avenir Next", 44))
#current_music.pack(side="top")

stop_song = Button(bottomFrame, text="⏹️", command=stop_music, bg="#cb7972", highlightthickness = 0, bd = 0, font=("Avenir Next", 20))
#stop_song.pack()

skip_song = Button(bottomFrame, text="⏭️", command=skip_music, bg="#cb7972", highlightthickness = 0, bd = 0, font=("Avenir Next", 20))
#skip_song.pack()

directory_button = Button(bottomFrame, text="Directory...", command=choose_directory, highlightthickness = 0, bd = 0, bg="#cb7972", font=("Avenir Next", 20))
#directory_button.pack()

current_music.place(x=450, y=60, anchor="center")

stop_song.place(x=300, y=60, anchor="center")
skip_song.place(x=370, y=60, anchor="center")
directory_button.place(x=500, y=60, anchor="center")

#stop_song.grid(row=0, column=0, sticky="w")
#skip_song.grid(row=0, column=1, sticky="w")
#directory_button.grid(row=0, column=2, sticky="w")

#root.iconbitmap(r'/home/nkomarn/Documents/MusicPlayer/icon.ico')
root.mainloop()