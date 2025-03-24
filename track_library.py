from library_item import LibraryItem
import os


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
    f = open("_library.csv", "w")
    for i in range(1, len(library) + 1):
        f.write(f'{library["%02d" % i].name},{library["%02d" % i].artist},{library["%02d" % i].rating},'
                f'{library["%02d" % i].play_count}\n')

def read_library():
    library={}
    with open("_library.csv") as f:
        contents = f.readlines()
        tracks_detail = []
        for content in contents:
            tracks_detail.append(content.strip().split(','))
        i = 1
        for detail in tracks_detail:
            try:
                if int(detail[2]) > 5:
                    library["%02d" % i] = LibraryItem(detail[0],detail[1],5)
                elif int(detail[2]) < 0:
                    library["%02d" % i] = LibraryItem(detail[0],detail[1],0)
                else:
                    library["%02d" % i] = LibraryItem(detail[0],detail[1],int(detail[2]))
                library["%02d" % i].play_count = int(detail[3])
                i+=1
            except IndexError :
                library["%02d" % i] = LibraryItem(detail[0],detail[1],int(detail[2]))
                i += 1
            except ValueError:
                library["%02d" % i] = LibraryItem(detail[0], detail[1], 0)
                i += 1

    return library

library = read_library()

if __name__ == "__main__":
    read_library()
    update_library()

    print(library)
    for key in library:
        print(library[key].info())