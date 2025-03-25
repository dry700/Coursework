import tkinter as tk
import tkinter.scrolledtext as tkst

from track_library import library
import track_library as lib

def set_text(text_area, content): #display on scroll text function
    text_area.delete("1.0", tk.END) #delete all previous text
    text_area.insert(1.0, content) #display new text


class Update_tracks(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Update tracks list")
        self.geometry("400x150")
        self.configure(bg="wheat")

        self.lbl_title = tk.Label(self,text="Update track information",font=("Arial",20,"bold"),bg="wheat")
        self.lbl_title.grid(row=0,column=0,columnspan=6,pady=10,sticky=tk.S)

        self.lbl1 = tk.Label(self,text="Enter \ntrack number",font=("Helvetica", 10,"bold"),bg="wheat")
        self.lbl1.grid(row=1,column=0)
        self.number_entry = tk.Entry(self,width=5)
        self.number_entry.grid(row=1,column=1,sticky=tk.W)

        self.lbl2 = tk.Label(self,text="Enter \nnew rating",font=("Helvetica", 10,"bold"),bg="wheat")
        self.lbl2.grid(row=1,column=2)
        self.rating_entry = tk.Entry(self, width=5)
        self.rating_entry.grid(row=1, column=3, sticky=tk.W)

        self.update_track_btn = tk.Button(self,text="Update track",font=("Helvetica", 10),bg="dark orange",fg="cyan"
                                        ,command=self.update_track)
        self.update_track_btn.grid(row=1,column=5,sticky=tk.SW)



    def update_track(self):
        #self.lbl_err.destroy()
        self.change_window()
        try:
            new_rating = int(self.rating_entry.get())
            if new_rating > 5 or new_rating < 0:
                set_text(self.new_detail, "Invalid rating input")
                return

        except ValueError:
            set_text(self.new_detail, "Invalid rating input")
            return

        try:
            track_number = int(self.number_entry.get())
            key = "%02d" % track_number
            name = lib.get_name(key)
            lib.set_rating(key,new_rating)
            if name is not None:  # if track exist then
                artist = lib.get_artist(key)  # get track name
                rating = lib.get_rating(key)  # get track rating
                play_count = lib.get_play_count(key)  # get track play count
                track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}"  # track detail text
                set_text(self.new_detail, track_details)  # track detail text display
            else:  # if track doesn't exist
                set_text(self.new_detail, f"Track {key} not found")  # display track not found
        except ValueError:
            set_text(self.new_detail, "Invalid number input")

    def change_window(self):
        self.geometry("400x250")

        self.lbl_current = tk.Label(self, text="New detail", font=("Helvetica", 10, "bold"), bg="wheat")
        self.lbl_current.grid(row=3, column=0, sticky=tk.SW)
        self.new_detail = tk.Text(self, width=26, height=5, wrap="none")
        self.new_detail.grid(row=4, column=0, columnspan=5)


if __name__ == "__main__":
    update_tracks = Update_tracks()
    update_tracks.mainloop()