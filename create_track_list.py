import tkinter as tk
import tkinter.scrolledtext as tkst
from library_item import LibraryItem
import font_manager as fonts
from track_library import library
import track_library as lib

def set_text(text_area, content): #display on scroll text function
    text_area.delete("1.0", tk.END) #delete all previous text
    text_area.insert(1.0, content) #display new text

class Create_track_list(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Create Track List")
        self.geometry("600x400")
        self.configure(bg="wheat")


        self.play_list = []
        self.detail = ""

        #Label to guide user
        self.lbl1 = tk.Label(self,text="Create play list",font=("Arial",20,"bold"),bg="wheat")
        self.lbl1.grid(row=0,column=0,columnspan=10,sticky=tk.S)

        #Song number label and input
        self.lbl2 = tk.Label(self,text="Song number:",bg="wheat",font=("Helvetica", 15))
        self.lbl2.grid(row=1,column=0,sticky=tk.E)
        self.song_number = tk.Entry(self,width=3)
        self.song_number.grid(row=1,column=1,sticky=tk.W)

        #Song add button
        self.add_btn = tk.Button(self, text="Add song",command=self.add_song,
                                 background="dark orange",foreground="cyan",font=("Helvetica", 15))
        self.add_btn.grid(row=1, column=5,columnspan=2, sticky=tk.SE)

        #Track list label
        self.lbl6 = tk.Label(self, text="Tracks list",bg="wheat",font=("Helvetica", 12))
        self.lbl6.grid(row=4, column=0, sticky=tk.SW,padx=10)

        #Label state
        self.lbl7 =tk.Label(self,text="",bg="wheat",font=("Helvetica", 12))
        self.lbl7.grid(row=3,column=0, columnspan=5)

        #list of song
        self.list_txt = tkst.ScrolledText(self, width=48, height=12, wrap="none",font=("Helvetica", 12))
        self.list_txt.grid(row=5, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        #play all tracks
        self.play_btn = tk.Button(self,text="Play",command=self.play_tracks_list
                                  ,background="dark orange",foreground="cyan",font=("Helvetica", 15))
        self.play_btn.grid(row=5,column=5)

        self.reset_button = tk.Button(self,text="Reset list",command=self.reset_list
                                      ,background="red",foreground="white",font=("Helvetica", 15))
        self.reset_button.grid(row=4,column=5)

    def add_song(self):

        tracks_detail = ''

        #avoid the non-number input
        try :
            songnum = int(self.song_number.get())
        except ValueError:
            self.lbl7.configure(text="Invalid number")
            return

        #check the validation of number and add song
        if f'0{songnum}' in list(library) or f'{songnum}' in list(library):
            if songnum<10: #If number lesser than 10 add a zero in-front of it. ex: 1 -> 01
                self.play_list.append(f'0{songnum}')
                self.lbl7.configure(text="Track added")
            else: # if number have 2 or more digit, it will be untouched
                self.play_list.append(f'{songnum}')
                self.lbl7.configure(text="Track added")

            for key in self.play_list:
                name = lib.get_name(key)
                artist = lib.get_artist(key)
                play_count = lib.get_play_count(key)
                tracks_detail += f"{name} - {artist}. Played: {play_count}\n"
            self.detail = tracks_detail
        else:
            self.lbl7.configure(text="Song doesn't exist")

        set_text(self.list_txt, self.detail)

    def play_tracks_list(self):
        tracks_detail = ''
        for key in self.play_list:
            lib.increment_play_count(key)

        for key in self.play_list:
            name = lib.get_name(key)
            artist = lib.get_artist(key)
            play_count = lib.get_play_count(key)
            tracks_detail += f"{name} - {artist}. Played: {play_count}\n"
        self.detail = tracks_detail

        set_text(self.list_txt, self.detail)

    def reset_list(self):
        self.play_list = []
        self.detail = ""
        set_text(self.list_txt,self.detail)


if __name__=="__main__":
    create_track_list = Create_track_list()
    create_track_list.mainloop()