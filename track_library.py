from library_item import LibraryItem


"""library["01"] = LibraryItem("Another Brick in the Wall", "Pink Floyd", 4)
library["02"] = LibraryItem("Stayin' Alive", "Bee Gees", 5)
library["03"] = LibraryItem("Highway to Hell ", "AC/DC", 2)
library["04"] = LibraryItem("Shape of You", "Ed Sheeran", 1)
library["05"] = LibraryItem("Someone Like You", "Adele", 3)
library["06"] = LibraryItem("Beat It","Micheal Jackson",5)"""


def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output


def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None


def get_artist(key):
    try:
        item = library[key]
        return item.artist
    except KeyError:
        return None


def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1


def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
        update_library()
    except KeyError:
        return


def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1


def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
        update_library()
    except KeyError:
        return

def update_library():
    f = open("_library.csv", "w")#open file to write
    for i in range(1, len(library) + 1): #write all track in library into file
        f.write(f'{library["%02d" % i].name},{library["%02d" % i].artist},{library["%02d" % i].rating},'
                f'{library["%02d" % i].play_count}\n')
    f.close()#close file

def read_library():
    library={} #initiate track library
    with open("_library.csv","r") as f: #open save file in readonly mode and auto close
        contents = f.readlines() #read all track in file save
        tracks_detail = [] #initiate detail list
        for content in contents:
            tracks_detail.append(content.strip().split(','))#split detail texts into lists
        i = 1 #start from first key in library
        for detail in tracks_detail:
            try: #avoid invalid rating and play count
                if int(detail[2]) > 5:#if rating greater than 5
                    library["%02d" % i] = LibraryItem(detail[0],detail[1],5)#add track with rating = 5
                elif int(detail[2]) < 0: #if rating lesser than 0
                    library["%02d" % i] = LibraryItem(detail[0],detail[1])#add track with rating = 0
                else:#if rating is valid
                    library["%02d" % i] = LibraryItem(detail[0],detail[1],int(detail[2]))#add track
                library["%02d" % i].play_count = int(detail[3])#set play count
                i+=1 #increase key index
            except IndexError: #if there is no play count
                library["%02d" % i] = LibraryItem(detail[0],detail[1],int(detail[2]))#add track playcount = 0
                i += 1 #increase key index
            except ValueError:#if there is no rating or play count
                library["%02d" % i] = LibraryItem(detail[0], detail[1])#add track with playcount = 0 and rating = 0
                i += 1 #increase key index

    return library #return the track library

library = read_library() #initiate track library from save file

if __name__ == "__main__":
    read_library()
    update_library()