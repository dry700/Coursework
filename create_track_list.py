import tkinter as tk
import tkinter.scrolledtext as tkst

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

        #initiate playlist by read save file
        self.play_list = self.read_list_file()
        #set playlist detail text
        self.detail = ""

        #Label title
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

        #reset list button
        self.reset_button = tk.Button(self,text="Reset list",command=self.reset_list
                                      ,background="red",foreground="white",font=("Helvetica", 15))
        self.reset_button.grid(row=4,column=5)
        #write list on screen
        self.print_detail()

    def add_song(self):
        #avoid the non-number input
        try :
            songnum = int(self.song_number.get())
            # check the validation of number and add song
            if "%02d" % songnum in list(library):  # convert 1 digit number to 2 digits string key and check if track exist
                self.play_list.append("%02d" % songnum) #add track key to playlist
                self.lbl7.configure(text="Track added") #write confirm text
                self.print_detail()#write all track in playlist on screen
            else:
                self.lbl7.configure(text="Song doesn't exist")#write status on screen
            self.write_list_file()#write tracks key in playlist on save file
            self.print_detail()#write playlist on scrolltext
        except ValueError:#if non number input
            self.lbl7.configure(text="Invalid number")#write error text on screen


    def play_tracks_list(self):
        #increase play count of tracks in playlist
        for key in self.play_list:
            lib.increment_play_count(key)
        self.print_detail()#write playlist on scrolltext

    def reset_list(self):
        self.play_list = [] #reset the list
        self.detail = ""#reset the detail
        self.write_list_file()#write playlist on scrolltext

    def write_list_file(self):
        f = open("_play_list.csv","w")#open and overwrite the file
        for track in self.play_list:
            f.write(f'{track},')#write keys in playlist on save file
        f.close()#close file

    def read_list_file(self):
        f = open("_play_list.csv",'r')#open file in readonly mode
        contents = f.read()#read all tracks key as string
        if contents == '':#if string is empty
            f.close()#close file
            return [] #return empty list
        else:
            contents = contents.split(',') #convert string into list
            f.close()#close file
            return contents #return key list

    def print_detail(self):
        tracks_detail ='' #initiate write content
        for key in self.play_list: #get tracks detail
            name = lib.get_name(key) #get track name
            artist = lib.get_artist(key) #get track artist
            play_count = lib.get_play_count(key) #get play count
            tracks_detail += f"{name} - {artist}. Played: {play_count}\n" #add track detail to print content
        self.detail = tracks_detail #set writen content on scroll text
        set_text(self.list_txt, self.detail)#write content on scroll text

if __name__=="__main__":
    create_track_list = Create_track_list()
    create_track_list.mainloop()