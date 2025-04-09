import tkinter as tk #import tkinter
import tkinter.scrolledtext as tkst #import scroll text display

import track_library as lib #import library
import font_manager as fonts #import custom font


def set_text(text_area, content): #display on scroll text function
    text_area.delete("1.0", tk.END) #delete all previous text
    text_area.insert(1.0, content) #display new text


class TrackViewer(): #create view track class
    def __init__(self, window): #class initiate function
        window.geometry("750x350") #set window size
        window.title("View Tracks") #set title
        window.configure(bg="wheat") #set background colour

        #list track button
        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked
                                    ,background="dark orange",foreground="white")
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        #song number input label and entry
        enter_lbl = tk.Label(window, text="Enter Track Number",bg="wheat")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        #check track button
        check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked
                                    ,background="dark orange",foreground="white")
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)

        #scroll text to display tracks list
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        #track detail text display
        self.track_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        #button status text
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10),bg="wheat")
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.list_tracks_clicked() #tracks list display when initiate window

    def view_tracks_clicked(self):                                                      #display track function
        key = self.input_txt.get()                                                      #get track number from entry
        name = lib.get_name(key)                                                        #get track detail from key
        if name is not None:                                                            #if track exist then
            artist = lib.get_artist(key)                                                #get track name
            rating = lib.get_rating(key)                                                #get track rating
            play_count = lib.get_play_count(key)                                        #get track play count
            track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}"  #track detail text
            set_text(self.track_txt, track_details)                                     #track detail text display
        else:                                                                           #if track doesn't exist
            set_text(self.track_txt, f"Track {key} not found")                  #display track not found
        self.status_lbl.configure(text="View Track button was clicked!")                #display view track button was clicked

    def list_tracks_clicked(self):                                           #list all tracks function
        track_list = lib.list_all()                                          #get all tracks detail
        set_text(self.list_txt, track_list)                                  #display all tracks
        self.status_lbl.configure(text="List Tracks button was clicked!")    #display list track button was clicked

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    TrackViewer(window)     # open the TrackViewer GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
