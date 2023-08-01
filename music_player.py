#Music Player using Python GUI
from tkinter import *
from tkinter import filedialog
import pygame.mixer as mixer
import os

mixer.init()

root = Tk()
root.geometry('800x250')
root.title('Music Player')
root.resizable(0,0)

root.update()

def play_song(song_name: StringVar, songs_list: Listbox, status: StringVar):
    song_name.set(songs_list.get(ACTIVE))
    mixer.music.load(songs_list.get(ACTIVE))
    mixer.music.play()
    status.set("Playing song")

def stop_song(status: StringVar):
    mixer.music.stop()
    status.set("Stopped")

def load(listbox):
    os.chdir(filedialog.askdirectory(title='Open songs folder'))
    tracks = os.listdir()
    for track in tracks:
        listbox.insert(END, track)

def pause_song(status: StringVar):
    mixer.music.pause()
    status.set("Paused")

def resume_song(status: StringVar):
    mixer.music.unpause()
    status.set("Resumed")

song_frame = LabelFrame(root, text='Current song', bg='LightBlue', width=450, height=100)
song_frame.place(x=0, y=0)

button_frame = LabelFrame(root, text='Control Buttons', bg='#8cf3e5', width=450, height=130)
button_frame.place(y=100)

listbox_frame = LabelFrame(root, text='Playlist', bg='#1ecbe1', width=400, height=130)
listbox_frame.place(x=450, y=0, height=230, width=350)

current_song = StringVar(root, value='<Not selected>')
song_status = StringVar(root, value='<Not available>')

playList = Listbox(listbox_frame, font=('Helvetica', 12), selectbackground='#0bf414')

scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL)
scroll_bar.pack(side=RIGHT, fill=BOTH)

playList.config(yscrollcommand=scroll_bar.set)

scroll_bar.config(command=playList.yview)

playList.pack(fill=BOTH, padx=5, pady=5)

Label(song_frame, text="Currently Playing :", bg="LightBlue", font=('Times', 11, 'bold')).place(x=5, y=25)

song_label = Label(song_frame, textvariable=current_song, bg='Yellow', font=('Times', 12), width=30)
song_label.place(x=150, y=25)

play_btn = Button(button_frame, text='Play', bg='#7ef0e6', font=("Sans", 13), width=7, command=lambda: play_song(current_song, playList, song_status))
play_btn.place(x=45, y=15)

pause_btn = Button(button_frame, text='Pause', bg='#7ef0e6', font=("Sans", 13), width=7, command=lambda:pause_song(song_status))
pause_btn.place(x=135, y=15)

resume_btn = Button(button_frame, text='Resume', bg='#7ef0e6', font=("Sans", 13), width=7, command=lambda: resume_song(song_status))
resume_btn.place(x=225, y=15)

stop_btn = Button(button_frame, text='Stop', bg='#7ef0e6', font=("Sans", 13), width=7, command=lambda: stop_song(song_status))
stop_btn.place(x=315, y=15)

load_btn = Button(button_frame, text='Load Directory', bg='#7ef0e6', font=("Sans", 13), width=35, command=lambda: load(playList))
load_btn.place(x=55, y=60)

Label(root, textvariable=song_status, bg="#0071ff", font=('Times', 10), justify=LEFT).pack(side=BOTTOM, fill=X)

root.mainloop()