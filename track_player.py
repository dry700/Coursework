import tkinter as tk
import font_manager as fonts
from view_tracks import TrackViewer
from create_track_list import Create_track_list
from update_tracks import Update_tracks

class Track_player(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("520x150")
        self.title("Omni-player")
        self.configure(bg="wheat")

        fonts.configure()

        #header label
        self.header_lbl = tk.Label(self, text="Select an option by clicking one of the buttons below")
        self.header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        #view track button
        self.view_tracks_btn = tk.Button(self, text="View Tracks", command=self.view_tracks_clicked,
                                         background="dark orange",foreground="cyan")
        self.view_tracks_btn.grid(row=1, column=0, padx=10, pady=10)

        #create track button
        self.create_track_list_btn = tk.Button(self, text="Create Track List",command=self.create_track_list,
                                               background="dark orange",foreground="cyan")
        self.create_track_list_btn.grid(row=1, column=1, padx=10, pady=10)

        #update track button
        self.update_tracks_btn = tk.Button(self, text="Update Tracks",command=self.update_tracks_clicked,
                                           background="dark orange",foreground="cyan")
        self.update_tracks_btn.grid(row=1, column=2, padx=10, pady=10)

        self.status_lbl = tk.Label(self, bg='wheat', text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    def view_tracks_clicked(self):
        self.status_lbl.configure(text="View Tracks button was clicked!")
        TrackViewer(tk.Toplevel(self))

    def create_track_list(self):
        self.status_lbl.configure(text="Create Tracks List button was clicked!")
        create_tracks = Create_track_list()
        create_tracks.mainloop()

    def update_tracks_clicked(self):
        self.status_lbl.configure(text="Update tracks button was clicked")
        Update_tracks()

if __name__ == "__main__":
    track_player = Track_player()
    track_player.mainloop()